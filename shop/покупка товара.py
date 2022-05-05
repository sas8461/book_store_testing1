# 1 задание (Откройте http://practice.automationtesting.in/)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2 задание (Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз)
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
# 3 задание (Добавьте в корзину книгу "HTML5 WebApp Development")
time.sleep(5)
driver.find_element_by_css_selector(".post-182 .button").click()
time.sleep(5)
# 4 задание (Перейдите в корзину)
driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents").click()
# 5 задание (Нажмите "PROCEED TO CHECKOUT")
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward"))).click()
# 6 задание (Заполните все обязательные поля)
WebDriverWait(driver, 20).until(
    EC.url_to_be("http://practice.automationtesting.in/checkout/"))
driver.find_element_by_id("billing_first_name").send_keys("sema")
driver.find_element_by_id("billing_last_name").send_keys("syundyukov")
driver.find_element_by_id("billing_email").send_keys("sema8461@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("89821110044")
time.sleep(5)
driver.find_element_by_id("select2-chosen-1").click()
time.sleep(5)
driver.find_element_by_id("select2-result-label-179").click()
driver.find_element_by_id("billing_address_1").send_keys("Russia, Chelyabinsk, Komsomolsky prospect")
driver.find_element_by_id("billing_city").send_keys("Russia")
driver.find_element_by_id("billing_state").send_keys("Chelyabinsk")
driver.find_element_by_id("billing_postcode").send_keys("123456")
# 7 задание (Выберите способ оплаты "Check Payments")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
driver.find_element_by_id("payment_method_cheque").click()
# 8 задание (Нажмите PLACE ORDER)
driver.find_element_by_id("place_order").click()
# 9 задание (Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received.")
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# 10 задание (Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments")
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))