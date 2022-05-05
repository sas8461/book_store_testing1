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
# 3 задание (Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm")
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(10)
driver.find_element_by_css_selector(".post-182 .button").click()
time.sleep(5)
driver.find_element_by_css_selector(".post-180 .button").click()
time.sleep(5)
# 4 задание (Перейдите в корзину)
driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents").click()
# 5 задание (Удалите первую книгу)
time.sleep(10)
driver.find_element_by_css_selector("tbody > .cart_item:nth-child(1) .remove").click()
# 6 задание (Нажмите на Undo (отмена удаления))
time.sleep(5)
driver.find_element_by_css_selector(".woocommerce-message a").click()
time.sleep(5)
# 7 задание (В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“)
driver.find_element_by_css_selector("tbody > .cart_item:nth-child(1) .input-text.qty").clear()
driver.find_element_by_css_selector("tbody > .cart_item:nth-child(1) .input-text.qty").send_keys(3)
# 8 задание (Нажмите на кнопку "UPDATE BASKET")
driver.find_element_by_css_selector(".actions [name='update_cart']").click()
# 9 задание (Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3)
value_checked = driver.find_element_by_css_selector("tbody > .cart_item:nth-child(1) .input-text.qty").get_attribute("value")
assert value_checked == "3"
# 10 задание (Нажмите на кнопку "APPLY COUPON")
time.sleep(5)
driver.find_element_by_css_selector(".coupon > [value='Apply Coupon']").click()
time.sleep(5)
# 11 задание (Добавьте тест, что возникло сообщение: "Please enter a coupon code.")
text_checked = driver.find_element_by_css_selector(".woocommerce-error li").text
assert text_checked == "Please enter a coupon code."