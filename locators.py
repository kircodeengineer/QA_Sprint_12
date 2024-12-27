from selenium.webdriver.common.by import By

class Css:
    class RegisterPage:
        REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".button_button_size_medium__3zxIa")  # кнопка Зарегистрироваться на странице регистрации
        REGISTRATION_PASS_ERROR =  (By.CSS_SELECTOR, ".input__error.text_type_main-default") # ошибка ввода пароля при регистрации

class Xpath:
    class LoginPage:
        RECOVER_PASS_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']") # гиперссылка Восстановить пароль для перехода на страницу восстановления пароля
        REGISTRATION_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/register']")  # гиперссылка Зарегистрироваться для перехода на форму регистрации
        EMAIL_FIELD = (By.XPATH, "(.//fieldset[@class='Auth_fieldset__1QzWN mb-6'])//input[@name='name']")  # Поле ввода email
        PASS_FIELD = (By.XPATH, "(.//fieldset[@class='Auth_fieldset__1QzWN mb-6'])//input[@name='Пароль']")  # Поле ввода Имя
        ENTER_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text() ='Войти']") # кнопка Войти

    class RegisterPage:
        EMAIL_FIELD = (By.XPATH, "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[2]/input")  # Поле ввода email
        NAME_FIELD = (By.XPATH, "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[1]/input")  # Поле ввода Имя
        PASS_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле ввода Пароль
        ENTER_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/login']") # гиперссылка Войти для перехода на страницу входа в аккаунт

    class MainPage:
        ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 "
                                "button_button_type_primary__1O7Bx "
                                "button_button_size_large__G21Vg' "
                                "and "
                                "text()='Войти в аккаунт']") # кнопка Войти в аккаунт на титульной странице
        PERSONAL_ACCOUNT_HREF = (By.XPATH,".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']") # кнопка Личный кабинет для перехода на страницу входа в аккаунт
        NOT_SELECTED_BUNS = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']") # не выбран раздел Булки
        NOT_SELECTED_TOPPINGS = (By.XPATH,".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']") # не выбран раздел Начинки
        NOT_SELECTED_SAUCE = (By.XPATH,".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']") # не выбран раздел Соусы
        SELECTED_BUNS = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']") # выбран раздел Булки
        SELECTED_TOPPINGS = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']") # выбран раздел Начинки
        SELECTED_SAUCE = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']") # выбран раздел Соусы
        SELECTED_INGREDIENT = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span")

    class FeedPage:
        PERSONAL_ACCOUNT_HREF = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']") # кнопка Личный кабинет для перехода на страницу входа в аккаунт

    class ForgotPassword:
        ENTER_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/login']")  # гиперссылка Войти для перехода на страницу входа в аккаунт

    class AccountProfile:
        CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']") # кнопка Конструктор для перехода на главную страницу
        LOGO_BUTTON = (By.XPATH, "(.//*[name()='svg' and @xmlns='http://www.w3.org/2000/svg'])[1]") # кнопка Лого для перехода на главную страницу
        LOGOUT_BUTTON = (By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']") # кнопка Выход для выхода из аккаунта
