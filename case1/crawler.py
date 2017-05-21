# coding: utf-8

import requests
from bs4 import BeautifulSoup


URL_BASE = "https://ja.wikipedia.org"
WORSHIP_JUDGE_LIST = ["社", "宮", "荷"]


def parse_worship_page(link):
    url = URL_BASE + link
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        table = soup.find("table", {"class": "infobox"})
        base_title = table.find("tr").find("th")
        decision_char = base_title.text[-1].encode('utf-8')
        if decision_char not in WORSHIP_JUDGE_LIST:
            raise
        title = base_title.text.encode('utf-8')

        rows = table.find_all("tr")
        for row in rows:
            if not row.find("th"):
                continue
            th_text = row.find("th").text.encode('utf-8')
            if th_text == "所在地":
                place = row.find("td").text.encode('utf-8')
            if th_text == "位置":
                location = row.find("span", {"class": "plainlinks"}).text.encode('utf-8').replace('\n', '')

        info = {}
        info["title"] = title
        info["place"] = place
        info["location"] = location
    except:
        raise

    return info


def main():
    # get base url
    url = URL_BASE + "/wiki/神社一覧"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    # parse worship list
    content = soup.find("div", {"id": "mw-content-text"})
    worship_list = content.find_all("a")

    # parse worship link
    worship_dic = {}
    for worship in worship_list:
        if not worship.text:
            continue
        worship_name = worship.text.encode('utf-8')
        worship_dic[worship_name] = {}
        try:
            worship_dic[worship_name]["link"] = worship.get("href").encode('utf-8')
        except:
            continue

    # parse indivisual worship page
    for worship in worship_dic:
        try:
            worship_info = parse_worship_page(worship_dic[worship]["link"])
            print worship_info["title"], worship_info["place"], worship_info["location"]
        except:
            continue


if __name__ == '__main__':
    main()
