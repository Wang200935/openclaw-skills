import os, json, re
from datetime import datetime

BASE_DIR = os.environ.get("OPENCLAW_HOME", os.path.expanduser("~/.openclaw"))
OUT_DIR = os.path.join(BASE_DIR, "workspace_second", "data", "bhuntr")
IN_FILE = os.path.join(OUT_DIR, "events.json")
OUT_MD = os.path.join(OUT_DIR, "daily_summary.md")


def parse_date(s: str):
    if not s:
        return None
    # try YYYY-MM-DD or YYYY/MM/DD
    m = re.search(r"(20\d{2})[-/](\d{1,2})[-/](\d{1,2})", s)
    if not m:
        return None
    y, mo, d = map(int, m.groups())
    try:
        return datetime(y, mo, d)
    except Exception:
        return None


def main():
    if not os.path.exists(IN_FILE):
        print("[BHuntr] events.json not found")
        return

    data = json.load(open(IN_FILE, "r", encoding="utf-8"))
    items = data.get("info_events") or []

    # sort by start date if available
    def key(it):
        dt = parse_date(it.get("start_date", ""))
        return dt or datetime.max

    items = sorted(items, key=key)

    lines = []
    lines.append(f"# BHuntr 資訊類活動/比賽速報\n")
    lines.append(f"更新時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"共 {len(items)} 則\n")

    for it in items:
        title = it.get("title") or "(無標題)"
        url = it.get("url") or ""
        start = it.get("start_date") or ""
        end = it.get("end_date") or ""
        org = it.get("organizer") or ""
        loc = it.get("location") or ""
        summary = (it.get("summary") or "").strip()
        summary = summary[:200] + ("..." if len(summary) > 200 else "")
        lines.append(f"## {title}")
        if url:
            lines.append(f"- 連結：{url}")
        if start or end:
            lines.append(f"- 時間：{start} ~ {end}")
        if org:
            lines.append(f"- 主辦：{org}")
        if loc:
            lines.append(f"- 地點：{loc}")
        if summary:
            lines.append(f"- 簡介：{summary}")
        lines.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))


if __name__ == "__main__":
    main()
