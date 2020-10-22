import platform

import random
import string

from selenium import webdriver
from helper.utils import load_xpath, get_system_os_type

common_prop = load_xpath("common")
# os names
os_name_windows ="windows"
os_name_mac = "darwin"
# browser names
driver_name_firefox = "firefox"
driver_name_chrome = "chrome"
driver_name_ie = "ie"
driver_name_safari = "safari"

URL = common_prop["common"]["url"]


def select_driver(browser=driver_name_firefox):
    """ this method will prepare  selenium driver based on the given os type and driver type"""
    os_type = get_system_os_type()

    if os_name_windows in os_type.lower():
        if browser == driver_name_firefox:
            driver_path = common_prop["common"]["gecko_driver_win"]
            driver = webdriver.Firefox(executable_path=driver_path)
            return driver

        elif browser == driver_name_ie:
            return "ie"
        elif browser == driver_name_chrome:
            return "chrome"
    elif os_name_mac in os_type.lower():
        if browser ==driver_name_firefox:
            driver_path = common_prop["common"]["gecko_driver_mac"]
            driver = webdriver.Firefox(executable_path=driver_path)
            return driver
        elif browser == driver_name_safari:
            return "safari"
        elif browser==driver_name_chrome:
            return "chrome"


# xpath list
banner_xp = common_prop["xpath"]["banner"]


# system user credentials

# admin user credentials
ADMIN_USER_EMAIL = "admin@agenda.com"
ADMIN_USER_PASSWORD = "Agenda@2020"

#user credentials

USER_EMAIL = "user@agenda.com"
USER_PASSWORD = "Agenda@2020"

#driver = webdriver.Chrome(DRIVER)
driver =select_driver(browser=driver_name_firefox)
driver.get(URL)

def generate_string(upper=0, lower=0, number=0, special=0):
    """ this method will generate random string based on the given inputs"""
    lower = [random.choice(string.ascii_lowercase) for _ in range(lower)]
    upper = [random.choice(string.ascii_uppercase) for _ in range(upper)]
    number = [random.choice(string.digits) for _ in range(number)]
    special = [random.choice(string.punctuation) for _ in range(special)]

    final_string = number + special +  lower + upper
    return "".join(final_string)