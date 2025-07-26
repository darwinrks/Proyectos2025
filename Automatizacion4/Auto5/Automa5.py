import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

service = Service(
	executable_path=r"C:\Users\W10HOME\Downloads\chromedriver-win64\chromedriver.exe",
	service_log_path=os.devnull)
driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.NAME, "my-text").send_keys("Darwin")
time.sleep(1)
driver.find_element(By.NAME, "my-password").send_keys("clave123")
time.sleep(1)
driver.find_element(By.NAME, "my-textarea").send_keys("prueba")
time.sleep(1)

select_element = driver.find_element(By.NAME, "my-select")
time.sleep(1)
Select(select_element).select_by_visible_text("Two")
time.sleep(1)

driver.find_element(By.ID, "radio-button-2").click()
time.sleep(1)

driver.find_element(By.ID, "checkbox-1").click()

driver.find_element(By.NAME, "my-date").send_keys("2025-07-26")
time.sleep(1)
driver.find_element(By.TAG_NAME, "button").click()