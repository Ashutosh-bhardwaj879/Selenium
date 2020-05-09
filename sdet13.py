#working with frames
#frame in frame
#driver.switch_to.frame(id)
#driver.switch_to.frame(name)
#driver.switch_to.default_content()
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
#firast frame
driver.switch_to.frame("packagelistframe")
driver.find_element_by_link_text("org.openqa.selenium").click()#clicked 
time.sleep(3)
#switch to main window after clicking in 1 frame
driver.switch_to.default_content()
# now go to 2 nd frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Webdriver").click()#clicked in 2 frame
time.sleep(3)
#now main window
driver.switch_to.default_content()
time.sleep(3)
# now go to 3rd frme
driver.switch_to.frame("classFrom")
driver.find_element_by_xpath("home/hwdi/").click()
driver.quit()