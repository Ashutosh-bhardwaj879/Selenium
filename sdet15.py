#working with web tbles
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.get("http://demo.guru99.com/test/web-table-element.php")
#count no of rows
rows = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div[1]/table/tbody/tr"))
#count no of columns
cols = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div[1]/table/thead/tr/th"))
print(rows)
print(cols)
print("Product"+"    "+"Article"+"     "+"Price")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)
    print()
#common mistakes
# "+str(c)+"
#no of brackets
# end didnt work
#
