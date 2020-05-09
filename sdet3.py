# basic webdriver commands
#captuure title of the page
#capture url of the page
#closing and quittng browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("http://demo.automationtesting.in/Index.html")#goessite
print(driver.title)#prints title
print(driver.current_url)#prints url
#will  click on it and close it after 6 sec
driver.find_element_by_xpath("//*[@id='enterimg']").click()
time.sleep(6)
driver.close()#will close single window at a time
driver.quit()#will close all windows      