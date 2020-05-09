#working with input boxes
#1  how to find how many inout boxes are there
#2  how to provide value in boxes
#3  how to get the status
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#how to find how many input boxes are there
input_boxes=driver.find_elements(By.ID,"text")
print(len(input_boxes))
#input is using send.key()

driver.quit()#quiting all browsers