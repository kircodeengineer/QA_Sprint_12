import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
from locators import Xpath


def test_main_page_click_personal_account_href_enter_personal_account(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.ACCOUNT_PROFILE))
    assert logged_in_main_page_driver.current_url == url.ACCOUNT_PROFILE

def test_feed_page_click_personal_account_href_enter_personal_account(logged_in_main_page_driver):
    logged_in_main_page_driver.get(url.FEED_PAGE)
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.FEED_PAGE))
    personal_account_href = logged_in_main_page_driver.find_element(*Xpath.FeedPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.ACCOUNT_PROFILE))
    assert logged_in_main_page_driver.current_url == url.ACCOUNT_PROFILE

def test_account_profile_push_constructor_button_enter_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.ACCOUNT_PROFILE))
    constructor_button = logged_in_main_page_driver.find_element(*Xpath.AccountProfile.CONSTRUCTOR_BUTTON)
    constructor_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.MAIN_PAGE))
    assert logged_in_main_page_driver.current_url == url.MAIN_PAGE

def test_account_profile_push_logo_button_enter_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.ACCOUNT_PROFILE))
    logo_button = logged_in_main_page_driver.find_element(*Xpath.AccountProfile.LOGO_BUTTON)
    logo_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.MAIN_PAGE))
    assert logged_in_main_page_driver.current_url == url.MAIN_PAGE

def test_account_profile_push_logout_main_page(logged_in_main_page_driver):
    personal_account_href = logged_in_main_page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.ACCOUNT_PROFILE))
    logout_button = logged_in_main_page_driver.find_element(*Xpath.AccountProfile.LOGOUT_BUTTON)
    logout_button.click()
    WebDriverWait(logged_in_main_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert logged_in_main_page_driver.current_url == url.LOGIN_PAGE