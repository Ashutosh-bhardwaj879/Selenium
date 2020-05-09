#working with dropdown
#select one option from options
#capture options
#count no of options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
drop_down = driver.find_element_by_id("select-demo")
drp = Select(drop_down)# select is a class ussed for drop downs
#driver.quit()
# 1 way
drp.select_by_visible_text('Monday')
#2
#drp.select_by_index(4)
#3
#drp.select_by_value("Friday")
#count no of options
print(len(drp.options))
#capture all the option
all_options = drp.options
for options in all_options:
    print(options.text)