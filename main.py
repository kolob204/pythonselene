from selene.api import *
from selene.browsers import BrowserName

# #some - id
# .some - class
#Configuration

url = "https://www.google.com/"
#config.browser_name = BrowserName.FIREFOX
config.browser_name = BrowserName.CHROME
#TimeOuts:
config.timeout = 10

#===========================================================
browser.open_url(url)

browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))