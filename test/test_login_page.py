
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from helper.common import URL, DRIVER
from helper.login import xpath_email, xpath_password, xpath_submit

driver = webdriver.Chrome(DRIVER)
driver.get(URL)

assert "Agenda App" in driver.title

# click sign in tab
driver.find_element_by_link_text("Sign in").click()
user = driver.find_element_by_xpath(xpath_email)
user.send_keys("admin@agenda.com")
passwd = driver.find_element_by_xpath(xpath_password)
passwd.send_keys("Agenda@2020")
driver.find_element_by_xpath(xpath_submit).click()
assert "Agenda Success" in driver.title
driver.close()




