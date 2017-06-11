# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


TEMPLE_JUDGE_LIST = ["寺", "院", "師"]
SHRINE_JUDGE_LIST = ["社", "宮", "荷"]
URL_BASE = "https://ja.wikipedia.org"


# wikipediaページから,urlを抽出
def get_links_from_list_page(url):
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
   
    return worship_link_dic


# wikipediaのtempleページのinfobox欄をparse
def parse_temple_page(link):
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
    if decision_char not in TEMPLE_JUDGE_LIST:
        print "this is not temple page"
        raise

    title = base_title.text.encode('utf-8').replace('\n', '')
    rows = table.find_all("tr")
    for row in rows:
        if not row.find("th"):
            continue
        th_text = row.find("th").text.encode('utf-8')
        if th_text == "所在地":
            address = row.find("td").text.encode('utf-8').replace('\n', '')
        if th_text == "寺格":
            rank = row.find("td").text.encode('utf-8').replace('\n', ',')
        if th_text == "宗派" or th_text == "宗旨":
            sect = row.find("td").text.encode('utf-8').replace('\n', ',')
        if th_text == "本尊":
            obj = row.find("td").text.encode('utf-8').replace('\n', ',')

    try:
        address
    except:
        address = ""

    try:
        rank
    except:
        rank = ""

    try:
        sect
    except:
        sect = ""

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
    info["rank"] = rank
    info["sect"] = sect
    info["obj"] = obj

    return info


# wikipediaのinfobox欄をparse
def parse_shrine_page(link):
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
    if decision_char not in SHRINE_JUDGE_LIST:
        print "this is not shrine page"
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
            obj = row.find("td").text.encode('utf-8').replace('\n', ',').replace(',', '・')

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
