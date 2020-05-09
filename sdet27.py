#Working with cookies
#capture ookies from browser
#count no of cookies
#read cookie pairs 
#add cookie
#deleting specific cookie
#deleting all cookie
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path ="/home/divya/Documents/cdn")
driver.get("https://www.amazon.in/")
driver.maximize_window()
cookies = driver.get_cookies()
print(len(cookies))# print no of cookies
print(cookies)#capture cookies
#add cookies
cookie = {'name':'mycookie','value':'1234567890'}
driver.add_cookie(cookie)
#after adding cookies         
cookies = driver.get_cookies()
print(len(cookies))# print no of cookies
print(cookies)#capture cookies
#deleting cookie
driver.delete_cookie('mycookie')
cookies = driver.get_cookies()
print(len(cookies))# print no of cookies
print(cookies)#capture cookies
#deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))        

