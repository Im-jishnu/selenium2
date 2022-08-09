from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
import time
from selenium.webdriver.common.by import By
a=driver.find_element(by=By.NAME,value="txtUsername").send_keys("Admin")
b=driver.find_element(by=By.NAME,value="txtPassword").send_keys("admin123")
c=driver.find_element(by=By.NAME,value="Submit").click()
driver.maximize_window()
time.sleep(10)
driver.minimize_window()
time.sleep(10)



