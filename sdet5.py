#send_keys is used to send iud and pwd to sites
#conditional statements 
#is_displayed
#is_enables
#is_selected
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.facebook.com/")
user_ele= driver.find_element_by_name("email")#inspect element then id
print(user_ele.is_displayed())#true or false
print(user_ele.is_enabled())#true or false
pwd_ele = driver.find_element_by_name("pass")#its an id
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
#userr_ele= driver.find_element_by_name("emal")#inspect element then id
#will show error
#print(userr_ele.is_displayed())#true or false
#print(userr_ele.is_enabled()
user_ele.send_keys("ashutoshbhardwaj879@gmail.com")#sending username to fb
pwd_ele.send_keys("Str@w2erry")# sending pwd to fb
driver.find_element_by_xpath("//*[@id='u_0_b']").click()
home = driver.find_element_by_css_selector("#u_0_c > a:nth-child(1)")
print(home.is_selected())#home is not selected when we open fb oso false
driver.close()
driver.quit()