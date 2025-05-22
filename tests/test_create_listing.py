from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import MainPageLocators, CreateListingLocators, ProfileLocators
import data
import random


class TestCreateListing:
    def test_create_listing_without_authorization(self, driver):
        driver.get(data.MAIN_URL)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.CREATE_LISTING_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_LISTING_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(MainPageLocators.AUTH_REQUEST_TEXT))
        auth_request_text = driver.find_element(*MainPageLocators.AUTH_REQUEST_TEXT).text

        assert auth_request_text == data.AUTH_REQUEST_TEXT
    
    def test_place_new_ad_show_in_my_ads(self, login_user):
        WebDriverWait(login_user, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.CREATE_LISTING_BUTTON))
        login_user.find_element(*MainPageLocators.CREATE_LISTING_BUTTON).click()

        WebDriverWait(login_user, 3).until(expected_conditions.url_to_be(data.CREATE_AD_URL))

        random_listing_number = random.randint(100,999)
        random_listing_price = random.randint(10000, 1000000)
        listing_name = f'Гараж {random_listing_number}'
        listing_description = f'Продам гараж {random_listing_number}'
        
        login_user.find_element(*CreateListingLocators.LISTING_NAME).send_keys(listing_name)
        login_user.find_element(*CreateListingLocators.LISTING_DESCRIPTION).send_keys(listing_description)
        login_user.find_element(*CreateListingLocators.LISTING_PRICE).send_keys(random_listing_price)

        login_user.find_element(*CreateListingLocators.CATEGORY_DROPDOWN).click()
        WebDriverWait(login_user, 3).until(expected_conditions.visibility_of_element_located(CreateListingLocators.CATEGORY_DROPDOWN))
        category = login_user.find_elements(*CreateListingLocators.DROPDOWN_ITEMS)
        category[random.randint(1, len(category)-1)].click()
        
        login_user.find_element(*CreateListingLocators.CITY_DROPDOWN).click()
        WebDriverWait(login_user, 3).until(expected_conditions.visibility_of_element_located(CreateListingLocators.CATEGORY_DROPDOWN))
        city = login_user.find_elements(*CreateListingLocators.DROPDOWN_ITEMS)
        city[random.randint(1, len(category)-1)].click()
        
        login_user.find_element(*CreateListingLocators.RADIO_BUTTONS).click()

        WebDriverWait(login_user, 3).until(expected_conditions.element_to_be_clickable(CreateListingLocators.SUBMIT_BUTTON))
        login_user.find_element(*CreateListingLocators.SUBMIT_BUTTON).click()

        WebDriverWait(login_user, 3).until(expected_conditions.url_to_be(data.MAIN_URL))

        WebDriverWait(login_user, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.PROFILE_IMAGE))
        login_user.find_element(*MainPageLocators.PROFILE_IMAGE).click()

        WebDriverWait(login_user, 3).until(expected_conditions.url_to_be(data.PROFILE_URL))

        while True: 
            try:
                button = WebDriverWait(login_user, 3).until(
                    expected_conditions.element_to_be_clickable((ProfileLocators.NEXT_PAGE_BUTTON)
                ))
                button.click()
            except:
                break

        last_order_name = login_user.find_element(*ProfileLocators.MY_ORDER_LAST_ITEM_NAME).text
        last_order_price = login_user.find_element(*ProfileLocators.MY_ORDER_LAST_ITEM_PRICE).text

        assert last_order_name == listing_name
        assert int(last_order_price.replace('₽', '').replace(' ', '')) == random_listing_price
