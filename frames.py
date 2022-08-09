from selenium import webdriver
# from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
driver.switch_to.frame("packageListFrame")
f1=driver.find_element(By.LINK_TEXT,"org.openqa.selenium.opera")
f1.click()
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame("packageFrame")
f2=driver.find_element(By.LINK_TEXT,"OperaOptions")
f2.click()
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame("classFrame")
f3=driver.find_element(By.XPATH,value="/html/body/header/nav/div[1]/div[1]/ul/li[4]/a")#('/html/body/div[1]/ul/li[4]/a')
f3.click()
time.sleep(4)
