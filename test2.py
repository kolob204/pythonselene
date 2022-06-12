
from selene.api import *
from selene.browsers import BrowserName

url = "https://www.google.com/"

#config.browser_name = BrowserName.FIREFOX
config.browser_name = BrowserName.CHROME
config.base_url = 'https://google.com'
config.timeout = 10

browser.open_url('/')
browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))