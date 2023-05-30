from argparse import ArgumentParser
import json
import jmespath


def get_videos(json_obj: dict | list | None) -> list[str]:
    # TODO: Get also cross-post video items
    jpath = "data.children[?data.is_video == `true`].data.url_overridden_by_dest"
    urls_list = jmespath.search(jpath, json_obj)
    return urls_list


if __name__ == "__main__":
    p = ArgumentParser()
    # breakpoint()
    default_json = "{}"
    p.add_argument("--json", default=default_json, required=False, type=str)
    namespace = p.parse_known_args()[0]
    json_data = json.loads(namespace.json)
    print(get_videos(json_data))
