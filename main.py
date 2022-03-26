import os
import json
import traceback

from dotenv import load_dotenv

from utils.slack import post_slack_by_webhook
from utils.qiita import get_trend_items, make_text_from_trend_items


load_dotenv()


def main(webhook_url: str):
    try:
        json_open = open('qiita.json', 'r')
        json_load = json.load(json_open)
        trend_items = get_trend_items(json_load['tag_list'], json_load['tread_get_num'])
        text = make_text_from_trend_items(trend_items)
        post_slack_by_webhook(webhook_url, text)
    except Exception as e:
        text = f"[{e}]{traceback.format_exc()}"
        post_slack_by_webhook(webhook_url, text)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--webhook_url', type=str, required=True)
    args = parser.parse_args()

    main(args.webhook_url)
