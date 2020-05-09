#mouse options
#double click
#action chains
#double_click
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
element = driver.find_element_by_xpath("/html/body/button")
actions = ActionChains(driver)
#will perform double click
actions.double_click(element).perform()
#driver.quit()