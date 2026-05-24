import yt_dlp
import os

VIDEO_URL = "https://www.youtube.com/watch?v=AYHEI67x-kI"
DOWNLOAD_DIR = "youtube_videos"


def download_video(url):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    ydl_opts = {
        "format": "bestvideo[vcodec*=avc1][height<=1080]+bestaudio[ext=m4a]",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Видео скачано")


def main():
    download_video(VIDEO_URL)


if __name__ == "__main__":
    main()
