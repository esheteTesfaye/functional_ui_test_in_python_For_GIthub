import pytest

from helper.common import URL, ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, driver
from helper.login import *
from helper.utils import generate_string


def setup_module():
    """ open the website"""
    driver.get(url_sign_in)


def teardown_module():
    """ this will close the driver after all test complete"""
    driver.close()


def test_sign_up_sign_in():
    """ this test will made a signup a user
    and try to signin ==> use should get sign in success
    """

    random_text = generate_string(lower=10)
    email = random_text+"@gmila.com"

    phone_no = generate_string(number=7)

    sign_up(email, "sdfds", "sdfds", phone_no, "solomon", "success")

    pass


@pytest.mark.parametrize("email, password, expected_banner_txt",
                         [
                             (ADMIN_USER_EMAIL, "sfsdfsfsadfasfdsaf", LOGIN_TITLE_FAIL_TXT),
                             ("dssdfs@g.com", ADMIN_USER_PASSWORD, LOGIN_TITLE_FAIL_TXT),
                             (ADMIN_USER_EMAIL, "", LOGIN_TITLE_FAIL_TXT),
                             ("",ADMIN_USER_PASSWORD, LOGIN_TITLE_FAIL_TXT),
                             ("","", LOGIN_TITLE_FAIL_TXT),
                             (ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, LOGIN_TITLE_SUCCESS_TXT),

                         ]
                         )
def test_login_with_different_credentials(email, password, expected_banner_txt):
    login(email, password, expected_banner_txt)


@pytest.mark.skip("feature not implemented yet")
def test_logout():
    """ logging as a user
    take an action ( go to profile page ==> u must get that user
    logout and go to profile page ==> you should not get user profile  """
    login("admin@agenda.com", "Agenda@2020")
    logout()

