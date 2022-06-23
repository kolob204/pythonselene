import contextlib
import os
import time

import stopit as stopit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

@contextlib.contextmanager
def supress(*exceptions):
    try:
        yield
    except exceptions:
        pass


browser = webdriver.Chrome(executable_path=os.getenv('webdriverpath')+'\\chromedriver.exe')


def wait_for(finder, condition):
    result = None

    with supress(NoSuchElementException):
        result = finder()

    with stopit.ThreadingTimeout(4) as _ctx_:
        while not (result and condition(result)):
            with supress(NoSuchElementException):
                time.sleep(0.1)
                result = finder()

    #Если таймаут закончился и блок кода был установлен
    if not _ctx_:
        raise stopit.TimeoutException('failed wait Element')
    return result


class WaitingElement():
    def __init__(self, css_locator):
        self._locator = css_locator

    def _finder(self):
        return browser.find_element_by_css_selector(self._locator)

    # Lazy Proxy (refinde element)
    def __getattr__(self, item):
        return getattr(self._finder(), item)
    #если self._finder
    #AttributeError: 'function' object has no attribute 'send_keys'

    def shouldbe(self, condition):
        wait_for(self._finder, condition)
    #если self._finder()
    #TypeError: 'WebElement' object is not callable




def s(css_selector):
    return WaitingElement(css_selector)


browser.get("http://google.com/ncr")
s("[name='q']").send_keys("selenium",Keys.ENTER)
s(".g:nth-child(1)").shouldbe(lambda element: "Selenium automates browsers" in element.text)
#you want to use Selenium WebDriver