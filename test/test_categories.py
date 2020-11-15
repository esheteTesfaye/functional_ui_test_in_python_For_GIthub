from helper.categories import new_category, category_actions, CATEGORY_SUCCESS_MSG, TITLE, DESC, CATEGORY_FAIL_MSG, \
    CATEGORY_ERROR_MSG, url_add_category
from helper.common import URL, ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, USER_EMAIL, USER_PASSWORD
from helper.login import *

def setup_module():
    """ open the website"""
    driver.get(url_add_category)


def teardown_module():
    """ this will close the driver after all test complete"""
    driver.close()


def test_new_category_without_login():
    category_actions()
    new_category(TITLE, DESC, CATEGORY_ERROR_MSG)


def test_new_category_admin():
    login(ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, CATEGORY_SUCCESS_MSG)
    category_actions()
    new_category(TITLE, DESC, CATEGORY_SUCCESS_MSG)

def test_new_category_non_admin():
    login(USER_EMAIL, USER_PASSWORD, CATEGORY_SUCCESS_MSG)
    category_actions()
    new_category(TITLE, DESC, CATEGORY_FAIL_MSG)










