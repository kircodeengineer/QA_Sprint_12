from locators import Css, Xpath, Url

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_valid_input_data(register_page_driver):
    email_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.email_field)
    email_field.send_keys(f"lolkasapsr@kek.qu")
    name_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.name_field)
    name_field.send_keys(f"Emit")
    pass_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.pass_field)
    pass_field.send_keys(f"lolkek")

    register_button = register_page_driver.find_element(By.CSS_SELECTOR, Css.RegisterPage.registration_button)
    register_button.click()

    WebDriverWait(register_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    register_page_driver.quit()

def test_bad_password_error(register_page_driver):
    pass_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.pass_field)
    pass_field.send_keys(f"123")

    register_button = register_page_driver.find_element(By.CSS_SELECTOR, Css.RegisterPage.registration_button)
    register_button.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, Css.RegisterPage.registration_pass_error)))
    input_error = register_page_driver.find_element(By.CSS_SELECTOR, Css.RegisterPage.registration_pass_error)

    assert input_error.text == 'Некорректный пароль'

    register_page_driver.quit()