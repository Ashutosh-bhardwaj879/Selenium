#download file in firefox
# bypass download box
from selenium import webdriver 
import time
#import os
#os.environ["LANG"] = "en_US.UTF-8"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","/home/divya/snap")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)
driver = webdriver.Firefox(executable_path="/home/divya/Documents/gd",firefox_profile = fp)
driver.get("http://demo.guru99.com/test/yahoo.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='messenger-download']").click()
driver.quit()
