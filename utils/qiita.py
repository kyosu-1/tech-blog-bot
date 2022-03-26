from typing import List, Dict, Set, Any

import requests


def fetch_qiita_trend_items() -> List[Dict[str, Any]]:
    """use unofficial api"""
    url = "https://qiita-api.vercel.app/api/trend"
    res = requests.get(url=url)
    return res.json()


def sort_qiita_items_by_like(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """sort items by like count

    Args:
        items (List[Dict[str, Any]]): qiita items

    Returns:
        List[Dict[str, Any]]: sorted items
    """
    sorted_items = sorted(items, key=lambda x: x["node"]["likesCount"], reverse=True)
    return sorted_items


def tag_name_exists(
    tags: List[Dict[str, str]],
    want_tag_set: Set[str]
) -> bool:
    """Determines whether a tag name exists

    Args:
        tags (List[Dict[str, str]]): List of tags attached to an article
        want_tag_set (Set[str]): Set of required tags

    Returns:
        bool:
    """
    for tag in tags:
        if tag['name'] in want_tag_set:
            return True
    return False


def get_trend_items(
    want_tags: List[str],
    get_num: int
) -> List[Dict[str, str]]:
    """Get tread items
    Obtain only the number of items specified by get_num want_tags.
    Priority is given to articles with tags in want tags and articles with a high number of likes.

    Args:
        want_tags (List[str]): List of required tags
        get_num (int): Number of Acquisitions

    Returns:
        List[Dict[str, str]]: List of article titles and url
    """
    qiita_trend_items = fetch_qiita_trend_items()
    want_tag_set = set(want_tags)
    want_items = list(
        filter(
            lambda x: tag_name_exists(x["node"]["tags"], want_tag_set), qiita_trend_items
        )
    )
    sorted_want_items = sort_qiita_items_by_like(want_items)
    if len(sorted_want_items) >= get_num:
        return [
            {
                'title': item['node']['title'],
                'url': item['node']['linkUrl']
            } for item in sorted_want_items[:get_num]
        ]
    sorted_items = sort_qiita_items_by_like(qiita_trend_items)
    res_items = []
    unique_id_set = set()
    for item in sorted_want_items:
        res_items.append(
            {
                'title': item['node']['title'],
                'url': item['node']['linkUrl']
            }
        )
        unique_id_set.add(item['node']['uuid'])
    for item in sorted_items:
        if len(res_items) == get_num:
            break
        if item['node']['uuid'] in unique_id_set:
            continue
        res_items.append(
            {
                'title': item['node']['title'],
                'url': item['node']['linkUrl']
            }
        )
    return res_items


def make_text_from_trend_items(items: List[Dict[str, str]]) -> str:
    text = ''
    for item in items:
        text += f"タイトル: {item['title']}\n"
        text += f"url: {item['url']} \n\n"
    return text
