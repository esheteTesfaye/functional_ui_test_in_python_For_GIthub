from helper.common import driver, banner_xp
from helper.utils import load_xpath

sign_in_link_txt = "Sign in"
login_xp = load_xpath("login")
email_xp = login_xp["login"]["email"]
password_xp = login_xp["login"]["password"]
submit_xp = login_xp["login"]["submit"]


# login success message
LOGIN_SUCCESS_MSG = "welcome"
LOGIN_FAIL_MSG = "wrong"

# click sign in tab

# login method
def login(email, password, banner_txt):
    """ this method will let you to login to ui with the given user name and password """
    driver.find_element_by_link_text(sign_in_link_txt).click()
    user = driver.find_element_by_xpath(email_xp)
    user.send_keys(email)
    passwd = driver.find_element_by_xpath(password_xp)
    passwd.send_keys(password)
    driver.find_element_by_xpath(submit_xp).click()
    assert banner_txt in driver.find_element_by_xpath(banner_xp)


def logout():
    """ this method will let you logout a given user"""
    pass

def sign_up(email, phone, password, confirm_password, name):
    """ write all steps to signup"""
    pass
