from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Css, Xpath, Url

def test_enter_login_page_from_main_page_push_enter_account_button(main_page_driver):
    enter_account_button = main_page_driver.find_element(By.XPATH, Xpath.MainPage.enter_account_button)
    enter_account_button.click()
    WebDriverWait(main_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    main_page_driver.quit()

def test_enter_login_page_from_main_page_push_personal_account_href(main_page_driver):
    personal_account_href = main_page_driver.find_element(By.XPATH, Xpath.MainPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(main_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    main_page_driver.quit()

def test_enter_login_page_from_feed_page_push_personal_account_href(feed_page_driver):
    personal_account_href = feed_page_driver.find_element(By.XPATH, Xpath.FeedPage.personal_account_href)
    personal_account_href.click()
    WebDriverWait(feed_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    feed_page_driver.quit()

def test_enter_login_page_from_register_page_push_registration_button(register_page_driver):
    email_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.email_field)
    email_field.send_keys(f"lolkasapsula@kek.qu")
    name_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.name_field)
    name_field.send_keys(f"Emit")
    pass_field = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.pass_field)
    pass_field.send_keys(f"lolkek")

    register_button = register_page_driver.find_element(By.CSS_SELECTOR, Css.RegisterPage.registration_button)
    register_button.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    register_page_driver.quit()

def test_enter_login_page_from_register_page_push_enter_href(register_page_driver):
    enter_href = register_page_driver.find_element(By.XPATH, Xpath.RegisterPage.enter_href)
    enter_href.click()
    WebDriverWait(register_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    register_page_driver.quit()

def test_enter_login_page_from_forgot_password_page_enter_href(forgot_password_page_driver):
    enter_href = forgot_password_page_driver.find_element(By.XPATH, Xpath.ForgotPassword.enter_href)
    enter_href.click()
    WebDriverWait(forgot_password_page_driver, 3).until(expected_conditions.url_to_be(Url.login_page))
    forgot_password_page_driver.quit()