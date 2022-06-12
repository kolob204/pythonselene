from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as ec

url = "https://www.google.com/"

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('-start-maximized')

experimentalFlags = ['same-site-by-default-cookies@1','cookies-without-same-site-must-be-secure@1']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
driver.implicitly_wait(15)
#=====================================================

driver.get(url)
element1 = driver.find_element_by_css_selector('[name="q"]')
element1.send_keys('selene')
element1.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 15)

wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#search')))
element = driver.find_element_by_css_selector('[id="search"]')
#print(element.text)
wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Selene - User-oriented Web UI browser tests in Python')]")))

driver.quit()






#assert element.text  'Selene - User-oriented Web UI browser tests in Python'
#StringAssert.Contains(expected, element.text, "Assert error!!");