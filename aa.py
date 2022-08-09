from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://www.python.org")
from selenium.webdriver.common.by import By
search=driver.find_element(by=By.NAME,value= "q")
search.send_keys("function")
go=driver.find_element(by=By.ID,value="submit")
go.click()
print(driver.title)
exptit="Welcome to Python.org"
captit=driver.title
if exptit==captit:
    print("pass")
else:
    print("fail")