from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Xpath

def test_main_page_select_sauce(main_page_driver):
    not_selected_sauce = main_page_driver.find_element(*Xpath.MainPage.NOT_SELECTED_SAUCE)
    not_selected_sauce.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located(Xpath.MainPage.SELECTED_SAUCE))
    selected_ingredient = main_page_driver.find_element(*Xpath.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Соусы"

def test_main_page_select_toppings(main_page_driver):
    not_selected_toppings = main_page_driver.find_element(*Xpath.MainPage.NOT_SELECTED_TOPPINGS)
    not_selected_toppings.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located(Xpath.MainPage.SELECTED_TOPPINGS))
    selected_ingredient = main_page_driver.find_element(*Xpath.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Начинки"

def test_main_page_select_buns(main_page_driver):
    not_selected_sauce = main_page_driver.find_element(*Xpath.MainPage.NOT_SELECTED_SAUCE)
    not_selected_sauce.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located(Xpath.MainPage.SELECTED_SAUCE))
    not_selected_buns = main_page_driver.find_element(*Xpath.MainPage.NOT_SELECTED_BUNS)
    not_selected_buns.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located(Xpath.MainPage.SELECTED_BUNS))
    selected_ingredient = main_page_driver.find_element(*Xpath.MainPage.SELECTED_INGREDIENT)
    assert selected_ingredient.text == "Булки"
