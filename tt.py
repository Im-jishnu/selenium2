from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
from selenium.webdriver.common.by import By
user_name= driver.find_element(by=By.NAME,value="txtUsername")
user_name.send_keys("Admin")
user_password=driver.find_element(by=By.NAME,value="txtPassword")
user_password.send_keys("admin123")
b=driver.find_element(by=By.NAME,value="Submit")
b.click()
exptitle="OrangeHRM"
captitle= driver.title
if exptitle==captitle:
    print("succes")
else:
    ("failed")