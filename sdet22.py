#how to download files
#how to download at specified locaations
#import options
#add_experimental_option
#chromeOptions = Options()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"/home/divya/Documents"})
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn",chrome_options = chromeOptions)
driver.get("http://demo.guru99.com/test/yahoo.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='messenger-download']").click()
driver.quit()


