#wait commandss
#implicit wait
#assert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.instagram.com/?hl=en")#complete url opening takes time
# waiting for 6 sec
driver.implicitly_wait(6)
assert "Instagram" in driver.title
user_ele = driver.find_element_by_name("username")
pwd_ele  = driver.find_element_by_name("password")
user_ele.send_keys("psab878@gmail.com")#sending username to fb
pwd_ele.send_keys("Str@w2err2")
driver.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div ").click()  
time.sleep(5)
driver.close()
driver.quit() 