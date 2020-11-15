from selenium.webdriver import ActionChains

from helper.common import driver, banner_xp, URL
from helper.login import login_xp
from helper.utils import load_prop_file
url_add_category = URL + "/addcategory"
url_categories = URL + "/categories"

categories_in_link_txt = "Category"
new_category_in_link_text = "New category"
categories_xp = load_prop_file("xpath/categories")
title_xp = categories_xp["categories"]["title"]
desc_xp = categories_xp["categories"]["desc"]
submit_xp = categories_xp["categories"]["submit"]

TITLE = "Entertainment"
DESC =  "All topics about entertainment should be discussed under this category"
CATEGORY_SUCCESS_MSG = "category has been created successfully"
CATEGORY_FAIL_MSG ="you must be admin to create category"
CATEGORY_ERROR_MSG = "login required"

def category_actions():
    action = ActionChains(driver);

    parent_level_menu = driver.find_element_by_link_text(categories_in_link_txt)
    action.move_to_element(parent_level_menu).perform()

    child_level_menu = driver.find_element_by_link_text(new_category_in_link_text)
    child_level_menu.click();


def new_category(title, desc, banner_txt):

    category_title = driver.find_element_by_xpath(title_xp)
    category_title.send_keys(title)
    category_desc = driver.find_element_by_xpath(desc_xp)
    category_desc.send_keys(desc)
    driver.find_element_by_xpath(submit_xp).click()
    assert banner_txt in driver.find_element_by_xpath(banner_xp)