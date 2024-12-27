import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from account_profile_data_generator import RandomAccountProfileData
from locators import Css, Xpath
import url


@pytest.fixture(scope='function')
def page_driver(request):
    driver = webdriver.Chrome()
    current_url = request.param
    driver.get(current_url)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(current_url))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def logged_in_main_page_driver():
    driver = webdriver.Chrome()
    driver.get(url.REGISTER_PAGE)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(url.REGISTER_PAGE))
    email_field = driver.find_element(*Xpath.RegisterPage.EMAIL_FIELD)
    email = RandomAccountProfileData.get_email()
    email_field.send_keys(email)
    name_field = driver.find_element(*Xpath.RegisterPage.NAME_FIELD)
    name = RandomAccountProfileData.get_name()
    name_field.send_keys(name)
    pass_field = driver.find_element(*Xpath.RegisterPage.PASS_FIELD)
    password = RandomAccountProfileData.get_pass()
    pass_field.send_keys(password)

    register_button = driver.find_element(*Css.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    email_field = driver.find_element(*Xpath.LoginPage.EMAIL_FIELD)
    email_field.send_keys(email)
    pass_field = driver.find_element(*Xpath.LoginPage.PASS_FIELD)
    pass_field.send_keys(password)
    enter_button = driver.find_element(*Xpath.LoginPage.ENTER_BUTTON)
    enter_button.click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(url.MAIN_PAGE))
    yield driver
    driver.quit()

