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

class LoginLocators:
    LOGIN_BUTTON = By.XPATH, ".//form//button[contains(text(), 'Войти')]"

class MainPageLocators:
    # PROFILE_IMAGE = By.XPATH, ".//div[contains(@class, 'header')]//button[@class = 'circleSmall']
    PROFILE_IMAGE = By.CSS_SELECTOR, "button.circleSmall"
    PROFILE_NAME = By.XPATH, ".//div[contains(@class, 'header')]//h3[contains(@class, 'profileText')]"
    LOGOUT_BUTTON = By.XPATH, ".//div[contains(@class, 'header')]//button[contains(text(), 'Выйти')]"
    CREATE_LISTING_BUTTON = By.XPATH, ".//div[contains(@class, 'header')]//button[contains(text(), 'Разместить объявление')]"
    AUTH_REQUEST_TEXT = By.XPATH, ".//form[contains(@class, 'popUp')]//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]"

class CreateListingLocators:
    LISTING_NAME = By.NAME, 'name'
    LISTING_DESCRIPTION = By.XPATH, ".//div[contains(@class, 'textarea')]//textarea[@name = 'description']"
    LISTING_PRICE = By.NAME, 'price'
    
    CATEGORY_DROPDOWN = By.XPATH, ".//button[preceding-sibling::input[@name = 'category']]"
    CITY_DROPDOWN = By.XPATH, ".//button[preceding-sibling::input[@name = 'city']]"
    DROPDOWN_ITEMS = By.XPATH, ".//div[contains(@class, 'dropDownMenu_options')]//button[contains(@class, 'dropDownMenu_btn')]"
    RADIO_BUTTONS = By.XPATH, ".//input[@type = 'radio']/following-sibling::div[contains(@class, 'inputRegular')]"
    SUBMIT_BUTTON = By.XPATH, ".//button[contains(text(), 'Опубликовать')]"

class ProfileLocators:
    NEXT_PAGE_BUTTON = By.XPATH, ".//button[contains(@class, 'arrowButton--right')]"
    MY_ORDER_LAST_ITEM_NAME = By.XPATH, "//h1[text()='Мои объявления']/following-sibling::div//div[@class='card'][last()]//div[@class='about']//h2"
    MY_ORDER_LAST_ITEM_PRICE = By.XPATH, "//h1[text()='Мои объявления']/following-sibling::div//div[@class='card'][last()]//div[@class='price']//h2"