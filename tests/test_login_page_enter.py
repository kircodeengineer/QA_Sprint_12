from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
from locators import Css, Xpath
from account_profile_data_generator import RandomAccountProfileData


def test_enter_login_page_from_main_page_push_enter_account_button(main_page_driver):
    enter_account_button = main_page_driver.find_element(*Xpath.MainPage.ENTER_ACCOUNT_BUTTON)
    enter_account_button.click()
    WebDriverWait(main_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert main_page_driver.current_url == url.LOGIN_PAGE

def test_enter_login_page_from_main_page_push_personal_account_href(main_page_driver):
    personal_account_href = main_page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(main_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert main_page_driver.current_url == url.LOGIN_PAGE

def test_enter_login_page_from_feed_page_push_personal_account_href(feed_page_driver):
    personal_account_href = feed_page_driver.find_element(*Xpath.FeedPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(feed_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert feed_page_driver.current_url == url.LOGIN_PAGE

def test_enter_login_page_from_register_page_push_registration_button(register_page_driver):
    email_field = register_page_driver.find_element(*Xpath.RegisterPage.EMAIL_FIELD)
    email_field.send_keys(RandomAccountProfileData.get_email())
    name_field = register_page_driver.find_element(*Xpath.RegisterPage.NAME_FIELD)
    name_field.send_keys(RandomAccountProfileData.get_name())
    pass_field = register_page_driver.find_element(*Xpath.RegisterPage.PASS_FIELD)
    pass_field.send_keys(RandomAccountProfileData.get_pass())

    register_button = register_page_driver.find_element(*Css.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert register_page_driver.current_url == url.LOGIN_PAGE

def test_enter_login_page_from_register_page_push_enter_href(register_page_driver):
    enter_href = register_page_driver.find_element(*Xpath.RegisterPage.ENTER_HREF)
    enter_href.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert register_page_driver.current_url == url.LOGIN_PAGE

def test_enter_login_page_from_forgot_password_page_enter_href(forgot_password_page_driver):
    enter_href = forgot_password_page_driver.find_element(*Xpath.ForgotPassword.ENTER_HREF)
    enter_href.click()
    WebDriverWait(forgot_password_page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert forgot_password_page_driver.current_url == url.LOGIN_PAGE
