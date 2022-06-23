import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome(executable_path=os.getenv('webdriverpath')+'\\chromedriver.exe')


class WaitingElement():
    def __init__(self, css_locator):
        self._locator = css_locator

    def _finder(self):
        return browser.find_element_by_css_selector(self._locator)

    # Lazy Proxy (refinde element)
    def __getattr__(self, item):
        return getattr(self._finder(), item)

    def should_contain(self, condition, *args):
        WebDriverWait(browser, 4).until(condition(self._finder, *args))


# Переопределение Selenium conditions
# Копия класса из ec.text_to_be_present_in_element
# Переделанная под наш вариант
class text(object):
    def __init__(self, finder, text_):
        self.finder = finder
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = self.finder().text
            return self.text in element_text
        except StaleElementReferenceException:
            return False


def s(css_selector):
    return WaitingElement(css_selector)


class AbstractPage(object):

    def perform_search(self, searching_str):
        self.input_search.send_keys(searching_str, Keys.ENTER)

    def check_first_search_result(self, condition, value):
        self.first_search_result.should_contain(condition, value)

    def open_page(self):
        browser.get(self.url)


class GooglePage(AbstractPage):
    url = "http://google.com/ncr"
    input_search = s("[name='q']")
    first_search_result = s(".g:nth-child(1)")


class Duckduckgo(AbstractPage):
    url = "https://duckduckgo.com/"
    input_search = s("#search_form_input_homepage")
    first_search_result = s(".nrn-react-div:nth-child(1)")


def teardown():
    browser.quit()

# ====================================================================


GooglePage.open_page(GooglePage)
GooglePage.perform_search(GooglePage,"selenium")
GooglePage.check_first_search_result(GooglePage, text, "Selenium automates browsers")


Duckduckgo.open_page(Duckduckgo)
Duckduckgo.perform_search(Duckduckgo,"selenium")
Duckduckgo.check_first_search_result(Duckduckgo,text, "Selenium WebDriver. If you want to create robust")

teardown()
