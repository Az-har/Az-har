"""Generate a reliable, self-hosted GitHub contribution streak SVG card."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Tuple


DEFAULT_USERNAME = "Az-har"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "streak.svg"
USER_AGENT = "Az-har-Streak-Generator/1.0"


def _fetch_via_graphql(username: str, token: str) -> Tuple[date, int, Dict[str, int]]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }

    meta_query = """
    query($login: String!) {
      user(login: $login) {
        createdAt
      }
    }
    """
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": meta_query, "variables": {"login": username}}).encode("utf-8"),
        headers=headers,
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        meta_res = json.loads(resp.read().decode("utf-8"))

    if "errors" in meta_res or not meta_res.get("data", {}).get("user"):
        raise RuntimeError(f"GraphQL metadata error: {meta_res}")

    created_str = meta_res["data"]["user"]["createdAt"][:10]
    created_date = date.fromisoformat(created_str)
    cur_year = datetime.now(timezone.utc).year

    days: Dict[str, int] = {}
    total_contributions = 0

    for year in range(created_date.year, cur_year + 1):
        year_query = """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            contributionsCollection(from: $from, to: $to) {
              contributionCalendar {
                totalContributions
                weeks {
                  contributionDays {
                    date
                    contributionCount
                  }
                }
              }
            }
          }
        }
        """
        variables = {
            "login": username,
            "from": f"{year}-01-01T00:00:00Z",
            "to": f"{year}-12-31T23:59:59Z",
        }
        y_req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": year_query, "variables": variables}).encode("utf-8"),
            headers=headers,
        )
        with urllib.request.urlopen(y_req, timeout=20) as y_resp:
            y_res = json.loads(y_resp.read().decode("utf-8"))

        if "errors" in y_res:
            raise RuntimeError(f"GraphQL year {year} error: {y_res}")

        cal = y_res["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        total_contributions += int(cal["totalContributions"])
        for week in cal["weeks"]:
            for day in week["contributionDays"]:
                d_str = day["date"]
                cnt = int(day["contributionCount"])
                # Merge cleanly if GitHub returns overlapping boundary dates
                days[d_str] = max(days.get(d_str, 0), cnt)

    return created_date, total_contributions, days


def _fetch_via_html(username: str) -> Tuple[date, int, Dict[str, int]]:
    headers = {"User-Agent": "Mozilla/5.0"}

    # Determine account join year from profile page or fallback to 2019
    created_year = 2019
    created_date = date(2019, 9, 23)
    try:
        profile_req = urllib.request.Request(f"https://api.github.com/users/{username}", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(profile_req, timeout=15) as pr:
            pdata = json.loads(pr.read().decode("utf-8"))
            if pdata.get("created_at"):
                created_date = date.fromisoformat(pdata["created_at"][:10])
                created_year = created_date.year
    except Exception:
        pass

    cur_year = datetime.now(timezone.utc).year
    days: Dict[str, int] = {}
    total_contributions = 0

    for year in range(created_year, cur_year + 1):
        url = f"https://github.com/users/{username}/contributions?from={year}-01-01&to={year}-12-31"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        m = re.search(rf"([\d,]+)\s+contributions?\s+in\s+{year}", html)
        if m:
            total_contributions += int(m.group(1).replace(",", ""))

        for d_str, lvl in re.findall(r'data-date="([^"]+)"[^>]*data-level="([^"]+)"', html):
            active = 1 if lvl != "0" else 0
            days[d_str] = max(days.get(d_str, 0), active)

    return created_date, total_contributions, days


def fetch_contributions(username: str) -> Tuple[date, int, Dict[str, int]]:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        try:
            return _fetch_via_graphql(username, token)
        except Exception as exc:
            print(f"GraphQL fetch fell back to public calendar HTML ({exc})")
    return _fetch_via_html(username)


def compute_streaks(days: Dict[str, int], today: date) -> Tuple[int, date | None, date | None, int, date | None, date | None]:
    today_iso = today.isoformat()
    all_dates = sorted(d for d in days.keys() if d <= today_iso)

    longest = 0
    longest_start: date | None = None
    longest_end: date | None = None
    run = 0
    run_start: date | None = None

    for d_str in all_dates:
        if days[d_str] > 0:
            d_obj = date.fromisoformat(d_str)
            if run == 0:
                run_start = d_obj
            run += 1
            if run >= longest:
                longest = run
                longest_start = run_start
                longest_end = d_obj
        else:
            run = 0
            run_start = None

    # Current streak: ends today if active today, otherwise yesterday if active yesterday
    check_day = today
    if days.get(check_day.isoformat(), 0) == 0:
        yesterday = today - timedelta(days=1)
        if days.get(yesterday.isoformat(), 0) > 0:
            check_day = yesterday

    current = 0
    curr_start: date | None = None
    curr_end: date | None = None
    if days.get(check_day.isoformat(), 0) > 0:
        curr_end = check_day
        while days.get(check_day.isoformat(), 0) > 0:
            curr_start = check_day
            current += 1
            check_day -= timedelta(days=1)

    return current, curr_start, curr_end, longest, longest_start, longest_end


def format_range(start: date | None, end: date | None, ref_year: int, empty_text: str = "No active streak") -> str:
    if start is None or end is None:
        return empty_text
    if start == end:
        return f"{start.strftime('%b')} {start.day}, {start.year}"
    if start.year == end.year == ref_year:
        return f"{start.strftime('%b')} {start.day} - {end.strftime('%b')} {end.day}"
    if start.year == end.year:
        return f"{start.strftime('%b')} {start.day} - {end.strftime('%b')} {end.day}, {end.year}"
    return f"{start.strftime('%b')} {start.day}, {start.year} - {end.strftime('%b')} {end.day}, {end.year}"


def render_svg(
    total: int,
    created_date: date,
    current: int,
    curr_start: date | None,
    curr_end: date | None,
    longest: int,
    longest_start: date | None,
    longest_end: date | None,
    ref_year: int,
) -> str:
    total_range = f"{created_date.strftime('%b')} {created_date.day}, {created_date.year} - Present"
    curr_range = format_range(curr_start, curr_end, ref_year)
    longest_range = format_range(longest_start, longest_end, ref_year, empty_text="—")
    ring_color = "#70A5FD" if current > 0 else "#414868"
    flame_color = "#FF9E64" if current > 0 else "#565F89"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 195" width="495" height="195" role="img" aria-label="GitHub Contribution Streak: {total} total, {current} current streak, {longest} longest streak">
  <defs>
    <mask id="ring-cutout">
      <rect width="495" height="195" fill="#ffffff"/>
      <ellipse cx="247.5" cy="31" rx="13" ry="16" fill="#000000"/>
    </mask>
  </defs>

  <rect x="0.5" y="0.5" width="494" height="194" rx="8" fill="#1A1B27" stroke="#30363D" stroke-width="1"/>

  <line x1="165" y1="28" x2="165" y2="167" stroke="#2F3549" stroke-width="1"/>
  <line x1="330" y1="28" x2="330" y2="167" stroke="#2F3549" stroke-width="1"/>

  <!-- Column 1: Total Contributions -->
  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" text-anchor="middle">
    <text x="82.5" y="82" fill="#70A5FD" font-size="28" font-weight="700">{total:,}</text>
    <text x="82.5" y="114" fill="#C0CAF5" font-size="13.5" font-weight="500">Total Contributions</text>
    <text x="82.5" y="138" fill="#38BDAE" font-size="11.5" font-weight="400">{total_range}</text>
  </g>

  <!-- Column 2: Current Streak -->
  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" text-anchor="middle">
    <circle cx="247.5" cy="70" r="38" fill="none" stroke="{ring_color}" stroke-width="4.5" mask="url(#ring-cutout)"/>
    <g transform="translate(247.5, 19)">
      <path d="M1.5 0.67 C1.5 0.67 2.24 3.32 2.24 5.47 C2.24 7.53 0.89 9.2 -1.17 9.2 C-3.23 9.2 -4.79 7.53 -4.79 5.47 L-4.76 5.11 C-6.78 7.51 -8 10.62 -8 14 C-8 18.42 -4.42 22 0 22 C4.42 22 8 18.42 8 14 C8 8.61 5.41 3.8 1.5 0.67 Z M-0.29 19 C-2.07 19 -3.51 17.6 -3.51 15.86 C-3.51 14.24 -2.46 13.1 -0.7 12.74 C1.07 12.38 2.9 11.53 3.92 10.16 C4.31 11.45 4.51 12.81 4.51 14.2 C4.51 16.85 2.36 19 -0.29 19 Z" fill="{flame_color}"/>
    </g>
    <text x="247.5" y="80" fill="#FFFFFF" font-size="28" font-weight="700">{current}</text>
    <text x="247.5" y="131" fill="#BF91F3" font-size="13.5" font-weight="600">Current Streak</text>
    <text x="247.5" y="153" fill="#38BDAE" font-size="11.5" font-weight="400">{curr_range}</text>
  </g>

  <!-- Column 3: Longest Streak -->
  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" text-anchor="middle">
    <text x="412.5" y="82" fill="#70A5FD" font-size="28" font-weight="700">{longest}</text>
    <text x="412.5" y="114" fill="#C0CAF5" font-size="13.5" font-weight="500">Longest Streak</text>
    <text x="412.5" y="138" fill="#38BDAE" font-size="11.5" font-weight="400">{longest_range}</text>
  </g>
</svg>
"""


def main() -> None:
    username = os.environ.get("GH_USERNAME", DEFAULT_USERNAME).strip() or DEFAULT_USERNAME
    created_date, total, days = fetch_contributions(username)

    # Check both UTC and IST so active same-day commits in IST are never missed
    utc_today = datetime.now(timezone.utc).date()
    ist_today = datetime.now(timezone(timedelta(hours=5, minutes=30))).date()
    today = ist_today if days.get(ist_today.isoformat(), 0) > 0 else utc_today

    current, curr_start, curr_end, longest, longest_start, longest_end = compute_streaks(days, today)
    svg = render_svg(
        total=total,
        created_date=created_date,
        current=current,
        curr_start=curr_start,
        curr_end=curr_end,
        longest=longest,
        longest_start=longest_start,
        longest_end=longest_end,
        ref_year=today.year,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"Updated {OUTPUT_PATH} | total={total}, current={current} ({curr_start}..{curr_end}), longest={longest} ({longest_start}..{longest_end})")


if __name__ == "__main__":
    main()
