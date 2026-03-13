#!/usr/bin/env python3
"""First-pass crawler skeleton for collecting Chinese news titles.

This file is intentionally written as a reusable starter template for ONE
news-site pattern. It is not a finished universal crawler.

What this script already does:
- Uses a polite requests.Session with retry behavior and headers.
- Defines a CSV-ready row schema for downstream labeling/training.
- Separates site configuration from crawling logic.
- Provides placeholders for site-specific list-item selectors and next-page rules.
- Normalizes whitespace and timestamps where possible.

What still needs manual site-specific work:
- CSS selectors / HTML structure for the target site.
- Pagination rule for the chosen section/search page.
- Optional article-page parsing if title/date are not complete on list pages.
- Legal/ethical review of the site's robots.txt and terms before real use.

Suggested usage:
1. Pick ONE site and fill in TARGET_SITE.
2. Adjust selectors in extract_list_rows().
3. Test on a very small page range first.
4. Export CSV and review data quality manually before scaling up.
"""

from __future__ import annotations

import csv
import random
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ---------------------------------------------------------------------------
# Output schema
# ---------------------------------------------------------------------------
# These columns are designed to be CSV-ready for later manual labeling,
# cleaning, and machine-learning experiments.
CSV_COLUMNS = [
    "source_site",
    "section",
    "list_page_url",
    "article_url",
    "title",
    "subtitle",
    "published_at_raw",
    "published_at_iso",
    "crawl_time_iso",
    "language",
    "country",
    "collector_version",
    "notes",
]

COLLECTOR_VERSION = "news-title-skeleton-v1"
DEFAULT_TIMEOUT = 20
DEFAULT_SLEEP_RANGE = (1.5, 3.5)  # polite delay between requests in seconds


@dataclass(frozen=True)
class SiteConfig:
    """Configuration for one news-source pattern.

    Replace these placeholders with a real target site before production use.
    """

    source_site: str
    country: str
    language: str
    start_urls: list[str]
    section_name: str
    allowed_domain: str
    # Optional URL template if the site uses page-number pagination.
    pagination_template: Optional[str] = None
    max_pages: int = 3


# ---------------------------------------------------------------------------
# TODO: Replace this placeholder config with one real site you plan to study.
# Example idea:
#   source_site="example_news",
#   start_urls=["https://example.com/news/politics"],
#   pagination_template="https://example.com/news/politics?page={page}",
# ---------------------------------------------------------------------------
TARGET_SITE = SiteConfig(
    source_site="replace_me_news_site",
    country="Taiwan",
    language="zh",
    start_urls=["https://example.com/news"],
    section_name="general",
    allowed_domain="example.com",
    pagination_template="https://example.com/news?page={page}",
    max_pages=3,
)


def build_session() -> requests.Session:
    """Create a polite HTTP session with retries and browser-like headers."""
    session = requests.Session()

    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "HEAD"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36 "
                "NewsTitleResearchBot/0.1 (academic-use; polite crawling)"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.6",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Connection": "keep-alive",
        }
    )
    return session


def polite_sleep() -> None:
    delay = random.uniform(*DEFAULT_SLEEP_RANGE)
    time.sleep(delay)


def fetch_html(session: requests.Session, url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Fetch one page with timeout and basic status checking."""
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def normalize_text(text: Optional[str]) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def normalize_datetime(raw_text: str) -> str:
    """Best-effort datetime normalization.

    This is intentionally conservative. Many news sites use different formats,
    so you may need to add parsing rules for the chosen source.
    """
    raw_text = normalize_text(raw_text)
    if not raw_text:
        return ""

    known_formats = [
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ]
    for fmt in known_formats:
        try:
            dt = datetime.strptime(raw_text, fmt)
            return dt.isoformat()
        except ValueError:
            continue

    # TODO: Add site-specific date parsing here if the site uses localized text,
    # e.g. "2026年03月10日 09:15" or relative time formats.
    return ""


def iter_list_page_urls(config: SiteConfig) -> Iterator[str]:
    """Yield list-page URLs to crawl.

    Current behavior:
    - uses start_urls directly
    - optionally expands a simple page-number template

    TODO for a real site:
    - if the site uses 'next' links, replace this with HTML-based pagination
    - if the site uses AJAX/infinite scroll, inspect the network API first
    """
    yielded = set()

    for url in config.start_urls:
        if url not in yielded:
            yielded.add(url)
            yield url

    if config.pagination_template:
        for page in range(2, config.max_pages + 1):
            url = config.pagination_template.format(page=page)
            if url not in yielded:
                yielded.add(url)
                yield url


def extract_list_rows(html: str, page_url: str, config: SiteConfig) -> list[dict[str, str]]:
    """Extract article rows from one list page.

    IMPORTANT: This function is the main site-specific placeholder.
    You MUST inspect the target site's HTML and update the selectors below.
    """
    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict[str, str]] = []

    # -----------------------------------------------------------------------
    # TODO: Replace selectors below with the real structure for your site.
    # Common patterns you might try after inspecting the site:
    # - article teaser blocks: "article", ".news-item", ".story-list__item"
    # - title link: "h2 a", "a.title", ".news-title a"
    # - subtitle/summary: ".summary", ".desc", "p"
    # - timestamp: "time", ".date", ".publish-time"
    # -----------------------------------------------------------------------
    candidate_items = soup.select("article")

    for item in candidate_items:
        title_link = item.select_one("h1 a, h2 a, h3 a, a")
        if not title_link:
            continue

        title = normalize_text(title_link.get_text(" ", strip=True))
        href = normalize_text(title_link.get("href"))
        article_url = urljoin(page_url, href) if href else ""

        subtitle_node = item.select_one("p, .summary, .desc, .subtitle")
        subtitle = normalize_text(subtitle_node.get_text(" ", strip=True) if subtitle_node else "")

        time_node = item.select_one("time, .date, .time, .publish-time")
        published_at_raw = normalize_text(
            time_node.get("datetime") if time_node and time_node.get("datetime") else (
                time_node.get_text(" ", strip=True) if time_node else ""
            )
        )
        published_at_iso = normalize_datetime(published_at_raw)

        if not title:
            continue

        rows.append(
            {
                "source_site": config.source_site,
                "section": config.section_name,
                "list_page_url": page_url,
                "article_url": article_url,
                "title": title,
                "subtitle": subtitle,
                "published_at_raw": published_at_raw,
                "published_at_iso": published_at_iso,
                "crawl_time_iso": datetime.now(timezone.utc).isoformat(),
                "language": config.language,
                "country": config.country,
                "collector_version": COLLECTOR_VERSION,
                "notes": "first-pass list-page extraction",
            }
        )

    return rows


def deduplicate_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    unique_rows: list[dict[str, str]] = []
    for row in rows:
        key = (row.get("article_url", ""), row.get("title", ""))
        if key in seen:
            continue
        seen.add(key)
        unique_rows.append(row)
    return unique_rows


def save_csv(rows: Iterable[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in CSV_COLUMNS})


def crawl_site(config: SiteConfig, output_path: Path) -> list[dict[str, str]]:
    session = build_session()
    all_rows: list[dict[str, str]] = []

    for idx, page_url in enumerate(iter_list_page_urls(config), start=1):
        print(f"[{idx}] Fetching: {page_url}")
        try:
            html = fetch_html(session, page_url)
            rows = extract_list_rows(html, page_url, config)
            print(f"    Extracted rows: {len(rows)}")
            all_rows.extend(rows)
        except requests.RequestException as exc:
            print(f"    Request failed: {exc}", file=sys.stderr)
        except Exception as exc:  # keep first-pass script resilient during exploration
            print(f"    Parse failed: {exc}", file=sys.stderr)

        polite_sleep()

    unique_rows = deduplicate_rows(all_rows)
    save_csv(unique_rows, output_path)
    return unique_rows


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / ".." / "data" / f"{TARGET_SITE.source_site}_titles_first_pass.csv"
    output_path = output_path.resolve()

    print("Starting first-pass news title collection...")
    print(f"Target site: {TARGET_SITE.source_site}")
    print(f"Output CSV: {output_path}")
    print()

    # Final safety reminder for real usage.
    if TARGET_SITE.source_site == "replace_me_news_site":
        print(
            "WARNING: TARGET_SITE is still a placeholder. "
            "Update the config and selectors before real crawling.",
            file=sys.stderr,
        )

    rows = crawl_site(TARGET_SITE, output_path)
    print()
    print(f"Done. Saved {len(rows)} unique rows.")
    print("Next step: inspect the CSV manually and refine selectors if needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
