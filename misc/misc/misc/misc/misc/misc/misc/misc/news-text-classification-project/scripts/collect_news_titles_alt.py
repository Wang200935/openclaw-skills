#!/usr/bin/env python3
"""Alternative first-pass crawler skeleton for a non-CNA general news site.

This script is a second crawler template intended for a different news-site
pattern than the existing CNA-oriented collector. It assumes a more typical
"category/list page -> article teasers" structure commonly seen on general
news websites.

What this skeleton is for:
- Crawl category/list pages from one general news site.
- Extract CSV-ready rows with title-focused metadata.
- Provide clear placeholders for site-specific selectors and pagination rules.
- Stay easy to adapt for a student research / small-paper workflow.

What still needs manual work:
- Replace TARGET_SITE with one real target news site.
- Inspect actual HTML and update selectors in extract_articles_from_category().
- Decide how category pages paginate on that site.
- Optionally fetch article pages when list pages do not expose full date/title.
- Review robots.txt / site terms before running at scale.
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
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


CSV_COLUMNS = [
    "source_site",
    "category",
    "category_url",
    "list_page_url",
    "article_url",
    "title",
    "summary",
    "published_at_raw",
    "published_at_iso",
    "crawl_time_iso",
    "language",
    "country",
    "collector_version",
    "notes",
]

COLLECTOR_VERSION = "news-title-alt-skeleton-v1"
DEFAULT_TIMEOUT = 20
DEFAULT_SLEEP_RANGE = (1.5, 3.5)


@dataclass(frozen=True)
class CategorySeed:
    """One category/listing entry point to crawl."""

    name: str
    start_url: str
    pagination_template: Optional[str] = None
    max_pages: int = 3


@dataclass(frozen=True)
class SiteConfig:
    """Configuration for one non-CNA general news site."""

    source_site: str
    allowed_domain: str
    country: str
    language: str
    categories: list[CategorySeed]


# ---------------------------------------------------------------------------
# Replace this placeholder config with ONE real site before real crawling.
# Example ideas for a general news site:
# - politics category page
# - society/local category page
# - international/world category page
#
# The point of this alt skeleton is to crawl category pages rather than a
# single CNA-like pattern.
# ---------------------------------------------------------------------------
TARGET_SITE = SiteConfig(
    source_site="replace_me_general_news",
    allowed_domain="example.com",
    country="Taiwan",
    language="zh",
    categories=[
        CategorySeed(
            name="politics",
            start_url="https://example.com/category/politics",
            pagination_template="https://example.com/category/politics?page={page}",
            max_pages=3,
        ),
        CategorySeed(
            name="society",
            start_url="https://example.com/category/society",
            pagination_template="https://example.com/category/society?page={page}",
            max_pages=3,
        ),
    ],
)


def build_session() -> requests.Session:
    """Create a polite requests session with retry behavior."""
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
        }
    )
    return session


def polite_sleep() -> None:
    time.sleep(random.uniform(*DEFAULT_SLEEP_RANGE))


def fetch_html(session: requests.Session, url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def normalize_text(text: Optional[str]) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def normalize_datetime(raw_text: str) -> str:
    """Best-effort normalization for common timestamp formats."""
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
            return datetime.strptime(raw_text, fmt).isoformat()
        except ValueError:
            continue

    # Placeholder for site-specific localized formats, for example:
    # 2026年03月10日 09:15
    # 03/10 09:15
    return ""


def is_allowed_article_url(url: str, config: SiteConfig) -> bool:
    """Basic domain guard to reduce accidental off-site links."""
    if not url:
        return False
    hostname = (urlparse(url).hostname or "").lower()
    return hostname == config.allowed_domain or hostname.endswith(f".{config.allowed_domain}")



def iter_category_page_urls(seed: CategorySeed) -> Iterator[str]:
    """Yield list-page URLs for one category.

    Current simple behavior:
    - emit the category start_url
    - if a pagination template exists, expand page 2..max_pages

    Replace this if the site uses:
    - next-page links embedded in HTML
    - query cursors
    - infinite scroll / AJAX endpoints
    """
    yielded = set()

    if seed.start_url not in yielded:
        yielded.add(seed.start_url)
        yield seed.start_url

    if seed.pagination_template:
        for page in range(2, seed.max_pages + 1):
            url = seed.pagination_template.format(page=page)
            if url not in yielded:
                yielded.add(url)
                yield url



def extract_articles_from_category(
    html: str,
    page_url: str,
    category_name: str,
    category_url: str,
    config: SiteConfig,
) -> list[dict[str, str]]:
    """Extract article teaser rows from a general-news category page.

    This is the main site-specific placeholder.

    Typical structure on non-CNA general news sites:
    - cards/teasers on category pages
    - title anchor inside h2/h3 or dedicated class
    - optional summary text
    - optional time element or small metadata row

    After inspecting the target site, update:
    1. candidate block selector
    2. title link selector
    3. summary selector
    4. time selector
    5. any filtering rules for non-article links
    """
    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict[str, str]] = []

    # -----------------------------------------------------------------------
    # Placeholder selectors to replace after inspecting one real site.
    # Common candidates:
    # - "article"
    # - ".news-list-item"
    # - ".story-card"
    # - ".category-page .item"
    # - "li.newsItem"
    #
    # If the page mixes article cards with ads or videos, add filtering rules.
    # -----------------------------------------------------------------------
    candidate_items = soup.select("article, .news-item, .story-card, li")

    for item in candidate_items:
        title_link = item.select_one("h1 a, h2 a, h3 a, .title a, a.title, a")
        if not title_link:
            continue

        title = normalize_text(title_link.get_text(" ", strip=True))
        href = normalize_text(title_link.get("href"))
        article_url = urljoin(page_url, href) if href else ""

        if not title or not article_url:
            continue
        if not is_allowed_article_url(article_url, config):
            continue

        # Optional summary / short description shown on list pages.
        summary_node = item.select_one("p, .summary, .desc, .brief, .intro")
        summary = normalize_text(summary_node.get_text(" ", strip=True) if summary_node else "")

        # Optional list-page timestamp.
        time_node = item.select_one("time, .date, .time, .publish-time, .meta time")
        published_at_raw = ""
        if time_node:
            published_at_raw = normalize_text(
                time_node.get("datetime") if time_node.get("datetime") else time_node.get_text(" ", strip=True)
            )
        published_at_iso = normalize_datetime(published_at_raw)

        # Optional filtering ideas after you know the site structure:
        # - skip URLs containing /video/ or /tag/
        # - skip cards whose title is too short or looks like "更多"
        # - skip duplicate promo modules

        rows.append(
            {
                "source_site": config.source_site,
                "category": category_name,
                "category_url": category_url,
                "list_page_url": page_url,
                "article_url": article_url,
                "title": title,
                "summary": summary,
                "published_at_raw": published_at_raw,
                "published_at_iso": published_at_iso,
                "crawl_time_iso": datetime.now(timezone.utc).isoformat(),
                "language": config.language,
                "country": config.country,
                "collector_version": COLLECTOR_VERSION,
                "notes": "alt first-pass category-page extraction",
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

    for category in config.categories:
        print(f"Category: {category.name}")
        for idx, page_url in enumerate(iter_category_page_urls(category), start=1):
            print(f"  [{idx}] Fetching: {page_url}")
            try:
                html = fetch_html(session, page_url)
                rows = extract_articles_from_category(
                    html=html,
                    page_url=page_url,
                    category_name=category.name,
                    category_url=category.start_url,
                    config=config,
                )
                print(f"      Extracted rows: {len(rows)}")
                all_rows.extend(rows)
            except requests.RequestException as exc:
                print(f"      Request failed: {exc}", file=sys.stderr)
            except Exception as exc:
                print(f"      Parse failed: {exc}", file=sys.stderr)

            polite_sleep()

    unique_rows = deduplicate_rows(all_rows)
    save_csv(unique_rows, output_path)
    return unique_rows



def main() -> int:
    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / ".." / "data" / f"{TARGET_SITE.source_site}_titles_alt_first_pass.csv"
    output_path = output_path.resolve()

    print("Starting alternative news-title collection skeleton...")
    print(f"Target site: {TARGET_SITE.source_site}")
    print(f"Output CSV: {output_path}")
    print()

    if TARGET_SITE.source_site == "replace_me_general_news":
        print(
            "WARNING: TARGET_SITE is still placeholder-only. "
            "Update config and selectors before actual crawling.",
            file=sys.stderr,
        )

    rows = crawl_site(TARGET_SITE, output_path)
    print()
    print(f"Done. Saved {len(rows)} unique rows.")
    print("Next step: inspect one real category page and refine selectors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
