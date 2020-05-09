#taking screenshots
#save_screenshot('filename')
#get_screenshot_as_file('filename')
#should wnd with .png
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =  webdriver.Chrome(executable_path = "/home/divya/Documents/cdn")
driver.get("https://www.selenium.dev/")
#driver.save_screenshot('/home/divya/snap/screenshots/homepage.png')

driver.get_screenshot_as_file("/home/divya/snap/screenshots/homepage.png")
time.sleep(2)
driver.quit()







