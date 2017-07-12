# coding: utf-8

import sys
import requests
from bs4 import BeautifulSoup
sys.path.append("lib")
import api
import crawl_wiki


URL_BASE = "https://ja.wikipedia.org"
IS_TEMPLE = "0"


def main():
    # get base url
    url = URL_BASE + "/wiki/神社一覧"
    shrine_link_dic = crawl_wiki.get_links_from_list_page(url)

    # parse indivisual shrine page
    num = 1
    len_shrine_link_dic = len(shrine_link_dic)
    shrine_dic = {}
    for shrine in shrine_link_dic:
        try:
            shrine_info = crawl_wiki.parse_shrine_page(shrine_link_dic[shrine])
            shrine_dic[shrine] = {}
            shrine_dic[shrine]["info"] = shrine_info

            print "%d/%d parse成功 : %s" % (num, len_shrine_link_dic, shrine)
        except:
            print "%d/%d parse失敗 : %s" % (num, len_shrine_link_dic, shrine)

        num += 1

    # output shrine_places data
    output_fn = 'res/shrines_base'
    with open(output_fn, 'w') as f:
        for shrine in shrine_dic:
            f.write(
                shrine_dic[shrine]["info"]["title"] + ',' + \
                shrine_dic[shrine]["info"]["title"] + ',' + \
                IS_TEMPLE + ',' + \
                shrine_dic[shrine]["info"]["address"] + ',' + \
                shrine_dic[shrine]["info"]["lat"] + ',' + \
                shrine_dic[shrine]["info"]["lng"] + ',' + \
                shrine_dic[shrine]["info"]["rank"] + ',' + \
                shrine_dic[shrine]["info"]["obj"] + '\n'
            )


if __name__ == '__main__':
    main()
