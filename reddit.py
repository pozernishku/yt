import json
from dataclasses import dataclass, field
from typing import Any

import jmespath
import requests


@dataclass
class Reddit:
    url: str
    user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
    json_data: Any = field(init=False)
    video_urls: list[str] | None = field(init=False)

    def __post_init__(self):
        self.json_data = json.loads(
            requests.request(
                method="GET",
                url=self.url,
                headers={"user-agent": self.user_agent},
            ).content
        )
        self.video_urls = self.get_video_urls()

    def get_video_urls(self) -> list[str] | None:
        # TODO: Get also cross-post video items
        jpath = "data.children[?data.is_video == `true`].data.url_overridden_by_dest"
        video_urls = jmespath.search(jpath, self.json_data)
        return video_urls
