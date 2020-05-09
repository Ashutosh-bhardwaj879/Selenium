#how to upload files
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("http://demo.guru99.com/test/upload/")
driver.maximize_window()
#uploading file from computer using file path remember the last slash
driver.find_element_by_xpath("//*[@id='uploadfile_0']").send_keys("/home/divya/Downloads/blog.jpg")
#clicking submit button
driver.find_element_by_xpath("//*[@id='submitbutton']").click()



#driver.quit()