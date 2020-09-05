"""
This module contains ChromeResultPage class
a page object for Chrome search result page
"""
from selenium.webdriver.common.by import By
import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



class ChromeResultPage():
    SEARCH_INPUT = (By.ID, "search_form_input")
    RESULT_LINK = (By.CSS_SELECTOR, 'a.result__a')
    RESULT_PAGE = (By.CSS_SELECTOR,'a.result--more__btn')
    # result result--more
    SEPARATOR = (By.XPATH, "//div[@class='result__pagenum  result__pagenum--side' and text()='2']")
    # SEPARATOR2 = (By.XPATH, "//div[@class='result__pagenum  result__pagenum--side' and text()='3']")
    SEARCH_BTN = (By.ID, 'search_button')
    IMAGES = (By.XPATH, "//a[@data-zci-link='images' and text()='Images']")
    IMAGES_SRC = (By.XPATH, "//img[@class='tile--img__img  js-lazyload']")
    SCROLL_PAUSE_TIME = 1
    # SEPARATOR = (By.CLASS_NAME, 'result__pagenum  result__pagenum--side')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):

        links = self.browser.find_elements(*self.RESULT_LINK)

        return [each.text for each in links]

    def search_input_value(self):

        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def title(self):

        return self.browser.title

    def click_first_link(self):
        link = self.browser.find_element(*self.RESULT_LINK)
        link.click()

    def click_more_result(self):
        more_result= self.browser.find_element(*self.RESULT_PAGE)
        more_result.click()

    def check_separator(self,i):
        if i== 1 and self.browser.find_element(*self.SEPARATOR):
            return True
        # elif i== 2 and self.browser.find_element(*self.SEPARATOR2):
        #     return True
        return False

    def scroll(self):
    #     last_height = self.browser.execute_script("return document.body.scrollHeight")
    #     html = self.browser.find_element_by_tag_name('html')
    #     html.send_keys(Keys.END)
    # # #     # Wait to load page
    #     time.sleep(self.SCROLL_PAUSE_TIME)
    #
    #     new_height = self.browser.execute_script("return document.body.scrollHeight")
    #     if new_height > last_height:
    #         return True
    #     return False
        more_result = self.browser.find_element(*self.RESULT_PAGE)
        self.browser.execute_script("arguments[0].scrollIntoView();", more_result)
        self.browser.execute_script("$(arguments[0]).click();", more_result)

    def images_link_click(self):
        images = self.browser.find_element(*self.IMAGES)
        images.click()

    def images_link_change(self):
        return self.browser.current_url

    def images_link_list(self):
        image_links = self.browser.find_elements(*self.IMAGES_SRC)
        return [links.get_attribute("src") for links in image_links]

    def load(self, URL):
        #adding it here to test direct load of respective url without going to home page firt
        self.browser.get(URL)









