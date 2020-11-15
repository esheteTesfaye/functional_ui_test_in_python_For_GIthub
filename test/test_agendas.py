import pytest
from datetime import time

from helper.agendas import AGENDA_ERROR_MSG, AGENDA_SUCCESS_MSG, new_agenda, TITLE, DESC, agenda_actions, url_addagenda
from helper.common import URL, ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, USER_EMAIL, USER_PASSWORD, driver, generate_string
from helper.login import LOGIN_BANNER_SUCCESS_TXT, login

def setup_module():
    """ open the website"""
    driver.get(url_addagenda)


def teardown_module():
    """ this will close the driver after all test complete"""
    driver.close()

def test_create_agenda_without_login_not_allowed():
    """ without login you should not able to create agenda"""
    agenda_actions()
    new_agenda(TITLE, DESC, AGENDA_ERROR_MSG)

@pytest.mark.parametrize("title_txt ,category_txt,desc_txt,expected_txt", [(generate_string(upper=7), "sports", "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", True),
                                                             (generate_string(upper=7), "sports", "DESCRIPTION ", False),
                                                             (generate_string(upper=7), "sports", None, False),
                                                             (generate_string(upper=7), None , "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", False),
                                                             (None, "sports", "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", False)])
def test_create_agenda_with_login(title_txt ,category_txt,desc_txt,expected_txt):
    """ this test is to create agenda with different data types"""
    login(ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, LOGIN_BANNER_SUCCESS_TXT)
    time.sleep(2)
    agenda_actions()
    new_agenda(title_txt ,category_txt,desc_txt,expected_txt)



