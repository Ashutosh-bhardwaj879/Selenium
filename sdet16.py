#scrolling
#using pixel
#using element found
#at the end of page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(1)
#scroll by pixels
#driver.execute_script("window.scrollBy(0,770)","")
#find until element
flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)
#scroll until end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#driver.quit()