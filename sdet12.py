#working with alerts
#switch_to_alert().accept()
#switch_to_alert().miss()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
time.sleep(3)
driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
driver.quit()