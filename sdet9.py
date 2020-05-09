#working with check boxes and radio button
#selected or not isselected()
#click()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
s = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[5]/div/form/table/tbody/tr[8]/td[2]/span[1]/input").is_selected()
print(s)
t = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[5]/div/form/table/tbody/tr[8]/td[2]/span[1]/input").click()
u = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[5]/div/form/table/tbody/tr[8]/td[2]/span[1]/input").is_selected()
print(u)
driver.quit()