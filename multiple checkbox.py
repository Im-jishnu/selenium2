# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# from selenium.webdriver.common.by import By
# a=driver.find_element(by=By.ID,value="Email").send_keys("")
# b=driver.find_element(by=By.ID,value="Password").send_keys("")
# c=driver.find_element(by=By.ID,value="RememberMe").click()
# d=driver.find_element(by=By.CLASS_NAME,value="login-button").click()



# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# # from selenium.webdriver.common.by import By
# box=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in box:
#     if i==box[2]:
#         pass
#     else:
#         i.click()

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# # from selenium.webdriver.common.by import By
# box=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in box:
#     if i==box[2]:
#         i.click()
#     else:
#         pass
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
driver.get("https://www.orangehrm.com/")
link=driver.find_elements(by=By.TAG_NAME,value='a')
#link=driver.find_elements_by_tag_name('a')
print("broken cods:")
glinks=[]
for i in link:
    url=i.get_attribute('href')
    try:
        res=requests.head(url)
        if res.status_code >= 400:
            print(url)
        else:
            glinks.append(url)
            print(glinks)

    except:
         None










# from selenium import webdriver
# import requests
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.orangehrm.com/")
# link=driver.find_elements(by=By.TAG_NAME,value="a")
# driver.get_at


