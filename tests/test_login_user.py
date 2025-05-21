from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import RegisterLocators, LoginLocators, MainPageLocators
import data

class TestLogin:
    def test_login_user_opens_main_page(self, driver):
        driver.get(data.MAIN_URL)

        driver.find_element(*RegisterLocators.ENTRY_OR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginLocators.LOGIN_BUTTON))

        driver.find_element(*RegisterLocators.ENTER_EMAIL).send_keys(data.EXIST_USER_EMAIL)
        driver.find_element(*RegisterLocators.ENTER_PASSWORD).send_keys(data.DEFAULT_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPageLocators.PROFILE_IMAGE))
        user_name = driver.find_element(*MainPageLocators.PROFILE_NAME).text
        assert user_name == 'User.'

    def test_logout_shows_login_or_register_button(self, login_user):
        WebDriverWait(login_user, 3).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON))

        login_user.find_element(*MainPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(login_user, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.ENTRY_OR_REGISTER_BUTTON))

        profile_image = login_user.find_elements(*MainPageLocators.PROFILE_IMAGE)
        profile_name = login_user.find_elements(*MainPageLocators.PROFILE_NAME)

        assert not profile_image
        assert not profile_name

