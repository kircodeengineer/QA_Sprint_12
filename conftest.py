import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Css, Xpath, Url

@pytest.fixture(scope='function')
def register_page_driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_page)

    enter_account_button = driver.find_element(By.CSS_SELECTOR, Css.TitlePage.enter_account_button)
    enter_account_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Xpath.LoginPage.registration_href)))

    register_href = driver.find_element(By.XPATH, Xpath.LoginPage.registration_href)
    register_href.click()
    return driver
