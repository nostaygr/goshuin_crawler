.PHONY: package

RES_DIR=res

package:
		pip install -U requests
		pip install -U BeautifulSoup

crawl_shrine:
		if [ ! -d ${RES_DIR} ]; then mkdir -p ${RES_DIR}; fi
		python shrine/crawler.py

crawl_temple:
		if [ ! -d ${RES_DIR} ]; then mkdir -p ${RES_DIR}; fi
		python temple/crawler.py
