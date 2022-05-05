# 1 задание (Откройте http://practice.automationtesting.in/)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2 задание (Нажмите на вкладку "Shop")
driver.find_element_by_link_text("Shop").click()
# 3 задание (Добавьте в корзину книгу "HTML5 WebApp Development")
driver.find_element_by_css_selector(".post-182 .button").click()
time.sleep(5)
# 4 задание (Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00")
element = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
element1 = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
element_get_text = element.text
element_get_text1 = element1.text
assert "1 Item" in element_get_text
assert "₹180.00" in element_get_text1
# 5 задание (Перейдите в корзину)
driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents").click()
# 6 задание (Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость)
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount"), "₹180.00"))
# 7 задание (Используя явное ожидание, проверьте что в Total отобразилась стоимость)
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong .woocommerce-Price-amount.amount"), "₹189.00"))