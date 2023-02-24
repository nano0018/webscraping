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

    #Set the translate language
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

    # Force to use google translate
    for i in range(3):
        pyautogui.sleep(0.25)
        pyautogui.press('up')
    pyautogui.press('enter')

    time.sleep(2)
    for i in range(3, 0, -1):
        place = "window.scrollTo({ top: (document.body.scrollHeight / " + \
            str(i) + "), behavior: 'smooth' });"
        driver.execute_script(place)
        time.sleep(0.5)
    time.sleep(2)
    print('Done!')

    # Define new set to gater all non-repeating href links
    href_links = set()
    a_list = driver.find_elements_by_tag_name("a")
    for link in a_list:
        href_links.add(link.get_attribute("href"))
    print('Found:',len(href_links), 'link(s)')

    # Create index.html
    html_source_code = driver.page_source
    text_file = open((current_path + "//web//index.html"),
                     "w", encoding="utf-8")
    text_file.write(html_source_code)
    text_file.close()


web_scraper('https://www.classcentral.com/', "hi")

# web_scraper('https://www.cmcsas.co', "hi")
