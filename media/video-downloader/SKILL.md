---
name: video-downloader
description: Download videos, playlists, and streams from major platforms (YouTube, Twitter/X, TikTok, Bilibili, Instagram, etc.) using yt-dlp/youtube-dl/gallery-dl/streamlink with aria2 and ffmpeg. Use when you need to fetch a video file locally, archive it, extract audio, or troubleshoot download errors.
---

# Video Downloader Skill

Use this skill to download and archive videos, playlists, or live streams. Default to **yt-dlp**. Fall back to **youtube-dl**, **gallery-dl**, or **streamlink** when needed. Use **ffmpeg** for remux/convert, and **aria2c** for faster parallel downloads.

## Auto-select script

```powershell
# Auto choose downloader by URL
# Examples:
# .\scripts\auto_download.ps1 -Url "<URL>"
# .\scripts\auto_download.ps1 -Url "<URL>" -OutDir "C:\\Users\\wang\\.openclaw\\media\\videos" -CookiesFromChrome
```

```powershell
# Single video (best quality, merge A/V)
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o "%(title)s.%(ext)s" "<URL>"

# Save into a folder
yt-dlp -P "C:\Users\wang\.openclaw\media\videos" -f "bv*+ba/b" --merge-output-format mp4 "<URL>"

# Playlist
yt-dlp --yes-playlist -o "%(playlist_title)s/%(playlist_index)03d-%(title)s.%(ext)s" "<URL>"
```

## Faster downloads (aria2c)

```powershell
yt-dlp --downloader aria2c --downloader-args "aria2c:-x16 -s16 -k1M" -f "bv*+ba/b" --merge-output-format mp4 "<URL>"
```

## Fallback tools

### youtube-dl (legacy fallback)
```powershell
youtube-dl -f "bestvideo+bestaudio/best" "<URL>"
```

### gallery-dl (image/video-heavy sites, albums)
```powershell
gallery-dl "<URL>"
```

### streamlink (live streams)
```powershell
streamlink "<URL>" best -o output.mp4
```

## Additional tools

### lux
```powershell
lux "<URL>"
```

### you-get
```powershell
you-get "<URL>"
```


- **403/Sign-in required**: use cookies
 ```powershell
 yt-dlp --cookies-from-browser chrome "<URL>"
 ```
- **Throttled**: add `--concurrent-fragments8` and/or aria2c.
- **Geo-block**: use VPN then retry.
- **Missing ffmpeg**: install ffmpeg or set `--merge-output-format mp4`.

## When to prefer which tool

- **Default**: yt-dlp
- **Legacy compatibility**: youtube-dl
- **Image/video galleries**: gallery-dl
- **Live streams**: streamlink
- **China platforms / misc**: lux, you-get
