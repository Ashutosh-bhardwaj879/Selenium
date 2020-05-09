#working with links
#maximize window
#how many link
#capture link
#click on link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

driver.maximize_window()
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)# text all the links 
#clicking on links
driver.find_element(By.LINK_TEXT,"Selenium Tutorials").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Sele Tuto").click()

#driver.quit()