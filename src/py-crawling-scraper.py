"""
Scraping using proxy crawl
"""

import lxml
import requests
import os

CURRENT_PATH = os.getcwd()
text_file = open((CURRENT_PATH + "//web//test_proxy.html"), "w", encoding="utf-8")

URL_TO_SCRAP = "https://www.classcentral.com/"


proxylcrawl_prefix = "https://api.crawlbase.com/"
javascript_token = "PS5b5WDFkZ5LOc4n109hBQ"
url_with_proxy = f"{proxylcrawl_prefix}?token={javascript_token}&url={URL_TO_SCRAP}"

webpage = requests.get(url_with_proxy, timeout=1000)

text_file.write(webpage.text)
text_file.close()