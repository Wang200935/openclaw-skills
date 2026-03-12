---
name: weather
description: "Get current weather and forecasts via wttr.in or Open-Meteo. Use when: user asks about weather, temperature, or forecasts for any location. NOT for: historical weather data, severe weather alerts, or detailed meteorological analysis. No API key needed."
homepage: https://wttr.in/:help
metadata: { "openclaw": { "emoji": "?尋锔?, "requires": { "bins": ["curl"] } } }
---

# Weather Skill

Get current weather conditions and forecasts.

## When to Use

??**USE this skill when:**

- "What's the weather?"
- "Will it rain today/tomorrow?"
- "Temperature in [city]"
- "Weather forecast for the week"
- Travel planning weather checks

## When NOT to Use

??**DON'T use this skill when:**

- Historical weather data ??use weather archives/APIs
- Climate analysis or trends ??use specialized data sources
- Hyper-local microclimate data ??use local sensors
- Severe weather alerts ??check official NWS sources
- Aviation/marine weather ??use specialized services (METAR, etc.)

## Location

Always include a city, region, or airport code in weather queries.

## Commands

### Current Weather

```bash
# One-line summary
curl "wttr.in/London?format=3"

# Detailed current conditions
curl "wttr.in/London?0"

# Specific city
curl "wttr.in/New+York?format=3"
```

### Forecasts

```bash
# 3-day forecast
curl "wttr.in/London"

# Week forecast
curl "wttr.in/London?format=v2"

# Specific day (0=today, 1=tomorrow, 2=day after)
curl "wttr.in/London?1"
```

### Format Options

```bash
# One-liner
curl "wttr.in/London?format=%l:+%c+%t+%w"

# JSON output
curl "wttr.in/London?format=j1"

# PNG image
curl "wttr.in/London.png"
```

### Format Codes

- `%c` ??Weather condition emoji
- `%t` ??Temperature
- `%f` ??"Feels like"
- `%w` ??Wind
- `%h` ??Humidity
- `%p` ??Precipitation
- `%l` ??Location

## Quick Responses

**"What's the weather?"**

```bash
curl -s "wttr.in/London?format=%l:+%c+%t+(feels+like+%f),+%w+wind,+%h+humidity"
```

**"Will it rain?"**

```bash
curl -s "wttr.in/London?format=%l:+%c+%p"
```

**"Weekend forecast"**

```bash
curl "wttr.in/London?format=v2"
```

## Notes

- No API key needed (uses wttr.in)
- Rate limited; don't spam requests
- Works for most global cities
- Supports airport codes: `curl wttr.in/ORD`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\misc\weather\SKILL.md
---
---
name: weather
description: Get current weather and forecasts (no API key required).
homepage: https://wttr.in/:help
metadata: {"clawdbot":{"emoji":"?尋锔?,"requires":{"bins":["curl"]}}}
---

# Weather

Two free services, no API keys needed.

## wttr.in (primary)

Quick one-liner:
```bash
curl -s "wttr.in/London?format=3"
# Output: London: ?咃? +8掳C
```

Compact format:
```bash
curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
# Output: London: ?咃? +8掳C 71% ??km/h
```

Full forecast:
```bash
curl -s "wttr.in/London?T"
```

Format codes: `%c` condition 路 `%t` temp 路 `%h` humidity 路 `%w` wind 路 `%l` location 路 `%m` moon

Tips:
- URL-encode spaces: `wttr.in/New+York`
- Airport codes: `wttr.in/JFK`
- Units: `?m` (metric) `?u` (USCS)
- Today only: `?1` 路 Current only: `?0`
- PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`

## Open-Meteo (fallback, JSON)

Free, no key, good for programmatic use:
```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```

Find coordinates for a city, then query. Returns JSON with temp, windspeed, weathercode.

Docs: https://open-meteo.com/en/docs


