# coding: utf-8

import sys
import requests
from bs4 import BeautifulSoup
sys.path.append("lib")
import api


URL_BASE = "https://ja.wikipedia.org"
WORSHIP_JUDGE_LIST = ["社", "宮", "荷"]
IS_TEMPLE = "0"


# wikipediaのinfobox欄をparse
def parse_worship_page(link):
    url = URL_BASE + link
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        table = soup.find("table", {"class": "infobox"})
        base_title = table.find("tr").find("th")
    except:
        print "can't find infobox"
        raise
    decision_char = base_title.text[-1].encode('utf-8')
    if decision_char not in WORSHIP_JUDGE_LIST:
        print "this is not worship page"
        raise

    title = base_title.text.encode('utf-8')
    rows = table.find_all("tr")
    for row in rows:
        if not row.find("th"):
            continue
        th_text = row.find("th").text.encode('utf-8')
        if th_text == "所在地":
            address = row.find("td").text.encode('utf-8').replace('\n', '')
        if th_text == "主祭神":
            obj = row.find("td").text.encode('utf-8').replace('\n', ',')

    try:
        address
    except:
        address = ""

    try:
        obj
    except:
        obj = ""

    try:
        lat, lng = api.convert_address_to_latlng(address)
    except:
        lat = lng = 0

    info = {}
    info["title"] = title
    info["address"] = address
    info["lat"] = str(lat)
    info["lng"] = str(lng)
    info["rank"] = ""
    info["obj"] = obj

    return info


def main():
    # get base url
    url = URL_BASE + "/wiki/神社一覧"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    # parse worship list
    content = soup.find("div", {"id": "mw-content-text"})
    a_tag_list = content.find_all("a")

    # parse worship link
    worship_link_dic = {}
    for a_tag in a_tag_list:
        if not a_tag.text:
            continue
        try:
            link = a_tag.get("href").encode('utf-8')
            worship_name = a_tag.text.encode('utf-8')
            worship_link_dic[worship_name] = link
        except:
            continue

    # parse indivisual worship page
    place_id = num = 1
    len_worship_link_dic = len(worship_link_dic)
    worship_dic = {}
    for worship in worship_link_dic:
        try:
            worship_info = parse_worship_page(worship_link_dic[worship])
            worship_dic[worship] = {}
            worship_dic[worship]["info"] = worship_info
            worship_dic[worship]["place_id"] = str(place_id)

            print "%d/%d parse成功 : %s" % (num, len_worship_link_dic, worship)
            place_id += 1
        except:
            print "%d/%d parse失敗 : %s" % (num, len_worship_link_dic, worship)

        num += 1

    # output worship_places data
    output_fn = 'res/worship_places'
    with open(output_fn, 'w') as f:
        for worship in worship_dic:
            f.write(
                worship_dic[worship]["place_id"] + ',' + \
                worship_dic[worship]["info"]["title"] + ',' + \
                worship_dic[worship]["info"]["title"] + ',' + \
                IS_TEMPLE + ',' + \
                worship_dic[worship]["info"]["address"] + ',' + \
                worship_dic[worship]["info"]["lat"] + ',' + \
                worship_dic[worship]["info"]["lng"] + '\n'
            )

    # output shrines data
    output_fn = 'res/shrines'
    with open(output_fn, 'w') as f:
        for worship in worship_dic:
            f.write(
                worship_dic[worship]["place_id"] + ',' + \
                worship_dic[worship]["info"]["rank"] + ',' + \
                worship_dic[worship]["info"]["obj"] + '\n'
            )


if __name__ == '__main__':
    main()
