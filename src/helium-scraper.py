"""
Helium web scraper
"""

import os
from helium import *

# Ruta actual
CURRENT_PATH = os.getcwd()

# Página web
URL = 'https://webcache.googleusercontent.com/search?q=cache:https://www.classcentral.com'

browser = start_firefox(URL, headless=True)
Config.implicit_wait_secs = 15
html = browser.page_source

text_file = open((CURRENT_PATH + "//web//test_helium.html"), "w", encoding="utf-8")
text_file.write(html)
text_file.close()