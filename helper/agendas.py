from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from helper.common import driver, banner_xp
from helper.utils import load_xpath

agendas_in_link_txt = "Agenda"
new_agenda_in_link_text = "New agenda"
agendas_xp = load_xpath("agendas")
title_xp = agendas_xp["agendas"]["title"]
category_xp = agendas_xp["agendas"]["category"]
desc_xp = agendas_xp["agendas"]["desc"]
submit_xp = agendas_xp["agendas"]["submit"]


TITLE = "Entertainment"
category = "sports"
DESC =  "All topics about entertainment should be discussed here"
AGENDA_SUCCESS_MSG = "posted successfully"
AGENDA_ERROR_MSG = "login required"

def agenda_actions():
    action = ActionChains(driver);

    parent_level_menu = driver.find_element_by_link_text(agendas_in_link_txt)
    action.move_to_element(parent_level_menu).perform()

    child_level_menu = driver.find_element_by_link_text(new_agenda_in_link_text)
    child_level_menu.click();

def category_select(category):
    select = Select(driver.find_element_by_xpath(category_xp))
    select.select_by_visible_text(category)

def new_agenda(title, desc, expected=True):
        category_title = driver.find_element_by_xpath(title_xp)
        category_title.send_keys(title)
        category_select()
        category_desc = driver.find_element_by_xpath(desc_xp)
        category_desc.send_keys(desc)
        driver.find_element_by_xpath(submit_xp).click()
        if expected:
            assert expected in driver.find_element_by_xpath(banner_xp)
        else:
            pass
