#navigation commands
# learn about navigation mean moving from one page to other 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.google.com/")#1
print(driver.title)
driver.get("https://www.facebook.com/")#2
print(driver.title)
time.sleep(3)
driver.back()#1
print(driver.title)
time.sleep(3)
driver.forward()#2
print(driver.title)
time.sleep(3)
driver.close()
driver.quit()