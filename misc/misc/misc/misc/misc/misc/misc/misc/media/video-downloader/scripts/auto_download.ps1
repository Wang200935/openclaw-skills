param(
 [Parameter(Mandatory=$true)][string]$Url,
 [string]$OutDir = "C:\Users\wang\.openclaw\media\videos",
 [switch]$Best,
 [switch]$CookiesFromChrome
)

# Auto-select downloader by URL
$u = $Url.ToLower()

# Ensure output directory
if (!(Test-Path $OutDir)) { New-Item -ItemType Directory -Force -Path $OutDir | Out-Null }

function Use-YtDlp {
 param([string]$Url,[string]$OutDir,[switch]$CookiesFromChrome)
 $cookieArg = ""
 if ($CookiesFromChrome) { $cookieArg = "--cookies-from-browser chrome" }
 & python -m yt_dlp -P $OutDir -f "bv*+ba/b" --merge-output-format mp4 $cookieArg $Url
}

function Use-Lux {
 param([string]$Url,[string]$OutDir)
 Push-Location $OutDir
 & lux $Url
 Pop-Location
}

function Use-YouGet {
 param([string]$Url,[string]$OutDir)
 Push-Location $OutDir
 & you-get $Url
 Pop-Location
}

function Use-Streamlink {
 param([string]$Url,[string]$OutDir)
 $out = Join-Path $OutDir "stream_output.mp4"
 & streamlink $Url best -o $out
}

# Rules
if ($u -match "bilibili|b23.tv|douyin|kuaishou|xigua") {
 Use-Lux -Url $Url -OutDir $OutDir
} elseif ($u -match "tiktok|instagram|twitter|x.com|facebook|youtube|youtu.be|vimeo") {
 Use-YtDlp -Url $Url -OutDir $OutDir -CookiesFromChrome:$CookiesFromChrome
} elseif ($u -match "m3u8|live|twitch|kick|huya|douyu") {
 Use-Streamlink -Url $Url -OutDir $OutDir
} else {
 # fallback to yt-dlp then you-get
 try { Use-YtDlp -Url $Url -OutDir $OutDir -CookiesFromChrome:$CookiesFromChrome }
 catch { Use-YouGet -Url $Url -OutDir $OutDir }
}
