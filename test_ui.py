import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

@allure.title("Поиск продукта")
@allure.description("Проверка поиска товара на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_rus_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск товара на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        text = main_page.search_product_rus_ui('Грибы')
        assert text == "грибы"
    
@allure.title("Добавление продукта в корзину")
@allure.description("Проверка добавления товара в корзину")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_add_product_to_cart_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск товара на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        text = main_page.add_product_to_cart_ui('Грибы')  
    with allure.step("Добавление товара в корзину"):
        assert text [0:12] == "Белые грибы"

@allure.title("Удаление продукта из корзины")
@allure.description("Проверка удаления товара из корзины")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_delete_product_from_cart_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск товара на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        text = main_page.delete_product_from_cart_ui('Чай')  
    with allure.step("Удаление товара из корзины"):
        assert text == "0 ₽"
    
