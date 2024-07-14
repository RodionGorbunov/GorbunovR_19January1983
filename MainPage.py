import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://altaivita.ru/")
        self._driver.implicitly_wait(10)
        
    with allure.step("Поиск продукта"):
        def search_product_rus_ui(self, term):
            self._driver.find_element(By.CSS_SELECTOR, ".searchpro__field-input").send_keys(term)
            self._driver.find_element(By.CSS_SELECTOR, "div.header__search:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()
            txt = self._driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/ul/li[2]/a').text
            return txt
            
    with allure.step("Добавление продукта в корзину"):
        def add_product_to_cart_ui(self, term):
            self._driver.find_element(By.CSS_SELECTOR, ".searchpro__field-input").send_keys(term)
            self._driver.find_element(By.CSS_SELECTOR, "div.header__search:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()   
            self._driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[4]/div[1]/div[1]/div/div[4]/div/div[2]/div[1]/button/span").click()
            self._driver.get("https://altaivita.ru/cart")
            txt = self._driver.find_element(By.CSS_SELECTOR, ".basket__name").text
            return txt

    with allure.step("Удаление продукта из корзины"):
        def delete_product_from_cart_ui(self, term):
            self._driver.find_element(By.CSS_SELECTOR, ".searchpro__field-input").send_keys(term)
            self._driver.find_element(By.CSS_SELECTOR, "div.header__search:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()   
            self._driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[4]/div[1]/div[1]/div/div[4]/div/div[2]/div[1]/button/span").click()
            self._driver.get("https://altaivita.ru/cart")
            self._driver.find_element(By. CSS_SELECTOR, ".basket__delete > button:nth-child(1) > i:nth-child(1)").click()
            txt = self._driver.find_element(By.CSS_SELECTOR, "span.sum:nth-child(7) > span:nth-child(1)").text
            return txt

    with allure.step("Закрытие веб-браузера"):
        def close_driver(self):
            self._driver.quit()
    
