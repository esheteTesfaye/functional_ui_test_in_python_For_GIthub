from selenium import webdriver
from helper.utils import load_xpath

common_prop = load_xpath("common")

URL = common_prop["common"]["url"]
DRIVER = common_prop["common"]["driver"]


# xpath list
banner_xp = common_prop["xpath"]["banner"]


# system user credentials

# admin user credentials
ADMIN_USER_EMAIL = "admin@agenda.com"
ADMIN_USER_PASSWORD = "Agenda@2020"

#driver = webdriver.Chrome(DRIVER)
driver = webdriver.Firefox(executable_path=DRIVER)
driver.get(URL)
