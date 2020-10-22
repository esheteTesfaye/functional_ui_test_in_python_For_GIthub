import pytest
from datetime import time

from helper.agendas import AGENDA_ERROR_MSG, AGENDA_SUCCESS_MSG, new_agenda, TITLE, DESC, agenda_actions
from helper.common import URL, ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, USER_EMAIL, USER_PASSWORD, driver, generate_string
from helper.login import LOGIN_BANNER_SUCCESS_TXT, login

driver.get(URL)

def test_new_agenda_without_login():
    driver.maximize_window()
    driver.minimize_window()
    return
    agenda_actions()
    new_agenda(TITLE, DESC, AGENDA_ERROR_MSG)

@pytest.mark.parametrize("title_txt ,category_txt,desc_txt,expected_txt", [(generate_string(upper=7), "sports", "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", True),
                                                             (generate_string(upper=7), "sports", "DESCRIPTION ", False),
                                                             (generate_string(upper=7), "sports", None, False),
                                                             (generate_string(upper=7), None , "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", False),
                                                             (None, "sports", "DESCRIPTION ABOUT THE TITLE IS MENTIONED HERE", False)])
def test_new_agenda_with_login(title_txt ,category_txt,desc_txt,expected_txt):
    driver.get(URL)
    driver.close()
    return
    login(ADMIN_USER_EMAIL, ADMIN_USER_PASSWORD, LOGIN_BANNER_SUCCESS_TXT)
    time.sleep(2)
    agenda_actions()
    new_agenda(title_txt ,category_txt,desc_txt,expected_txt)



