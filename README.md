# tech-blog-bot

Post popular qiita articles to slack

## setting

qiita.jsonにて以下のようなjsonファイルを作成する。

```json=
{
    "tag_list": [
        "Python",
        "AWS",
        "Linux",
        "Docker",
        "機械学習",
        "データサイエンス",
        "競技プログラミング"
    ],
    "tread_get_num": 5
}
```

`tag_list`: 取得したい記事のtagのリスト
`tread_get_num`: いくつの記事を投稿するか(最大30)

## usage

```bash=
python3 main.py
```
