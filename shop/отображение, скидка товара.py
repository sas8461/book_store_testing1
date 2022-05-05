# 1 задание (Откройте http://practice.automationtesting.in/)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# 4 задание (Откройте книгу "Android Quick Start Guide")
driver.find_element_by_css_selector(".post-169 .attachment-shop_catalog").click()
# 5 задание (Добавьте тест, что содержимое старой цены = "₹600.00")
element = driver.find_element_by_css_selector("del .woocommerce-Price-amount.amount")
element_get_text = element.text
assert "₹600.00" in element_get_text
# 6 задание (Добавьте тест, что содержимое новой цены = "₹450.00")
element1 = driver.find_element_by_css_selector("ins .woocommerce-Price-amount.amount")
element_get_text1 = element1.text
assert "₹450.00" in element_get_text1
# 7 задание (Добавьте явное ожидание и нажмите на обложку книги)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images img")))
driver.find_element_by_css_selector(".images img").click()
# 8 задание (Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа))
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
driver.find_element_by_css_selector("a.pp_close").click()