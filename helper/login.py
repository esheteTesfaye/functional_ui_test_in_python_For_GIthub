from helper.common import driver, banner_xp
from helper.utils import load_xpath, sleep_seconds

sign_in_link_txt = "Sign in"
login_xp = load_xpath("login")
email_xp = login_xp["login"]["email"]
password_xp = login_xp["login"]["password"]
submit_xp = login_xp["login"]["submit"]


# login success message
LOGIN_BANNER_SUCCESS_TXT = "welcome"
LOGIN_BANNER_FAIL_TXT = "wrong"
LOGIN_TITLE_SUCCESS_TXT = "agenda app"
LOGIN_TITLE_FAIL_TXT = "signin agenda"

# click sign in tab

# login method

def login(email, password, title_txt):
    """ this method will let you to login to ui with the given user name and password """
    driver.find_element_by_link_text(sign_in_link_txt).click()
    user = driver.find_element_by_xpath(email_xp)
    user.send_keys(email)
    passwd = driver.find_element_by_xpath(password_xp)
    passwd.send_keys(password)
    driver.find_element_by_xpath(submit_xp).click()
    sleep_seconds(2) # give some time until page loads
    actual_title = driver.title.lower()
    assert title_txt.lower() in actual_title


def logout():
    """ this method will let you logout a given user"""
    # TODO add the signup similar to signin one

    pass

def sign_up(email, phone, password, confirm_password, name):
    """ write all steps to signup"""
    # TODO add the signup similar to signin one
    pass
