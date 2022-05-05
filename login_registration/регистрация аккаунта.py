# 1 задание (Откройте http://practice.automationtesting.in/)
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2 задание (Нажмите на вкладку "My Account Menu")
driver.find_element_by_link_text("My Account").click()
# 3 задание (В разделе "Register", введите email для регистрации)
driver.find_element_by_id("reg_email").send_keys("sema846@mail.ru")
# 4 задание (В разделе "Register", введите пароль для регистрации)
driver.find_element_by_id("reg_password").send_keys("Sas223sas223")
# 5 задание (Нажмите на кнопку "Register")
driver.find_element_by_css_selector(".woocommerce-Button.button[value='Register']").click()