"""
Run these tests after completing the setup steps to verify that the framework works.
"""

from pages.search import ChromeSearchPage
from pages.result import ChromeResultPage
from pages.result_link_page import ChromeResultLinkPage
import pytest
import mimetypes
import urllib
import time
from urllib.request import urlopen
import validators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_opera_search(browser,phrase):

  #Scenario: Search feature of chrome
  search_page = ChromeSearchPage(browser)
  result_page = ChromeResultPage(browser)
  # PHRASE = 'panda'

  #Given: Chrome page is loaded
  search_page.load("http://duckduckgo.com/")

  #When: User enters search term "Opera"
  search_page.search(phrase, True)

  #And: search bar shows PHRASE search term
  assert phrase in result_page.search_input_value()

  #And: Links on page shows search term "Opera"
  match = [True for each in result_page.result_link_titles() if phrase.lower() in each.lower()]
  assert len(match) > 0

   # Then: Url shows search query
  assert phrase in result_page.title()



# @pytest.mark.parametrize('s_link', ['https://duckduckgo.com/?q=panda', 'https://duckduckgo.com/?q=python',
#                                     'https://duckduckgo.com/?q=polar bear'])
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_result_link(browser,phrase):
  s_link = 'https://duckduckgo.com/?q='

  #Scenario: Scenario: Clicking a search link
  search_page = ChromeSearchPage(browser)
  result_page = ChromeResultPage(browser)
  result_page_2 = ChromeResultLinkPage(browser)

  # Given:Given the search result page for a search query is displayed
  search_page.load(s_link+phrase)

  #When user clicks first link on search page
  result_page.click_first_link()
  assert phrase in result_page_2.title().lower()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_more_result(browser,phrase):
  s_link = 'https://duckduckgo.com/?q='

  #Scenario: "More Result" button check
  search_page = ChromeSearchPage(browser)
  result_page = ChromeResultPage(browser)

  #Given the search result page for a search query "panda" is displayed\
  search_page.load(s_link + phrase)
  first_result = len(result_page.result_link_titles())
  #Then more results search links are displayed
  i = 1
  while i < 3:
      # assert True == result_page.scroll()
      result_page.scroll()
      result_page.click_more_result()
      assert len(result_page.result_link_titles()) > first_result
      first_result = len(result_page.result_link_titles())

        #And the search result links pertain to "panda"
      match = [True for each in result_page.result_link_titles() if phrase.lower() in each.lower()]
      assert len(match) > 0

    #And the page separator showing "2" should be displayed
      if i == 1:
          assert True == result_page.check_separator(i)
      i = i + 1


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_autocomplete_search(browser,phrase):

  #Scenario: Autocomplete suggestions pertains to search query
  search_page = ChromeSearchPage(browser)

  # PHRASE = 'panda'

  #Given the DuckDuckGo home page is displayed
  search_page.load("http://duckduckgo.com/")

  #When user searches a search query "pan"
  search_page.search(phrase)

  #Then autocomplete suggestion  dropdown appears
  assert True == search_page.autocomplete_check()

  #And each autocomplete suggestion contains text "pan"
  match = [True for each in search_page.autocomplete_values() if phrase.lower() in each]
  assert True == all(match)

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_autocomplete_search_click(browser,phrase):

  #Scenario: Search using autocomplete suggestion
  search_page = ChromeSearchPage(browser)
  result_page = ChromeResultPage(browser)

  # PHRASE = 'panda'

  #Given the DuckDuckGo home page is displayed
  search_page.load("http://duckduckgo.com/")

  #When user search a phrase and selects second autocomplete suggestion
  search_page.search(phrase)
  search_term = search_page.autocomplete_click(2)

  time.sleep(30)
  #And the search result query is equal to selected suggestion
  assert search_term in result_page.search_input_value()


  #And the search result links pertain to selected suggestion
  match = [True for each in result_page.result_link_titles() if search_term.lower() in each.lower()]
  assert len(match) > 0

  # Then the search result title contains selected suggestion (moved at the end to avoid race condition
  assert search_term in result_page.title()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear']) #, 'python', 'polar bear'
def test_image_search(browser,phrase):
  s_link = 'https://duckduckgo.com/?q='

  # Scenario: Do an image search
  result_page = ChromeResultPage(browser)

  # Given the DuckDuckGo search query page is displayed
  result_page.load(s_link+phrase)

  # When user clicks on Image tab
  result_page.images_link_click()

  #Then images link appear
  phrase_ = phrase.replace(' ', '+')

  time.sleep(30)
  #And More Then 100 Images appear
  assert len(result_page.images_link_list()) >= 100

  #And Images have urls that contains images
  assert True == all([is_url_image(url) for url in result_page.images_link_list()])
  assert True == all([sendRequest(url) for url in result_page.images_link_list()])
  assert "https://duckduckgo.com/?q=" + phrase_ + "&iax=images&ia=images" == result_page.images_link_change()


def is_url_image(url):
  image_formats = ("image/png", "image/jpeg", "image/gif")
  site = urlopen(url)
  meta = site.info()  # get header of the http request
  if meta["content-type"] in image_formats:  # check if the content-type is a image
    return True

def sendRequest(url):
  # try:
  #   page = requests.get(url)
  #
  # except Exception as e:
  #   print("error:", e)
  #   return False
  #
  #   # check status code
  #   if (page.status_code != 200):
  #     return False

    # return True
    return validators.url(url)


