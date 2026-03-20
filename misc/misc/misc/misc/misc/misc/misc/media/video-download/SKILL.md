---
name: video-download
description: "Download videos (and audio) from most major platforms using yt-dlp. Use when the user provides a video URL and wants it downloaded, converted to audio, or needs a safe command template for cross-platform (Windows/macOS/Linux) downloading. Covers YouTube, Twitter/X, TikTok, Instagram, Facebook, Bilibili, Vimeo, Twitch, Reddit, and more via yt-dlp."
---

# Video Download (yt-dlp)

## Workflow

1. **Confirm intent & legality**
 - Ask the user to confirm they have rights/permission to download the content.
 - Proceed only after confirmation.

2. **Normalize inputs**
 - Collect the URL(s).
 - Optional: ask for preferred output format (mp4/mkv/webm) and quality (best,1080p,720p, etc.).

3. **Choose command template**
 - Use the cross-platform templates in `references/commands.md`.
 - If user wants audio only, use the audio template.

4. **Run download**
 - Prefer `yt-dlp` with safe flags.
 - For playlists, use the playlist template.

5. **Deliver output**
 - If the user wants files sent, attach them through the platform.

## Notes

- yt-dlp supports a very large set of sites; don’t claim “all platforms.”
- When a site blocks downloads, suggest updating yt-dlp or using cookies (only if the user can provide them).
