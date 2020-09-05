"""
This page contains ChromeSearchPage class
a page object for Google Chrome search page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver
import time

class ChromeSearchPage:
    SEARCH_INPUT = (By.ID , "search_form_input_homepage")
    SEARCH_BUTTON = (By.ID, "search_button_homepage")
    AUTOC_DROPDOWN = (By.CLASS_NAME, "search__autocomplete")
    AUTOC_VALUES = (By.CLASS_NAME, "acp")
    AUTOC_TEXT = (By.CLASS_NAME, "t-normal")

    # AUTOC_VALUES = (By.CLASS_NAME, "acp-wrap")
    # URL = "http://duckduckgo.com/"

    def __init__(self,browser):
        self.browser = browser

    def load(self, URL):
        #TODO load main search page
        self.browser.get(URL)

    def search(self, phrase, click= False):
        #TODO enter search in search bar
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        # search_input.send_keys(phrase + Keys.RETURN) # for testcase where phrase and enter key is hit
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        time.sleep(0.5)
        if click:
            search_button.click() # for testcase where phrase and search button is clicked-

    def autocomplete_check(self):
        autoc_comp = self.browser.find_element(*self.AUTOC_DROPDOWN)
        autoc_values = self.browser.find_elements(*self.AUTOC_VALUES)
        if autoc_comp.is_displayed() and autoc_values: #autoc_values.get_attribute('value') != ""
            return True
        return False

    def autocomplete_values(self):
        autoc_text = self.browser.find_elements(*self.AUTOC_TEXT)
        return [each.text for each in autoc_text]

    def autocomplete_click(self, index):
        autoc_values = self.browser.find_elements(*self.AUTOC_VALUES)
        search_term = autoc_values[index].get_attribute("textContent")
        autoc_values[index].click()
        return search_term



