import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Css, Xpath, Url

@pytest.fixture(scope='function')
def feed_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.feed_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.feed_page))
    return driver

@pytest.fixture(scope='function')
def forgot_password_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.forgot_password_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.forgot_password_page))
    return driver

@pytest.fixture(scope='function')
def login_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.login_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    return driver

@pytest.fixture(scope='function')
def main_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.main_page))
    return driver

@pytest.fixture(scope='function')
def register_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.register_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Url.register_page))
    return driver



