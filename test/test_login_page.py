import pytest

from helper.common import URL, ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, driver
from helper.login import *

driver.get(URL)

def test_sign_up_sign_in():
    """ this test will made a signup a user
    and try to signin ==> use should get sign in success
    """
    sign_up("abdcdfg@gmila.com", "223-333-3333", "sdfds", "sdfsfdsf", "any name")
    pass


def test_login_with_wrong_credentials():
    login(ADMIN_USER_EMAIL, "sfsdfsfsadfasfdsaf", LOGIN_FAIL_MSG)
    login("dssdfs@g.com", ADMIN_USER_PASSWORD, LOGIN_FAIL_MSG)
    login(ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, LOGIN_SUCCESS_MSG)

    driver.find_element_by_partial_link_text("Profile").click()
    driver.close()


def test_logout():
    """ loing as a user
    take an action ( go to profile page ==> u must get that user
    logout and go to profile page ==> you should not get user profile  """
    login("admin@agenda.com", "Agenda@2020")

    pass

