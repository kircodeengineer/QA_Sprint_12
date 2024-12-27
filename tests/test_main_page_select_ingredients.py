import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
import locators


@pytest.mark.parametrize("page_driver", [url.MAIN_PAGE], indirect=True)
def test_main_page_select_sauce(page_driver):
    not_selected_sauce = page_driver.find_element(*locators.MainPage.NOT_SELECTED_SAUCE)
    not_selected_sauce.click()
    WebDriverWait(page_driver, 3).until(
        expected_conditions.presence_of_element_located(locators.MainPage.SELECTED_SAUCE))
    selected_ingredient = page_driver.find_element(*locators.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Соусы"

@pytest.mark.parametrize("page_driver", [url.MAIN_PAGE], indirect=True)
def test_main_page_select_toppings(page_driver):
    not_selected_toppings = page_driver.find_element(*locators.MainPage.NOT_SELECTED_TOPPINGS)
    not_selected_toppings.click()
    WebDriverWait(page_driver, 3).until(
        expected_conditions.presence_of_element_located(locators.MainPage.SELECTED_TOPPINGS))
    selected_ingredient = page_driver.find_element(*locators.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Начинки"

@pytest.mark.parametrize("page_driver", [url.MAIN_PAGE], indirect=True)
def test_main_page_select_buns(page_driver):
    not_selected_sauce = page_driver.find_element(*locators.MainPage.NOT_SELECTED_SAUCE)
    not_selected_sauce.click()
    WebDriverWait(page_driver, 3).until(
        expected_conditions.presence_of_element_located(locators.MainPage.SELECTED_SAUCE))
    not_selected_buns = page_driver.find_element(*locators.MainPage.NOT_SELECTED_BUNS)
    not_selected_buns.click()
    WebDriverWait(page_driver, 3).until(
        expected_conditions.presence_of_element_located(locators.MainPage.SELECTED_BUNS))
    selected_ingredient = page_driver.find_element(*locators.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Булки"
