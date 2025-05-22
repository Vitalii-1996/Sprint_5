from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import RegisterLocators, MainPageLocators
import data
import random


class TestRegister:
    def test_register_new_user_shows_user_and_profile_image(self, driver):
        driver.get(data.MAIN_URL)

        driver.find_element(*RegisterLocators.ENTRY_OR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterLocators.NO_ACCOUNT_BUTTON))

        driver.find_element(*RegisterLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.REGISTER_BUTTON))

        email = f'RegisterUserTest{random.randint(100,999)}@test.com'
        driver.find_element(*RegisterLocators.ENTER_EMAIL).send_keys(email)

        driver.find_element(*RegisterLocators.ENTER_PASSWORD).send_keys(data.DEFAULT_PASSWORD)
        driver.find_element(*RegisterLocators.SUBMIT_PASSWORD).send_keys(data.DEFAULT_PASSWORD)
        driver.find_element(*RegisterLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPageLocators.PROFILE_IMAGE))

        user_name = driver.find_element(*MainPageLocators.PROFILE_NAME).text
        assert user_name == 'User.'

    def test_register_new_user_with_wrong_email_mask(self, driver):
        driver.get(data.MAIN_URL)

        driver.find_element(*RegisterLocators.ENTRY_OR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterLocators.NO_ACCOUNT_BUTTON))

        driver.find_element(*RegisterLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.REGISTER_BUTTON))

        driver.find_element(*RegisterLocators.ENTER_EMAIL).send_keys(data.WRONG_EMAIL_MASK)

        driver.find_element(*RegisterLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.EMAIL_ERROR_TEXT))

        email_input_field_style = driver.find_element(*RegisterLocators.EMAIL_INPUT_FIELD).value_of_css_property('border')
        password_input_field_style = driver.find_element(*RegisterLocators.PASSWORD_INPUT_FIELD).value_of_css_property('border')
        submit_password_input_field_style = driver.find_element(*RegisterLocators.SUBMIT_PASSWORD_INPUT_FIELD).value_of_css_property('border')
        
        assert data.RED_BORDER_COLOR in email_input_field_style
        assert data.RED_BORDER_COLOR in password_input_field_style
        assert data.RED_BORDER_COLOR in submit_password_input_field_style

    def test_register_existing_user_fails(self, driver):
        driver.get(data.MAIN_URL)

        driver.find_element(*RegisterLocators.ENTRY_OR_REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterLocators.NO_ACCOUNT_BUTTON))

        driver.find_element(*RegisterLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.REGISTER_BUTTON))

        driver.find_element(*RegisterLocators.ENTER_EMAIL).send_keys(data.EXIST_USER_EMAIL)
        driver.find_element(*RegisterLocators.ENTER_PASSWORD).send_keys(data.DEFAULT_PASSWORD)
        driver.find_element(*RegisterLocators.SUBMIT_PASSWORD).send_keys(data.DEFAULT_PASSWORD)

        driver.find_element(*RegisterLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(RegisterLocators.EMAIL_ERROR_TEXT))

        email_input_field_style = driver.find_element(*RegisterLocators.EMAIL_INPUT_FIELD).value_of_css_property('border')
        password_input_field_style = driver.find_element(*RegisterLocators.PASSWORD_INPUT_FIELD).value_of_css_property('border')
        submit_password_input_field_style = driver.find_element(*RegisterLocators.SUBMIT_PASSWORD_INPUT_FIELD).value_of_css_property('border')
        
        assert data.RED_BORDER_COLOR in email_input_field_style
        assert data.RED_BORDER_COLOR in password_input_field_style
        assert data.RED_BORDER_COLOR in submit_password_input_field_style
