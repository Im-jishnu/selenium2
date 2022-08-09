from selenium import webdriver"https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get(")
from selenium.webdriver.common.by import By
name=driver.find_element(by=By.NAME,value="Email")
name.send_keys("")
pas=driver.find_element(by=By.NAME,value="Password")
pas.send_keys("")
r=driver.find_element(by=By.ID,value="RememberMe")
r.click()
log=driver.find_element_by_xpath("//button[@type='submit']")
log.click()
