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
# 4 задание (Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию)
select_checked = driver.find_element_by_css_selector("select > [value='menu_order']").get_attribute("selected")
if select_checked == "true":
    print("В селекторе выбран вариант по умолчанию")
else:
    print("В селекторе выбран вариант не по умолчанию")
# 5 задание (Отсортируйте товары по цене от большей к меньшей)
driver.find_element_by_class_name("orderby").click()
driver.find_element_by_css_selector(".orderby > [value='price-desc']").click()
# 6 задание (Снова объявите переменную с локатором основного селектора сортировки)
select_checked = driver.find_element_by_css_selector("select > [value='menu_order']").get_attribute("selected")
if select_checked == "true":
    print("В селекторе выбран вариант по умолчанию")
else:
    print("В селекторе выбран вариант не по умолчанию")
# 7 задание (Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей)
select_checked1 = driver.find_element_by_css_selector("select > [value='price-desc']").get_attribute("selected")
if select_checked1 == "true":
    print("В селекторе выбран вариант от большей к меньшей")
else:
    print("В селекторе выбран другой вариант")