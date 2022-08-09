# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# # import time
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# time.sleep(20)
# driver.close()

# from selenium.webdriver.common.by import By
# s=driver.find_element(by=By.NAME,value="txtUsername").send_keys("Admin")
# driver.implicitly_wait(60)
# a=driver.find_element(by=By.NAME,value="txtPassword").send_keys("admin123")
# c=driver.find_element(by=By.NAME,value="Submit").click()
# a=driver.find_element_by_class_name("firstLevelMenu").click()



# from selenium import webdriver
# # from selenium.webdriver.support.ui import webdriverwait
# # from selenium.webdriver.support import expected_conditions as ec
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://demoqa.com/login")
# from selenium.webdriver.common.by import By
# a=driver.find_element_by_id("userName").send_keys("sherin")
# b=driver.find_element_by_id("password").send_keys("Sherin27@")
# c=driver.find_element(by=By.ID,value="login").click()

#import time
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://demoqa.com/login")
a=driver.find_element(by=By.ID,value="userName").send_keys("sherin")
b=driver.find_element(by=By.ID,value="password").send_keys("Sherin27@")
c=driver.find_element(by=By.ID,value="login").click()

# try:
#     element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"searchBox")))
#     element.send_keys("learn java")
#     time.sleep(10)
# finally:
#      driver.close()