# yt-dlp Command Templates

> Use these as starting points. Adjust paths for Windows/macOS/Linux.

##1) Basic (best quality)

```bash
yt-dlp -o "%(title)s.%(ext)s" "<URL>"
```

##2) MP4 (best mp4 up to1080p)

```bash
yt-dlp -f "bv*[ext=mp4][height<=1080]+ba[ext=m4a]/b[ext=mp4]" -o "%(title)s.%(ext)s" "<URL>"
```

##3) Audio-only (mp3)

```bash
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "<URL>"
```

##4) Playlist (download all)

```bash
yt-dlp -o "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" "<URL>"
```

##5) Windows paths example

```powershell
yt-dlp -o "C:\\Downloads\\%(title)s.%(ext)s" "<URL>"
```

##6) macOS/Linux paths example

```bash
yt-dlp -o "$HOME/Downloads/%(title)s.%(ext)s" "<URL>"
```

##7) Cookies (if needed)

```bash
yt-dlp --cookies-from-browser chrome -o "%(title)s.%(ext)s" "<URL>"
```

##8) Update yt-dlp

```bash
yt-dlp -U
```
