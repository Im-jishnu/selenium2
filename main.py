from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://www.google.com/")
a=driver.find_element_by_link_text("Gmail")
a.click()
sign=driver.find_element_by_link_text("Sign in").click()
from selenium.webdriver.common.by import By
b=driver.find_element(by=By.NAME,value="identifier")
b.send_keys("jishnusreedharan0@gmail.com")
c=driver.find_element(by=By.ID,value="identifierNext").click()


