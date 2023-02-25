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
        pyautogui.moveTo(0, 127, 2)
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
        full_path = current_path + "\\web\\"
        if path:
            full_path = current_path + "\\web\\" + path + "\\"
            try:
                os.mkdir(full_path)
            except OSError as error:
                print(error)

        full_path += filename
        print(full_path)
        html_source_code = "<!DOCTYPE html>" + driver.page_source
        try:
            text_file = open((full_path),
                             "w", encoding="utf-8")
            text_file.write(html_source_code)
            text_file.close()
        except OSError as error:
            print("Filename is not valid!", error)

    # Scrolling down for full image load
    scroll_page()

    # Define new set to gather all non-repeating href links
    href_links_set = set()
    a_list = driver.find_elements_by_tag_name("a")
    for link in a_list:
        href_links_set.add(link.get_attribute("href"))
    href_links = list(href_links_set)
    print('Found:', len(href_links), 'link(s)')

    driver.execute_script('let css_selector; let new_href')

    for href_link in href_links_set:

        if not href_link:
            continue

        href_link_raw = href_link.replace('https://', '')
        href_data = href_link_raw.split('/')

        index_path = len(href_data) - 1

        if not href_data[index_path]:
            href_data.pop()
            index_path -= 1

        if len(href_data) < 1:
            continue

        if len(href_data) < 3:
            new_url = href_data[index_path]
        else:
            new_url = href_data[index_path - 1]

        if ("mailto" in new_url or "tweet" in new_url) or ("facebook" in new_url or "twitter" in new_url):
            continue

        print(new_url)
        page_filename = href_data[len(href_data) - 1] + ".html"
        html_path = new_url.replace("/", "\\")
        driver.get(href_link)
        scroll_page()
        save_page(path=html_path, filename=page_filename)

    driver.get(url)
    scroll_page()

    for href_link in href_links:

        if not href_link:
            continue

        href_link_raw = href_link.replace('https://', '')
        href_data = href_link_raw.split('/')

        index_path = len(href_data) - 1

        if not href_data[index_path]:
            href_data.pop()
            index_path -= 1

        if len(href_data) < 1:
            continue

        if len(href_data) < 3:
            new_url = href_data[index_path]
        else:
            new_url = href_data[index_path - 1]

        if ("mailto" in new_url or "tweet" in new_url) or ("facebook" in new_url or "twitter" in new_url):
            continue

        print(new_url)
        page_filename = href_data[len(href_data) - 1] + ".html"

        css_selector_element = 'a[href="' + href_link + '"]'
        new_href = (new_url + "/" + page_filename)

        driver.execute_script('css_selector = ' + "'" +
                              css_selector_element + "'")
        driver.execute_script('new_href = ' + "'" + new_href + "'")
        try:
            driver.execute_script(
                "try {document.querySelector(css_selector).setAttribute('href', new_href)} catch (error) {console.log()}")
        finally:
            print('JS Error!')
            alt_href = "/" + new_url + "/" + href_data[len(href_data) - 1]
            css_selector_element = 'a[href="' + alt_href + '"]'
            driver.execute_script('css_selector = ' +
                                  "'" + css_selector_element + "'")
            driver.execute_script(
                "try {document.querySelector(css_selector).setAttribute('href', new_href)} catch (error) {console.log()}")
    # Create index.html
    save_page(filename="index.html")