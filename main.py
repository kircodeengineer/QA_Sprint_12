import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

enter_account_button = driver.find_element(By.CSS_SELECTOR , ".button_button_size_large__G21Vg")
enter_account_button.click()


#register_href = driver.find_element(By.CLASS_NAME , "Auth_link__1fOlj")
registration_href = "Auth_link__1fOlj" # гиперссылка Зарегистрироваться для перехода на форму регистрации
register_href.click()

name_field = driver.find_element(By.XPATH, "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[2]/input")
name_field.send_keys("123")

pass_field_xpath = ".//input[@type='password' and @name='Пароль']"
pass_field = driver.find_element(By.XPATH , pass_field_xpath)
pass_field.send_keys("123")

register_button = driver.find_element(By.CSS_SELECTOR , ".button_button_size_medium__3zxIa")
register_button.click()

input_error = driver.find_element(By.CSS_SELECTOR , ".input__error.text_type_main-default")
assert input_error.text == 'Некорректный пароль'

time.sleep(5)
driver.quit()