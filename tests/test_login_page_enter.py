import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
from locators import Css, Xpath
from account_profile_data_generator import RandomAccountProfileData

@pytest.mark.parametrize("page_driver", [url.MAIN_PAGE], indirect=True)
def test_enter_login_page_from_main_page_push_enter_account_button(page_driver):
    enter_account_button = page_driver.find_element(*Xpath.MainPage.ENTER_ACCOUNT_BUTTON)
    enter_account_button.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.MAIN_PAGE], indirect=True)
def test_enter_login_page_from_main_page_push_personal_account_href(page_driver):
    personal_account_href = page_driver.find_element(*Xpath.MainPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.FEED_PAGE], indirect=True)
def test_enter_login_page_from_feed_page_push_personal_account_href(page_driver):
    personal_account_href = page_driver.find_element(*Xpath.FeedPage.PERSONAL_ACCOUNT_HREF)
    personal_account_href.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.REGISTER_PAGE], indirect=True)
def test_enter_login_page_from_register_page_push_registration_button(page_driver):
    email_field = page_driver.find_element(*Xpath.RegisterPage.EMAIL_FIELD)
    email_field.send_keys(RandomAccountProfileData.get_email())
    name_field = page_driver.find_element(*Xpath.RegisterPage.NAME_FIELD)
    name_field.send_keys(RandomAccountProfileData.get_name())
    pass_field = page_driver.find_element(*Xpath.RegisterPage.PASS_FIELD)
    pass_field.send_keys(RandomAccountProfileData.get_pass())

    register_button = page_driver.find_element(*Css.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.REGISTER_PAGE], indirect=True)
def test_enter_login_page_from_register_page_push_enter_href(page_driver):
    enter_href = page_driver.find_element(*Xpath.RegisterPage.ENTER_HREF)
    enter_href.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.FORGOT_PASSWORD_PAGE], indirect=True)
def test_enter_login_page_from_forgot_password_page_enter_href(page_driver):
    enter_href = page_driver.find_element(*Xpath.ForgotPassword.ENTER_HREF)
    enter_href.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE
