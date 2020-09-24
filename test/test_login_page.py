
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from helper.common import URL, DRIVER
from helper.login import email_xp, password_xp, submit_xp

#driver = webdriver.Chrome(DRIVER)
driver = webdriver.Firefox(executable_path=DRIVER)
driver.get(URL)

assert "Agenda App" in driver.title

# click sign in tab
driver.find_element_by_link_text("Sign in").click()
user = driver.find_element_by_xpath(email_xp)
user.send_keys("admin@agenda.com")
passwd = driver.find_element_by_xpath(password_xp)
passwd.send_keys("Agenda@2020")
driver.find_element_by_xpath(submit_xp).click()
assert "Agenda Success" in driver.title
driver.close()




