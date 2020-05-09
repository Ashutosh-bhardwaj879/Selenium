from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.instagram.com/?hl=en")
print(driver.title)
driver.close()
 