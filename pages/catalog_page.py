import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):
    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_button = '//button[@class="styles_catalogButton__z9L_j"]'

    computers_category = '//a[@href="/computers/"]'
    laptops_category = '(//a[@href="/notebooks/"])[2]'

    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_computers_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.computers_category)))

    def get_laptops_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.laptops_category)))

    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Click catalog button')

    def hover_on_computers_category(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_computers_catalog()).perform()
        print('Open computers catalog')

    def click_laptops_category(self):
        self.get_laptops_category().click()
        print('Click to laptops catalog')

    # Methods
    def open_notebooks_page(self):
        with allure.step('Open notebooks page'):
            Logger.add_start_step(method='open_notebooks_page')
            self.get_current_url()
            self.click_catalog_button()
            self.hover_on_computers_category()
            self.click_laptops_category()
            time.sleep(5)
            self.assert_url('https://www.21vek.by/notebooks/')
            Logger.add_end_step(url=self.driver.current_url, method='open_notebooks_page')
