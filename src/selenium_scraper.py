"""
Selenium web scarping
"""
import os
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver import ActionChains


def web_scraper(url, language="es"):
    """Web scraper for 1 level scrap"""
    # Current path
    current_path = os.getcwd()

    # Browser options
    options = webdriver.ChromeOptions()

    # Set the translate language
    options.add_argument("--lang=" + language)
    prefs = {
        "translate_whitelists": {"en-US": "hi"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)
    driver_path = current_path + "\\.driver\\chromedriver.exe"

    driver = webdriver.Chrome(driver_path, options=options)

    # Init browser
    driver.maximize_window()
    time.sleep(1)
    print('Opening... Done!')
    driver.get(url)
    print('Waiting for full load!')

    action_chains = ActionChains(driver)
    action_chains.context_click().perform()

    def scroll_page():
        """Scroll the page and force to use google translate"""

        pyautogui.press('esc')
        pyautogui.moveTo(100, 200, 2)
        pyautogui.click(button='right')
        for i in range(3):
            pyautogui.sleep(0.25)
            pyautogui.press('up')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('esc')

        for i in range(3, 0, -1):
            place = "window.scrollTo({ top: (document.body.scrollHeight / " + \
                str(i) + "), behavior: 'smooth' });"
            driver.execute_script(place)
            time.sleep(0.5)
        time.sleep(2)
        print('Done!')

    def save_page(path="", filename=""):
        full_path = "//web//"
        if not path:
            full_path = "//web//" + path + "//"
        full_path += filename
        html_source_code = driver.page_source
        text_file = open((current_path + full_path),
                         "w", encoding="utf-8")
        text_file.write(html_source_code)
        text_file.close()

    # Scrolling down for full image load
    scroll_page()

    # Create index.html
    save_page(filename="index.html")

    # Define new set to gather all non-repeating href links
    href_links = set()
    a_list = driver.find_elements_by_tag_name("a")
    for link in a_list:
        href_links.add(link.get_attribute("href"))
    print('Found:', len(href_links), 'link(s)')

    for href_link in href_links:

        raw_url = url.replace('https://', '')
        if not href_link:
            continue

        href_data = href_link.split('/')
        index_path = len(href_data) - 1

        if not href_data[index_path]:
            index_path -= 1

        new_url = href_data[index_path]
        if new_url == raw_url:
            continue

        driver.get(url + "/" + new_url)
        scroll_page()
        save_page(path=new_url, filename=(new_url + ".html"))


web_scraper('https://www.classcentral.com/', "hi")

# web_scraper('https://www.cmcsas.co', "hi")
