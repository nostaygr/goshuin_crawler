.PHONY: package

RES_DIR=res

package:
		pip install -U requests
		pip install -U BeautifulSoup

crawl_case1:
		if [ ! -d ${RES_DIR} ]; then mkdir -p ${RES_DIR}; fi
		python shrine/crawler.py

crawl_case2:
		if [ ! -d ${RES_DIR} ]; then mkdir -p ${RES_DIR}; fi
		python temple/crawler.py
