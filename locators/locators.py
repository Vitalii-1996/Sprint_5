from selenium.webdriver.common.by import By

class RegisterLocators:
    ENTRY_OR_REGISTER_BUTTON = By.XPATH, ".//button[contains(text(), 'Вход и регистрация')]"
    NO_ACCOUNT_BUTTON = By.XPATH, ".//form//button[contains(text(), 'Нет аккаунта')]"
    REGISTER_BUTTON = By.XPATH, ".//form//h1[contains(text(), 'Зарегистрироваться')]"
    CREATE_ACCOUNT_BUTTON = By.XPATH, ".//form//button[contains(text(), 'Создать аккаунт')]"

    #ERRORS
    EMAIL_ERROR_TEXT = By.XPATH, ".//span[contains(@class, 'input_span') and contains(text(), 'Ошибка')]"
    EMAIL_INPUT_FIELD = By.XPATH, ".//input[@name = 'email']/parent::div"
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name = 'password']/parent::div"
    SUBMIT_PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name = 'submitPassword']/parent::div"

    #INPUTS
    ENTER_EMAIL = By.NAME, 'email'
    ENTER_PASSWORD = By.NAME, 'password'
    SUBMIT_PASSWORD = By.NAME, 'submitPassword'

class MainPageLocators:
    PROFILE_IMAGE = By.XPATH, ".//div[contains(@class, 'header')]//button[@class = 'circleSmall']"
    PROFILE_NAME = By.XPATH, ".//div[contains(@class, 'header')]//h3[contains(@class, 'profileText')]"
    LOGOUT_BUTTON = By.XPATH, ".//div[contains(@class, 'header')]//button[contains(text(), 'Выйти')]"