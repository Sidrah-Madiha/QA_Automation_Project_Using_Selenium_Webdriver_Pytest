"""
This module contains ChromeResultLinkPage class
a page object for Chrome search result lead link webpage page
"""
from selenium.webdriver.common.by import By
import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ChromeResultLinkPage():
    # SEARCH_INPUT = (By.ID, "search_form_input")
    # RESULT_LINK = (By.CSS_SELECTOR, 'a.result__a')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

