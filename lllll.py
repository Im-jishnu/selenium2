from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
a=driver.find_element(by=By.NAME,value="q").send_keys("Linkedin login")
b=driver.find_element(by=By.NAME,value="q").send_keys(Keys.ENTER)
driver.fullscreen_window()
time.sleep(10)
c=driver.find_element_by_class_name("LC20lb").click()
driver.refresh()
driver.close()
driver.quit()




