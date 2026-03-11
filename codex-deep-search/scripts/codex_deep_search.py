import argparse
import json
import os
import re
import subprocess
import tempfile
import urllib.request
from html import unescape
from pathlib import Path

try:
    import winreg
except ImportError:
    winreg = None

TAVILY_URL = 'https://api.tavily.com/search'
SERPER_URL = 'https://google.serper.dev/search'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) OpenClaw/1.0'
OPENCODE_CONFIG = r'C:\Users\wang\.config\opencode\opencode.json'
OPENCODE_MODEL = 'wangchatai/gpt-5.3-codex'
OPENCODE_BIN = r'C:\Users\wang\AppData\Roaming\npm\opencode.cmd'


def get_user_env(name: str) -> str:
    val = os.environ.get(name)
    if val:
        return val
    if winreg is None:
        return ''
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment')
        value, _ = winreg.QueryValueEx(key, name)
        return str(value).strip()
    except OSError:
        return ''


def post_json(url, payload, headers=None, timeout=60):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.add_header('User-Agent', USER_AGENT)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8', errors='replace'))


def get_text(url, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'text/html,application/xhtml+xml'})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get('Content-Type', '')
        if 'text' not in content_type and 'html' not in content_type:
            return ''
        html = resp.read().decode('utf-8', errors='replace')
    html = re.sub(r'<script[\s\S]*?</script>', ' ', html, flags=re.I)
    html = re.sub(r'<style[\s\S]*?</style>', ' ', html, flags=re.I)
    html = re.sub(r'<noscript[\s\S]*?</noscript>', ' ', html, flags=re.I)
    text = re.sub(r'<[^>]+>', ' ', html)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:12000]


def tavily_search(query, max_results):
    api_key = get_user_env('TAVILY_API_KEY')
    if not api_key:
        return []
    payload = {'api_key': api_key, 'query': query, 'max_results': max_results, 'search_depth': 'advanced'}
    data = post_json(TAVILY_URL, payload)
    return [{'source': 'tavily', 'title': i.get('title', ''), 'url': i.get('url', ''), 'snippet': i.get('content', '')} for i in data.get('results', [])]


def serper_search(query, max_results):
    api_key = get_user_env('SERPER_API_KEY')
    if not api_key:
        return []
    payload = {'q': query, 'num': max_results}
    data = post_json(SERPER_URL, payload, headers={'X-API-KEY': api_key})
    return [{'source': 'serper', 'title': i.get('title', ''), 'url': i.get('link', ''), 'snippet': i.get('snippet', '')} for i in data.get('organic', [])]


def dedupe_results(items):
    seen = set()
    out = []
    for item in items:
        url = item.get('url', '').strip()
        if not url or url in seen:
            continue
        seen.add(url)
        out.append(item)
    return out


def build_research_pack(query, fetched):
    lines = ['# Deep Search Research Pack', '', f'Query: {query}', '']
    for idx, item in enumerate(fetched, start=1):
        lines.extend([
            f'## Source {idx}',
            f'URL: {item["url"]}',
            f'Title: {item["title"]}',
            f'Snippet: {item["snippet"]}',
            '',
            item['content'] or '(no extracted content)',
            ''
        ])
    return '\n'.join(lines)


def clean_opencode_output(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        if line.strip().startswith('> '):
            continue
        if line.strip() == '[0m':
            continue
        cleaned.append(line)
    return '\n'.join(cleaned).strip()


def call_opencode(material_path, query):
    prompt = (
        'Read the attached research pack and answer the query in markdown. '
        'Be source-grounded and only use the provided materials. '
        'Required sections: Title, Short answer, What the sources show, Credible vs uncertain, Sources. '
        f'Query: {query}'
    )
    env = os.environ.copy()
    env['OPENCODE_CONFIG'] = OPENCODE_CONFIG
    proc = subprocess.run(
        [OPENCODE_BIN, 'run', '--model', OPENCODE_MODEL, prompt, '--file', material_path],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        env=env,
        timeout=240,
        check=True,
        shell=False,
    )
    return clean_opencode_output(proc.stdout)


def run(query, max_results, fetch_pages, out_path=None):
    search_results = tavily_search(query, max_results) + serper_search(query, max_results)
    merged = dedupe_results(search_results)
    fetched = []
    for item in merged[:fetch_pages]:
        try:
            content = get_text(item['url'])
        except Exception:
            content = ''
        fetched.append({**item, 'content': content})

    if not fetched:
        answer = '# Deep Search\n\nNo search results were fetched.'
    else:
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.md', encoding='utf-8') as tmp:
            tmp.write(build_research_pack(query, fetched))
            temp_path = tmp.name
        try:
            answer = call_opencode(temp_path, query)
        finally:
            try:
                os.unlink(temp_path)
            except OSError:
                pass

    if out_path:
        Path(out_path).write_text(answer, encoding='utf-8')
        print(f'WROTE:{out_path}')
    else:
        print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deep web research using Tavily + Serper + OpenCode synthesis')
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=8)
    parser.add_argument('--fetch_pages', type=int, default=5)
    parser.add_argument('--out', required=False)
    args = parser.parse_args()
    run(args.query, args.max_results, args.fetch_pages, args.out)
