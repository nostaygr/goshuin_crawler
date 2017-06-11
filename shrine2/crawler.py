# coding: utf-8

import sys
import requests
from bs4 import BeautifulSoup
sys.path.append("lib")
import api
import crawl_wiki


URL_BASE = "https://ja.wikipedia.org"
IS_TEMPLE = "1"


def main():
    # get base url
    url = URL_BASE + "/wiki/日本の寺院一覧"
    temple_link_dic = crawl_wiki.get_links_from_list_page(url)

    # parse indivisual temple page
    num = 1
    len_temple_link_dic = len(temple_link_dic)
    temple_dic = {}
    for temple in temple_link_dic:
        try:
            temple_info = crawl_wiki.parse_temple_page(temple_link_dic[temple])
            temple_dic[temple] = {}
            temple_dic[temple]["info"] = temple_info

            print "%d/%d parse成功 : %s" % (num, len_temple_link_dic, temple)
        except:
            print "%d/%d parse失敗 : %s" % (num, len_temple_link_dic, temple)

        num += 1

    print temple_dic

    # output temple_places data
    output_fn = 'res/temples_base'
    with open(output_fn, 'w') as f:
        for temple in temple_dic:
            f.write(
                temple_dic[temple]["info"]["title"] + ',' + \
                temple_dic[temple]["info"]["title"] + ',' + \
                IS_TEMPLE + ',' + \
                temple_dic[temple]["info"]["address"] + ',' + \
                temple_dic[temple]["info"]["lat"] + ',' + \
                temple_dic[temple]["info"]["lng"] + ',' + \
                temple_dic[temple]["info"]["sect"] + ',' + \
                temple_dic[temple]["info"]["rank"] + ',' + \
                temple_dic[temple]["info"]["obj"] + '\n'
            )


if __name__ == '__main__':
    main()
