# 1 задание (Откройте http://practice.automationtesting.in/)
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2 задание (Нажмите на вкладку "My Account Menu")
driver.find_element_by_link_text("My Account").click()
# 3 задание (В разделе "Login", введите email для логина)
driver.find_element_by_id("username").send_keys("sema846@mail.ru")
# 4 задание (В разделе "Login", введите пароль для логина)
driver.find_element_by_id("password").send_keys("Sas223sas223")
# 5 задание (Нажмите на кнопку "Login")
driver.find_element_by_css_selector(".woocommerce-Button.button[value='Login']").click()
# 6 задание (Добавьте проверку, что на странице есть элемент "Logout")
element = driver.find_element_by_link_text("Logout")
element_get_text = element.text
assert "Logout" in element_get_text
