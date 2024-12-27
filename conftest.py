import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from account_profile_data_generator import RandomAccountProfileData
from locators import Css, Xpath, Url

@pytest.fixture(scope='function')
def feed_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.feed_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.feed_page))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def forgot_password_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.forgot_password_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.forgot_password_page))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.login_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.main_page))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def logged_in_main_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.register_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.register_page))

    email_field = driver.find_element(By.XPATH, Xpath.RegisterPage.email_field)
    email = RandomAccountProfileData.get_email()
    email_field.send_keys(email)
    name_field = driver.find_element(By.XPATH, Xpath.RegisterPage.name_field)
    name = RandomAccountProfileData.get_name()
    name_field.send_keys(name)
    pass_field = driver.find_element(By.XPATH, Xpath.RegisterPage.pass_field)
    password = RandomAccountProfileData.get_pass()
    pass_field.send_keys(password)

    register_button = driver.find_element(By.CSS_SELECTOR, Css.RegisterPage.registration_button)
    register_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    email_field = driver.find_element(By.XPATH, Xpath.LoginPage.email_field)
    email_field.send_keys(email)
    pass_field = driver.find_element(By.XPATH, Xpath.LoginPage.pass_field)
    pass_field.send_keys(password)
    enter_button = driver.find_element(By.XPATH, Xpath.LoginPage.enter_button)
    enter_button.click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.main_page))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def register_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.register_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.register_page))
    yield driver
    driver.quit()



