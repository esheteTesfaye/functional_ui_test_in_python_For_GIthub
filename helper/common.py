from selenium import webdriver
from helper.utils import load_xpath

common_prop = load_xpath("common")
driver_name_firefox = "firefox"
driver_name_chrome = "chrome"
driver_name_ie = "ie"
driver_name_safari = "safari"

URL = common_prop["common"]["url"]
def select_driver(os_type="win", browser=driver_name_firefox):
    """ this method will prepare  selenium driver based on the given os type and driver type"""
    if os_type =="win":
        if browser == driver_name_firefox:
            return common_prop["common"]["gecko_driver_win"]
        elif browser == driver_name_ie:
            return "ie"
        elif browser == driver_name_chrome:
            return "chrome"
    elif os_type =="mac":
        if browser ==driver_name_firefox:
            return common_prop["common"]["gecko_driver_mac"]
        elif browser == driver_name_safari:
            return "safari"
        elif browser==driver_name_chrome:
            return "chrome"

DRIVER = select_driver(os_type="win", browser=driver_name_firefox)


# xpath list
banner_xp = common_prop["xpath"]["banner"]


# system user credentials

# admin user credentials
ADMIN_USER_EMAIL = "admin@agenda.com"
ADMIN_USER_PASSWORD = "Agenda@2020"

#driver = webdriver.Chrome(DRIVER)
driver = webdriver.Firefox(executable_path=DRIVER)
driver.get(URL)
