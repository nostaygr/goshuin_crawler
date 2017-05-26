.PHONY: package

RES_DIR=res

package:
		pip install -U requests
		pip install -U BeautifulSoup

crawl_case1:
		if [ ! -d ${RES_DIR} ]; then mkdir -p ${RES_DIR}; fi
		python case1/crawler.py
