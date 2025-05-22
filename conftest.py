from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import RegisterLocators, LoginLocators, MainPageLocators
import data
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
    driver.get(data.MAIN_URL)

    driver.find_element(*RegisterLocators.ENTRY_OR_REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginLocators.LOGIN_BUTTON))

    driver.find_element(*RegisterLocators.ENTER_EMAIL).send_keys(data.EXIST_USER_EMAIL)
    driver.find_element(*RegisterLocators.ENTER_PASSWORD).send_keys(data.DEFAULT_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON))
    return driver