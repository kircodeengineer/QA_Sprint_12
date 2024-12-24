class Css:
    class RegisterPage:
        registration_button = ".button_button_size_medium__3zxIa"  # кнопка Зарегистрироваться на странице регистрации
        registration_pass_error =  ".input__error.text_type_main-default" # ошибка ввода пароля при регистрации
    class LoginPage:
        enter_button = ".button_button_size_medium__3zxIa" # кнопка Войти на странице входа в аккаунт

class Xpath:
    class LoginPage:
        recover_pass_href = ".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']" # гиперссылка Восстановить пароль для перехода на страницу восстановления пароля
        registration_href = ".//a[@class='Auth_link__1fOlj' and @href='/register']"  # гиперссылка Зарегистрироваться для перехода на форму регистрации

    class RegisterPage:
        email_field = "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[2]/input"  # Поле ввода email
        name_field = "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[1]/input"  # Поле ввода Имя
        pass_field = ".//input[@type='password' and @name='Пароль']"  # Поле ввода Пароль
        enter_href = ".//a[@class='Auth_link__1fOlj' and @href='/login']" # гиперссылка Войти для перехода на страницу входа в аккаунт

    class MainPage:
        enter_account_button = (".//button[@class='button_button__33qZ0 "
                                "button_button_type_primary__1O7Bx "
                                "button_button_size_large__G21Vg' "
                                "and "
                                "text()='Войти в аккаунт']") # кнопка Войти в аккаунт на титульной странице
        personal_account_href = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']" # кнопка Личный кабинет для перехода на страницу входа в аккаунт
        not_selected_buns = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']"
        not_selected_toppings = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']"
        not_selected_sauce = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']"
        selected_buns = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']"
        selected_toppings = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']"
        selected_sauce = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']"

    class FeedPage:
        personal_account_href = ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']" # кнопка Личный кабинет для перехода на страницу входа в аккаунт
    class ForgotPassword:
        enter_href = ".//a[@class='Auth_link__1fOlj' and @href='/login']"  # гиперссылка Войти для перехода на страницу входа в аккаунт

class Url:
    main_page = "https://stellarburgers.nomoreparties.site/"
    feed_page = f"{main_page}feed"
    forgot_password_page = f"{main_page}forgot-password"
    login_page = f"{main_page}login"
    register_page = f"{main_page}register"
