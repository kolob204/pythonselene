from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as ec

url = "https://www.google.com/"

driver = webdriver.Chrome()
driver.implicitly_wait(15)

#=====================================================
def clickElementByXpath(xpath):
    

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