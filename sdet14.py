#working with browser windows
#driver.current_window_handle
#driver.window_handles
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.google.com/intl/en-GB/gmail/about/")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a").click()
print(driver.current_window_handle)#CDwindow-5193E30B6CCCDFA7279E83D69E0B3C02
cools = driver.window_handles#returns all values of open window
for handle in cools:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Gmail - Email from Google":
        driver.close()
time.sleep(2)
driver.quit()
