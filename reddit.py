from dataclasses import dataclass


@dataclass
class Reddit:
    url: str
    user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"


if __name__ == "__main__":
    r = Reddit("https://www.reddit.com/r/TikTokCringe/hot.json?limit=2")
    print(r)
