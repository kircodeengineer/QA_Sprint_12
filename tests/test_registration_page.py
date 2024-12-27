from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
from locators import Css, Xpath
from account_profile_data_generator import RandomAccountProfileData


def test_registration_page_enter_valid_input_data(register_page_driver):
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

def test_registration_page_enter_bad_password_get_error(register_page_driver):
    pass_field = register_page_driver.find_element(*Xpath.RegisterPage.PASS_FIELD)
    pass_field.send_keys(f"123")

    register_button = register_page_driver.find_element(*Css.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.presence_of_element_located(Css.RegisterPage.REGISTRATION_PASS_ERROR))
    input_error = register_page_driver.find_element(*Css.RegisterPage.REGISTRATION_PASS_ERROR)

    assert input_error.text == 'Некорректный пароль'