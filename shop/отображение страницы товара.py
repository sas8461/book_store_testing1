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
# 4 задание (Откройте книгу "HTML 5 Forms")
driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
# 5 задание (Добавьте тест, что заголовок книги назвается: "HTML5 Forms")
element = driver.find_element_by_css_selector("h1.product_title.entry-title")
element_get_text = element.text
assert "HTML5 Forms" in element_get_text