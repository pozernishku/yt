from argparse import ArgumentParser

import youtube_dl

from reddit import Reddit

if __name__ == "__main__":
    p = ArgumentParser()
    default_url = "https://www.reddit.com/r/TikTokCringe/hot.json?limit=30"
    p.add_argument("--url", default=default_url, required=False, type=str)
    namespace, _ = p.parse_known_args()
    reddit = Reddit(namespace.url)
    if not reddit.video_urls:
        raise Exception("No videos found")

    ydl_opts = {"outtmpl": "%(epoch)s-%(title)s-%(id)s.%(ext)s"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(reddit.video_urls)
