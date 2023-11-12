import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # User data
    email = 'yanqatest1322@gmail.com'
    password = '487e112e'

    # Locators
    cookie_button = '//*[@id="modal-cookie"]/div/div[2]/div/button[3]'
    # authorisation
    account_button = '//button[@class="styles_userToolsToggler__c2aHe"]'
    login_button = '//button[@data-testid="loginButton"]'
    email_field = '//input[@data-testid="login-form-email"]'
    password_field = '//input[@data-testid="login-form-password"]'
    login_submit_button = '//button[@data-testid="loginSubmit"]'
    account_name = '//span[@class="userToolsSubtitle"]'

    # Getters
    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_submit_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_submit_button)))

    def get_close_promo_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_promo_button)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.account_name)))

    # Actions
    def click_cookie_button(self):
        self.get_cookie_button().click()
        print('Click accept cache and cookies')

    def click_account_button(self):
        self.get_account_button().click()
        print('Click account button')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def input_email_field(self, login):
        self.get_email_field().send_keys(login)
        print('Input login')

    def input_password_field(self, password):
        self.get_password_field().send_keys(password)
        print('Input password')

    def click_login_submit_button(self):
        self.get_login_submit_button().click()
        print('Click login submit button')

    def user_email_value(self):
        self.get_user_email().text()

    # Methods
    def authorization(self, url):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(url)
            self.driver.maximize_window()
            self.click_cookie_button()
            self.click_account_button()
            self.click_login_button()
            self.input_email_field('yanqatest1322@gmail.com')
            self.input_password_field('487e112e')
            self.click_login_submit_button()
            self.assert_url('https://www.21vek.by/')
            time.sleep(5)
            self.click_account_button()
            self.assert_word(self.get_user_email(), 'yanqatest1322@gmail.com')
            print('Success login')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

