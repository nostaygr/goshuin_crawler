# goshuin_crawler
goshuinプロジェクトのための寺社仏閣クローラー管理リポジトリ

## case1
- ベースページ: [神社一覧 -wikipedia-](https://ja.wikipedia.org/wiki/%E7%A5%9E%E7%A4%BE%E4%B8%80%E8%A6%A7)
- 末尾が"社", "宮", "荷"のリンクを神社とみなし、それぞれのページをクロール
- 各ページでは、info_boxをもとに、住所と緯度経度を取得

## case2
- ベースページ: [日本の寺院一覧 -wikipedia-](https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%AF%BA%E9%99%A2%E4%B8%80%E8%A6%A7)
- 末尾が"寺", "院", "師"のリンクを寺とみなし、それぞれのページをクロール
- 各ページでは、info_boxをもとに、住所と緯度経度を取得
- とりあえず以下のように出力
