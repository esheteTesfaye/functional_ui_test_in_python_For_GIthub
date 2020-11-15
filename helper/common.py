import platform

import random
import string

from selenium import webdriver
from helper.utils import load_prop_file, get_system_os_type

# reading test environment setups
test_env_prop = load_prop_file("test_env_setup")
URL = test_env_prop["test_env"]["url"]

# os names
os_name_windows = test_env_prop["os"]["windows"]
os_name_mac = test_env_prop["os"]["mac"]

# all browser names
driver_name_firefox = test_env_prop["browser_name"]["firefox"]
driver_name_chrome = test_env_prop["browser_name"]["chrome"]
driver_name_ie = test_env_prop["browser_name"]["ie"]
driver_name_safari = test_env_prop["browser_name"]["safari"]
driver_name_opera = test_env_prop["browser_name"]["opera"]

# selected browser
selected_browser_name = test_env_prop["test_env"]["browser_name"]

# reading xpaths
common_prop = load_prop_file("xpath/common")


def start_driver():
    """ this method will prepare  selenium driver based on
     the given os type and driver type from test env setup properties file"""
    os_type = get_system_os_type()

    if os_name_windows in os_type.lower():
        if selected_browser_name == driver_name_firefox:
            driver_path = test_env_prop["drivers"]["gecko_driver_win"]
            driver = webdriver.Firefox(executable_path=driver_path)
            return driver
        elif selected_browser_name == driver_name_ie:
            return "ie"
        elif selected_browser_name == driver_name_chrome:
            driver_path = test_env_prop["drivers"]["chrome_driver_win"]
            driver = webdriver.Chrome(executable_path=driver_path)
            return driver
    elif os_name_mac in os_type.lower():
        if selected_browser_name == driver_name_firefox:
            driver_path = test_env_prop["drivers"]["gecko_driver_mac"]
            driver = webdriver.Firefox(executable_path=driver_path)
            return driver
        elif selected_browser_name == driver_name_safari:
            return "safari"
        elif selected_browser_name == driver_name_chrome:
            driver_path = test_env_prop["drivers"]["chrome_driver_mac"]
            driver = webdriver.Chrome(executable_path=driver_path)
            return driver
        elif selected_browser_name == driver_name_opera:
            driver_path = test_env_prop["drivers"]["opera_driver_mac"]
            driver = webdriver.Chrome(executable_path=driver_path)
            return driver


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
driver =start_driver()
driver.get(URL)

def generate_string(upper=0, lower=0, number=0, special=0):
    """ this method will generate random string based on the given inputs"""
    lower = [random.choice(string.ascii_lowercase) for _ in range(lower)]
    upper = [random.choice(string.ascii_uppercase) for _ in range(upper)]
    number = [random.choice(string.digits) for _ in range(number)]
    special = [random.choice(string.punctuation) for _ in range(special)]

    final_string = number + special +  lower + upper
    return "".join(final_string)