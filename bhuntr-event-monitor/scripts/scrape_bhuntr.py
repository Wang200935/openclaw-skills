import os, re, json, time, hashlib
from datetime import datetime
from urllib.parse import urljoin, urlparse, urldefrag
import requests

BASE = "https://bhuntr.com"
START_URL = "https://bhuntr.com/tw"

BASE_DIR = os.environ.get("OPENCLAW_HOME", os.path.expanduser("~/.openclaw"))
OUT_DIR = os.path.join(BASE_DIR, "workspace_second", "data", "bhuntr")
LOG_DIR = os.path.join(OUT_DIR, "logs")
OUT_FILE = os.path.join(OUT_DIR, "events.json")
LOG_FILE = os.path.join(LOG_DIR, "bhuntr_scrape.log")

KEYWORDS = [
    "資訊", "科技", "AI", "人工智慧", "資安", "程式", "程式設計", "Coding", "軟體", "開發", "電腦",
    "資料", "Data", "機器學習", "深度學習", "雲端", "網路", "黑客松", "Hackathon"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8"
}


def log(msg: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")


def fetch(url, timeout=25):
    for _ in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200:
                return r.text
        except Exception:
            time.sleep(1)
    return ""


def find_js_chunks(html: str):
    return list(set(re.findall(r"/react/js/[^\"']+\.js(?:\?[^\"']+)?", html)))


def discover_api_endpoints(html: str):
    endpoints = set()
    chunks = find_js_chunks(html)
    for c in chunks:
        js = fetch(BASE + c)
        if not js:
            continue
        for m in re.findall(r"/api/[^\"']+", js):
            if ":" in m or "{" in m or "}" in m:
                continue
            endpoints.add(m)
    return list(endpoints)


def extract_items(data):
    items = []
    if isinstance(data, list):
        items += data
    elif isinstance(data, dict):
        for k in ("items", "data", "list", "records", "contests", "events"):
            if k in data:
                items += extract_items(data[k])
        for v in data.values():
            if isinstance(v, (list, dict)):
                items += extract_items(v)
    return items


def normalize_item(item: dict):
    title = item.get("title") or item.get("name") or item.get("contestName") or ""
    url = item.get("url") or item.get("link") or ""
    if not url:
        slug = item.get("slug") or item.get("id") or item.get("contestId")
        if slug:
            url = f"{BASE}/tw/contest/{slug}" if "/contest" not in str(slug) else f"{BASE}{slug}"
    summary = item.get("summary") or item.get("description") or item.get("intro") or ""
    tags = item.get("tags") or item.get("category") or item.get("categories") or []
    if isinstance(tags, str):
        tags = [tags]
    start_date = item.get("startDate") or item.get("start_at") or item.get("start") or ""
    end_date = item.get("endDate") or item.get("end_at") or item.get("end") or ""
    organizer = item.get("organizer") or item.get("host") or ""
    location = item.get("location") or item.get("place") or ""

    text_blob = " ".join([title, summary, " ".join(tags)])
    is_info = any(k.lower() in text_blob.lower() for k in KEYWORDS)

    base = f"{title}|{url}"
    eid = hashlib.md5(base.encode("utf-8")).hexdigest()

    return {
        "id": eid,
        "title": title,
        "url": url,
        "tags": tags,
        "start_date": start_date,
        "end_date": end_date,
        "organizer": organizer,
        "location": location,
        "summary": summary,
        "is_info_related": is_info,
        "fetched_at": datetime.now().isoformat(),
    }


def parse_event_page(url: str):
    html = fetch(url)
    if not html:
        return None
    title = ""
    m = re.search(r"<meta property=\"og:title\" content=\"([^\"]+)\"", html)
    if m:
        title = m.group(1)
    if not title:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    desc = ""
    m = re.search(r"<meta property=\"og:description\" content=\"([^\"]+)\"", html)
    if m:
        desc = m.group(1)
    text_blob = " ".join([title, desc])
    is_info = any(k.lower() in text_blob.lower() for k in KEYWORDS)
    eid = hashlib.md5(f"{title}|{url}".encode("utf-8")).hexdigest()
    return {
        "id": eid,
        "title": title,
        "url": url,
        "tags": [],
        "start_date": "",
        "end_date": "",
        "organizer": "",
        "location": "",
        "summary": desc,
        "is_info_related": is_info,
        "fetched_at": datetime.now().isoformat(),
    }


def is_static_asset(url: str):
    path = urlparse(url).path.lower()
    return re.search(r"\.(css|js|png|jpg|jpeg|webp|svg|woff2?|ttf|ico|mp4|mp3|json)$", path) is not None or "/react/" in path


def extract_links(html: str, base_url: str):
    links = set()
    for href in re.findall(r"href=[\"']([^\"']+)[\"']", html, re.I):
        href = href.strip()
        if not href or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:") or href.startswith("tel:"):
            continue
        full = urljoin(base_url, href)
        full, _ = urldefrag(full)
        if is_static_asset(full):
            continue
        links.add(full)
    return links


def is_same_domain(url: str):
    return urlparse(url).netloc.endswith("bhuntr.com")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    log("start scrape")

    html = fetch(START_URL)
    if not html:
        log("failed to fetch homepage")
        return

    endpoints = discover_api_endpoints(html)
    items = []

    # try api endpoints
    for ep in endpoints:
        try:
            url = BASE + ep
            r = requests.get(url, headers=HEADERS, timeout=20)
            if r.status_code != 200:
                continue
            data = r.json()
            raw_items = extract_items(data)
            for it in raw_items:
                if isinstance(it, dict):
                    norm = normalize_item(it)
                    if norm.get("title"):
                        items.append(norm)
        except Exception:
            continue

    # crawl all subpages (no depth limit) within bhuntr.com
    seen = set()
    seed_routes = [
        START_URL,
        BASE + "/tw/contest",
        BASE + "/tw/event",
        BASE + "/tw/activity",
        BASE + "/tw/topic",
        BASE + "/tw/category",
        BASE + "/tw/tag",
        BASE + "/tw/info",
        BASE + "/tw/other",
        BASE + "/tw/portfolio",
        BASE + "/tw/timeline",
    ]
    queue = seed_routes[:]
    all_pages = []

    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        if not is_same_domain(url):
            continue
        seen.add(url)
        page_html = fetch(url)
        if not page_html:
            continue
        all_pages.append(url)

        # extract potential event pages while crawling
        if re.search(r"/tw/(?:contest|event|activity)/", url):
            ev = parse_event_page(url)
            if ev:
                items.append(ev)

        # enqueue links
        for link in extract_links(page_html, url):
            if is_same_domain(link) and link not in seen:
                queue.append(link)

        time.sleep(0.5)

    # fallback: find candidate links in HTML if still empty
    if not items:
        links = set(re.findall(r"/tw/(?:contest|event|activity)/[^\"'#? ]+", html))
        for l in links:
            full = BASE + l
            ev = parse_event_page(full)
            if ev:
                items.append(ev)

    # dedupe by id
    dedup = {}
    for it in items:
        dedup[it["id"]] = it
    items = list(dedup.values())

    info_items = [i for i in items if i.get("is_info_related")]

    payload = {
        "fetched_at": datetime.now().isoformat(),
        "total": len(items),
        "info_total": len(info_items),
        "page_total": len(all_pages),
        "pages": all_pages,
        "events": items,
        "info_events": info_items,
    }

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    log(f"done pages={len(all_pages)} total={len(items)} info={len(info_items)}")


if __name__ == "__main__":
    main()
