#explicit wait
#import various things
#mplicit wait also
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="/home/divya/Documents/cdn")
driver.implicitly_wait(5)
#max window
driver.maximize_window()
driver.get("https://www.expedia.co.in/")
driver.find_element(By.ID,"tab-flight-tab-hp").click()#2 method will click flight  button
time.sleep(2)
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID,"flight-departing-hp-flight").clear()#date pre identified get cleared
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("30/04/2020")
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("10/05/2020")
#driver.find_element_by_xpath("//*[@id='flight-returning-hp-flight']").clear()
#driver.find_element_by_xpath("[@id='flight-returning-hp-flight']").send_keys("10/05/2020")
driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div[1]/div[2]/div[2]/section[1]/form/div[9]/label/button").click()
#explicit wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='changeOptionFilter-0']")))#remember 3 brackets
element.click()#clicking the elemnet no return 
time.sleep(3)
driver.quit()#quiting all browsers


#driver.close()
#driver.quit() s