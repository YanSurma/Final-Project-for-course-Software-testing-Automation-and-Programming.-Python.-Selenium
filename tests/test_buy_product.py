import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.basket_page import Basket_page
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.notebooks_page import Notebooks_page


@allure.description("Test buy product 1")
def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('S:\\Projects_1\\main_project\\driver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    url = 'https://www.21vek.by/'

    login = Main_page(driver)
    login.authorization(url)

    cat = Catalog_page(driver)
    cat.open_notebooks_page()

    np = Notebooks_page(driver)
    np.select_notebook_product()

    bs = Basket_page(driver)
    bs.confirm_product_order()

    driver.close()
