import json
from argparse import ArgumentParser

import jmespath


def get_videos(json_obj: dict | list | None) -> list[str] | None:
    # TODO: Get also cross-post video items
    jpath = "data.children[?data.is_video == `true`].data.url_overridden_by_dest"
    urls_list = jmespath.search(jpath, json_obj)
    return urls_list


if __name__ == "__main__":
    p = ArgumentParser()
    default_json = "{}"
    p.add_argument("--json", default=default_json, required=False, type=str)
    namespace = p.parse_known_args()[0]
    json_data = json.loads(namespace.json)
    videos = get_videos(json_data)
    if not videos:
        raise Exception("No videos found")
    for v in videos:
        print(v)
