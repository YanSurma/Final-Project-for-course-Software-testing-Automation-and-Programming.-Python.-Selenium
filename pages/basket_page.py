import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Basket_page(Base):
    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.product_name_value = None
        self.driver = driver

    # Locators
    confirm_order = '//button[@data-testid="basketConfirmation"]'
    basket_button = '//a[@class="headerCartBox"]'

    # Getters
    def get_confirm_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_order)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    # Actions
    def click_confirm_order(self):
        self.get_confirm_order().click()
        print('Click confirm order')

    def click_basket_button(self):
        self.get_basket_button().click()
        print('Open basket')

    # Methods
    def confirm_product_order(self):
        with allure.step('Confirm product order'):
            Logger.add_start_step(method='confirm_product_order')
            self.click_basket_button()
            self.get_current_url()
            time.sleep(5)
            self.click_confirm_order()
            time.sleep(5)
            self.assert_url('https://www.21vek.by/order/?step=delivery')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='confirm_product_order')
