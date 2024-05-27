from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, "").click()
bb = Select(driver.find_element((By.XPATH, "")))
bb.select_by_visible_