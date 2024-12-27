import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url
import locators
from account_profile_data_generator import RandomAccountProfileData


@pytest.mark.parametrize("page_driver", [url.REGISTER_PAGE], indirect=True)
def test_registration_page_enter_valid_input_data(page_driver):
    email_field = page_driver.find_element(*locators.RegisterPage.EMAIL_FIELD)
    email_field.send_keys(RandomAccountProfileData.get_email())
    name_field = page_driver.find_element(*locators.RegisterPage.NAME_FIELD)
    name_field.send_keys(RandomAccountProfileData.get_name())
    pass_field = page_driver.find_element(*locators.RegisterPage.PASS_FIELD)
    pass_field.send_keys(RandomAccountProfileData.get_pass())

    register_button = page_driver.find_element(*locators.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()

    WebDriverWait(page_driver, 3).until(expected_conditions.url_to_be(url.LOGIN_PAGE))
    assert page_driver.current_url == url.LOGIN_PAGE

@pytest.mark.parametrize("page_driver", [url.REGISTER_PAGE], indirect=True)
def test_registration_page_enter_bad_password_get_error(page_driver):
    pass_field = page_driver.find_element(*locators.RegisterPage.PASS_FIELD)
    pass_field.send_keys(f"123")

    register_button = page_driver.find_element(*locators.RegisterPage.REGISTRATION_BUTTON)
    register_button.click()
    WebDriverWait(page_driver, 3).until(expected_conditions.presence_of_element_located(locators.RegisterPage.REGISTRATION_PASS_ERROR))
    input_error = page_driver.find_element(*locators.RegisterPage.REGISTRATION_PASS_ERROR)

    assert input_error.text == 'Некорректный пароль'