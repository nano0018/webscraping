"""
Scraper app
"""
import os
import requests
import bs4

CURRENT_PATH = os.getcwd()
text_file = open((CURRENT_PATH + "//web//test.html"), "w", encoding="utf-8")

URL_TO_SCRAP = "https://es.wikipedia.org/wiki/Rompecabezas"
headers = {
    'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}
webpage = requests.get(URL_TO_SCRAP, headers=headers, timeout=1000)

text_file.write(webpage.text)
text_file.close()
text_file = open((CURRENT_PATH + "//soup.html"), "w", encoding="utf-8")
soup = bs4.BeautifulSoup(webpage.content, "lxml")
