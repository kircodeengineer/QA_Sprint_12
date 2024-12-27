from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Xpath

def test_main_page_select_sauce(main_page_driver):
    not_selected_sauce = main_page_driver.find_element(By.XPATH, Xpath.MainPage.not_selected_sauce)
    not_selected_sauce.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, Xpath.MainPage.selected_sauce)))

def test_main_page_select_toppings(main_page_driver):
    not_selected_toppings = main_page_driver.find_element(By.XPATH, Xpath.MainPage.not_selected_toppings)
    not_selected_toppings.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, Xpath.MainPage.selected_toppings)))

def test_main_page_select_buns(main_page_driver):
    not_selected_sauce = main_page_driver.find_element(By.XPATH, Xpath.MainPage.not_selected_sauce)
    not_selected_sauce.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, Xpath.MainPage.selected_sauce)))
    not_selected_buns = main_page_driver.find_element(By.XPATH, Xpath.MainPage.not_selected_buns)
    not_selected_buns.click()
    WebDriverWait(main_page_driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, Xpath.MainPage.selected_buns)))
