
import time  
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()

options.add_experimental_option("prefs", {
"credentials_enable_service": False,
"profile.password_manager_enabled": False})
options.add_argument("--incognito")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-infobars")
options.add_argument("--disable-autofill-keyboard-accessory-view[8]")

service = Service(executable_path=r"C:\Users\W10HOME\Downloads\chromedriver-win64\chromedriver.exe", service_log_path=os.devnull)
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)
user = driver.find_element(By.ID, "user-name")
user.send_keys("standard_user")
time.sleep(1)
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(1)
btn_login = driver.find_element(By.ID, "login-button").click()
time.sleep(1)

# 3. Agregar una camiseta al carrito
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

# 4. Ir al carrito
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(1)

# 5. Proceder al checkout
driver.find_element(By.ID, "checkout").click()

# 6. Llenar formulario de envío
driver.find_element(By.ID, "first-name").send_keys("Darwin")
driver.find_element(By.ID, "last-name").send_keys("Moreno")
driver.find_element(By.ID, "postal-code").send_keys("50500")
driver.find_element(By.ID, "continue").click()

time.sleep(1)

# 7. Finalizar la compra
driver.find_element(By.ID, "finish").click()
driver.close()