import yt_dlp
import os

url = input("Paste YouTube URL: ")
#Enter your pathname for download it to your computer
download_path = "/Users/bahadirkilic/Documents/python100/Youtube_Video_Downloader/DownloadedVideos"


try:
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save to your chosen path
        'quiet': True,  # No unnecessary output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("✅ Done! Check your folder.")

except Exception as e:
    print(f"❌ Error: {e}")