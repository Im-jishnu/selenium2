#
# from selenium.webdriver.common.by import By
# log=driver.find_element(by=By.CSS_SELECTOR,value="input#txtUsername")
# log.send_keys("Admin")
# pas=driver.find_element(by=By.CSS_SELECTOR,value="input#txtPassword").send_keys("admin123")
# ff=driver.find_element(by=By.CSS_SELECTOR,value="input#btnLogin").click()

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")from selenium import webdriver
# # driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# # driver.get('https://opensource-demo.orangehrmlive.com/')
# driver.get('https://www.facebook.com/login/')
# from selenium.webdriver.common.by import By
# log=driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext")
# log.send_keys("")
# pas=driver.find_element(by=By.CSS_SELECTOR,value="input#pass").send_keys("")
# ff=driver.find_element(by=By.CSS_SELECTOR,value="button#loginbutton").click()

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.pendujatt.net/")
# a=driver.find_element_by_link_text("Malayalam Songs").click()
# b=driver.find_element_by_partial_link_text("New Malayalam Songs").click()
# print(driver.title)
# ctitle="Latest Malayalam Song Download Mp3 New Malayalam Single Tracks"
# etitle=driver.title
# if ctitle==etitle:
#     print("pass")
# else:
#     print("fail")


# tag and atribrute..........
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get('https://opensource-demo.orangehrmlive.com/')
# from selenium.webdriver.common.by import By
# driver.find_element(by=By.CSS_SELECTOR,value="input[id=txtUsername]").send_keys("Admin")
# driver.find_element(by=By.CSS_SELECTOR,value="input[name=txtPassword]").send_keys("admin123")
# driver.find_element(by=By.CSS_SELECTOR,value="input[name=Submit]").click()













# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# from selenium.webdriver.common.by import By
# c=driver.find_element(by=By.CSS_SELECTOR,value="input[name=txtUsername]").send_keys("Admin")
# v=driver.find_element(by=By.CSS_SELECTOR,value="input[name=txtPassword]").send_keys("admin123")
# b=driver.find_element(by=By.CSS_SELECTOR,value="input[name=Submit]").click()


# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# from selenium.webdriver.common.by import By
# c=driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext[name=email]").send_keys("9747800202")
# v=driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext[name=pass]").send_keys("admin123")
# b=driver.find_element(by=By.CSS_SELECTOR,value="input.button[name=Submit]").click()
#

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://training.rcvacademy.com")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# driver.minimize_window()
# driver.refresh()
# driver.forward()
# driver.back()
# driver.quit()
# driver.close()
# a=driver.find_element_by_link_text("Courses")
# print(a.get_attribute("href"))
# print(a.text)
# print(len(a))
# for i in a:
#     print(a.text)
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://training.rcvacademy.com")
a=driver.find_element_by_link_text("Home")
