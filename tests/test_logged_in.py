import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Xpath, Url

def test_main_page_click_personal_account_href_enter_personal_account(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(By.XPATH, Xpath.MainPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.account_profile))

def test_feed_page_click_personal_account_href_enter_personal_account(logged_in_main_page_driver):
    logged_in_main_page_driver.get(Url.feed_page)
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.feed_page))
    personal_account_href = logged_in_main_page_driver.find_element(By.XPATH, Xpath.FeedPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.account_profile))

def test_account_profile_push_constructor_button_enter_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(By.XPATH, Xpath.MainPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.account_profile))
    constructor_button = logged_in_main_page_driver.find_element(By.XPATH, Xpath.AccountProfile.constructor_button)
    constructor_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.main_page))

def test_account_profile_push_logo_button_enter_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(By.XPATH, Xpath.MainPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.account_profile))
    logo_button = logged_in_main_page_driver.find_element(By.XPATH, Xpath.AccountProfile.logo_button)
    logo_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.main_page))

def test_account_profile_push_logout_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(By.XPATH, Xpath.MainPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.account_profile))
    logout_button = logged_in_main_page_driver.find_element(By.XPATH, Xpath.AccountProfile.logout_button)
    logout_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))