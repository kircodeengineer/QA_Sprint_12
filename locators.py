class Css:
    class RegisterPage:
        registration_button = ".button_button_size_medium__3zxIa"  # кнопка Зарегистрироваться на странице регистрации
        registration_pass_error =  ".input__error.text_type_main-default" # ошибка ввода пароля при регистрации
    class TitlePage:
        enter_account_button = ".button_button_size_large__G21Vg" # кнопка Войти в аккаунт на титульной странице
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