---
name: bhuntr-event-monitor
description: Monitor https://bhuntr.com/tw for information-related competitions/activities, scrape all subpages/events, store structured data, and produce daily7am briefings. Use when running the scheduled BHuntr monitoring job or when updating the data files manually.
---

# BHuntr Event Monitor

## Purpose
Continuously scan **https://bhuntr.com/tw** every10 minutes, deeply fetch each event subpage, **recursively crawl all bhuntr.com subpages (no depth limit, de-duplicated)**, extract structured fields, filter **information/tech-related** events, store results, and produce a **daily07:00 report** for the user.

## Tools used
- **Python3**
- **requests** (HTTP fetch)
- **BeautifulSoup (bs4)** (HTML parsing; fallback to regex if unavailable)
- **OpenClaw cron** (scheduled runs)

## Data locations
- **Raw+filtered data:** `<OPENCLAW_HOME>/workspace_second/data/bhuntr/events.json`
- **Daily summary output:** `<OPENCLAW_HOME>/workspace_second/data/bhuntr/daily_summary.md`
- **Logs:** `<OPENCLAW_HOME>/workspace_second/data/bhuntr/logs/bhuntr_scrape.log`

## How to run manually
```powershell
python <OPENCLAW_HOME>/skills/bhuntr-event-monitor/scripts/scrape_bhuntr.py
python <OPENCLAW_HOME>/skills/bhuntr-event-monitor/scripts/summarize_bhuntr.py
```

## Scheduling (cron)
Create **two isolated cron jobs**:

###1) Every10 minutes: scrape & store
```powershell
openclaw cron add \
 --name "BHuntr scrape" \
 --cron "*/10 * * * *" \
 --tz "Asia/Taipei" \
 --session isolated \
 --message "Use bhuntr-event-monitor skill to run scrape_bhuntr.py and update events.json" \
 --delivery none
```

###2) Daily07:00: summarize & notify
```powershell
openclaw cron add \
 --name "BHuntr daily brief" \
 --cron "0 7 * * *" \
 --tz "Asia/Taipei" \
 --session isolated \
 --message "Use bhuntr-event-monitor skill to run summarize_bhuntr.py and post today’s info/tech events" \
 --announce
```

## Output schema (events.json)
Each event item includes:
- `id`: stable hash
- `title`
- `url`
- `category/tags`
- `start_date`, `end_date` (if detected)
- `organizer` (if detected)
- `location` (if detected)
- `summary`
- `is_info_related`: boolean
- `fetched_at`

Top-level payload includes:
- `total`, `info_total`
- `page_total` and `pages` (all crawled URLs)

## Filtering rule (資訊類)
Mark as **資訊/科技/AI/資安/程式/資料** related if title/summary/tags contain any of:
```
資訊, 科技, AI, 人工智慧, 資安, 程式, 程式設計, Coding, 軟體, 開發, 電腦,
資料, Data, 機器學習, 深度學習, 雲端, 網路, 黑客松, Hackathon
```

## Notes
- If site uses heavy JS and data is missing, script will attempt to discover API endpoints from JS bundles.
- If no API endpoints are found, script crawls all same-domain pages and extracts event subpages.
