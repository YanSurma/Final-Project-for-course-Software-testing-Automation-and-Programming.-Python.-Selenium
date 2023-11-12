import time

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Notebooks_page(Base):
    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # A testing Locators
    min_price = '//input[@id="minPrice"]'
    max_price = '//input[@id="maxPrice"]'

    asus_producer = '//button[@data-testid="producer-asus"]'

    filter_button = '//button[@data-testid="apply-products-filters"]'
    add_product = '(//button[@data-testid="in-basket-button"])[1]'

    # A testing Getters
    def get_add_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_product)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_filter_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_asus_producer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.asus_producer)))

    # A testing Actions
    def input_min_price(self, min_price_value):
        self.get_min_price().send_keys(min_price_value)
        print(f'Input min price {min_price_value}')

    def input_max_price(self, max_price_value):
        self.get_max_price().send_keys(max_price_value)
        print(f'Input max price {max_price_value}')

    def click_add_product(self):
        self.get_add_product().click()
        print('Click add product button')

    def click_filter_button(self):
        self.get_filter_button().click()
        print('Apply filters')

    def click_asus_producer(self):
        self.get_asus_producer().click()
        print('Select asus producer')

    # A testing Actions
    def a_select_notebook_product(self):
        with allure.step('Select notebook_product'):
            Logger.add_start_step(method='select_notebook_product')
            self.get_current_url()
            time.sleep(5)
            self.assert_url('https://www.21vek.by/notebooks/')
            self.input_min_price('3000')
            self.input_max_price('4000')
            self.click_asus_producer()
            self.click_filter_button()
            self.click_add_product()
            Logger.add_end_step(url=self.driver.current_url, method='select_notebook_product')

    # B testing Locators
    price_from = '//input[@name="filter[price][from]"]'
    price_to = '//input[@name="filter[price][to]"]'
    b_asus_producer = '//label[@title="Asus"]'
    b_filter_button = '//button[@class="filter-controls__submit filter__button g-button"]'
    b_add_to_cart = '(//button[@data-ga_action="add_to_cart"])[1]'
    checker = '//span[@class="b-filter-help__text"]'

    # B testing Getters
    def get_checker(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checker)))

    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_to)))

    def get_b_asus_producer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.b_asus_producer)))

    def get_b_filter_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.b_filter_button)))

    def get_b_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.b_add_to_cart)))

    # B testing Actions
    def input_price_from(self, price_from_value):
        self.get_price_from().send_keys(price_from_value)
        print('Input price from')

    def input_price_to(self, price_to_value):
        self.get_price_to().send_keys(price_to_value)
        print('Input price to')

    def select_b_asus_producer(self):
        self.get_b_asus_producer().click()
        print('Select asus producer')

    def click_b_filter_button(self):
        self.get_b_filter_button().click()
        print('Click apply filter button')

    def click_b_add_to_cart(self):
        self.get_b_add_to_cart().click()

    # B testing Methods
    def b_select_notebook_product(self):
        with allure.step('Select notebook_product'):
            Logger.add_start_step(method='b_select_notebook_product')
            self.get_current_url()
            time.sleep(5)
            self.assert_url('https://www.21vek.by/notebooks/')
            self.input_price_from('3000')
            self.input_price_to('4000')
            self.select_b_asus_producer()
            self.click_b_filter_button()
            self.click_b_add_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='b_select_notebook_product')

    def select_notebook_product(self):
        try:
            self.get_checker()
            print('B Testing page opens, run B method')
            self.b_select_notebook_product()
        except TimeoutException:
            self.a_select_notebook_product()
            print('A testing page open, run A method')
