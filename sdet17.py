#mouse actions
#hover options
#impot actionchains
#.perform()
#move_to_element(whichever you wanna click)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("https://www.toolsqa.com/selenium-webdriver/mouse-hover-action/")
driver.maximize_window()
tutorial = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/nav/ul/li[2]/a/span/span")
prog_lang = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/nav/ul/li[2]/ul/li[9]/a/span/span")
python = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/nav/ul/li[2]/ul/li[9]/ul/li[3]/a/span/span")
actions = ActionChains(driver)
actions.move_to_element(tutorial).move_to_element(prog_lang).move_to_element(python).click().perform()
#c= actions.move_to_element(tutorial)#.move_to_element(prog_lang).move_to_element(python).click().perform(
#time.sleep(2)
#d= c.move_to_element(prog_lang)
#time.sleep(2)
#e = d.move_to_element(python).click().perform()







