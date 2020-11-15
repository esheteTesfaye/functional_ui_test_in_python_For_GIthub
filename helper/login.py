from helper.common import driver, banner_xp, URL
from helper.utils import load_prop_file, sleep_seconds
url_sign_in = URL + "/signin"
sign_in_link_txt = "Sign in"
sign_up_link_txt = "Create new account"
login_xp = load_prop_file("xpath/login")
email_xp = login_xp["login"]["email"]
password_xp = login_xp["login"]["password"]
confirm_password_xp = login_xp["login"]["confirm_password"]
phone_xp = login_xp["login"]["phone"]
name_xp = login_xp["login"]["name"]
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


def sign_up(email, password, confirm_password, phone, name, banner_txt):
    """ write all steps to signup"""
    driver.find_element_by_link_text(sign_in_link_txt).click()
    driver.find_element_by_link_text(sign_up_link_txt).click()
    user = driver.find_element_by_xpath(email_xp)
    user.send_keys(email)
    passwrd = driver.find_element_by_xpath(password_xp)
    passwrd.send_keys(password)
    confirm_passwrd = driver.find_element_by_xpath(confirm_password_xp)
    confirm_passwrd.send_keys(confirm_password)
    phone_no = driver.find_element_by_xpath(phone_xp)
    phone_no.send_keys(phone)
    user_name = driver.find_element_by_xpath(name_xp)
    user_name.send_keys(name)
    driver.find_element_by_xpath(submit_xp).click()
    assert banner_txt in driver.find_element_by_xpath(banner_xp)

