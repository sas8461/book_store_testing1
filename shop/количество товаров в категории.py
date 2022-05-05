# 1 задание (Откройте http://practice.automationtesting.in/)
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2 задание (Залогиньтесь)
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("sema846@mail.ru")
driver.find_element_by_id("password").send_keys("Sas223sas223")
driver.find_element_by_css_selector(".woocommerce-Button.button[value='Login']").click()
# 3 задание (Нажмите на вкладку "Shop")
driver.find_element_by_link_text("Shop").click()
# 4 задание (Откройте категорию "HTML")
driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()
# 5 задание (Добавьте тест, что отображается три товара)
items_count = driver.find_elements_by_css_selector("li.product.type-product.status-publish.product_cat-html")
if len(items_count) == 3:
    print("На витрине 3 товара")
else:
    print("Ошибка. Количество товаров на витрине: " + str(len(items_count)))