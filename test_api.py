import requests
import allure
import pytest

Base_url = "https://altaivita.ru/engine/cart"
Product_ID = 5883

@allure.feature("API")
@allure.story("Добавление товара в корзину")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_add_product_to_cart():
    data = {
        "product_id": "Product_ID",
        "this_listId": "product_cart",
        "parent_product": "667",
        "LANG_key": "ru",
        "S_wh": "1",
        "S_CID": "f84d3a3af377ddbc1ebd3c6135fe84dd",
        "S_cur_code": "rub",
        "S_koef": "1",
        "quantity": "1",
        "S_hint_code": "",
        "S_customerID": ""
    }
        
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    response = requests.post(f"{Base_url}/add_products_to_cart_from_preview.php", data = data, headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Изменение количества товара в корзине")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_update_quantity():
    data = {
        "itemID" : "533466",
        "quantity" : "3",
        "action" : "update_quantity",
        "LANG_key" : "ru",
        "S_wh" : "1",
        "S_CID" : "f84d3a3af377ddbc1ebd3c6135fe84dd",
        "S_cur_code" : "rub",
        "S_koef" : "1",
        "S_hint_code" : "",
        "S_customerID" : ""
    }
        
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    response = requests.post(f"{Base_url}/action_with_basket_on_cart_page.php", data = data, headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Удаление товара из корзины")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_delete_product_from_cart():
    data = {
       "product_id" : "Product_ID",
       "LANG_key" : "ru",
       "S_wh" : "1",
       "S_CID" : "f84d3a3af377ddbc1ebd3c6135fe84dd",
       "S_cur_code" : "rub",
       "S_koef" : "1",
       "S_hint_code" : "",
       "S_customerID" : ""
    }
        
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    response = requests.post(f"{Base_url}/action_with_basket_on_cart_page.php", data = data, headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    
