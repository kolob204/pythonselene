from selene.browser import open_url
from selene.support.jquery_style_selectors import s, ss
from selene.support.conditions import have


class GooglePage(object):
    def open(self):
        open_url('http://google.com/ncr')
        return self

    def search(self, text):
        s("[name='q']").set(text).press_enter()
        return SearchResultsPage()


class SearchResultsPage(object):
    def __init__(self):
        self.results = ss('.g .tF2Cxc')


def test_google_search():
    google = GooglePage().open()
    search = google.search('selene')
    search.results[0].should(have.text('Selene - Wikipedia'))
   # search.results[1].should(have.text('Selene - User-oriented Web UI browser tests in Python'))
