#  from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.facebook.com")
# driver.find_element_by_link_text("Log In").click()
# from selenium.webdriver.common.by import By
# log=driver.find_element(by=By.NAME,value="email")
# log.send_keys("9747800202")
# pas=driver.find_element(by=By.NAME,value="pass")
# pas.send_keys("Idonthavefriends")
# logg=driver.find_element(by=By.ID,value="loginbutton")
# logg.click()
#
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.yatra.com")
# lo=driver.find_elements_by_tag_name('a')
# print(len(lo))
# for i in lo:
#     print(i.text)



# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.canva.com")
# hom=driver.find_elements_by_tag_name("a")
# print(len(hom))
# for i in hom:
#    print(i.text)
# print(driver.title)
# a="Free Design Tool: Presentations, Video, Social Media | Canva"
# b=driver.title
# if a==b:
#     print("pass")
# else:
#     print("fail")
#
# import time
#
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_id("txtUsername").send_keys("admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# driver.find_element_by_link_text("Performance").click()
# driver.find_element_by_css_selector("a.firstLevelMenu").click()
# driver.maximize_window()
# time.sleep(20)
# driver.minimize_window()
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# a=driver.find_elements(by=By.ID,value="//input[@id='checkBoxOption']")
# for i in a:
#     if i==a[0]:
#         pass
#     else:
#         i.click()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# selected=driver.find_element(by=By.XPATH,value="//select[@id='dropdown-class-example']")
# dd=Select(selected)
# dd.selectby_visible_text("Option3")



# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# selected=driver.find_element(by=By.XPATH,value="//select[@id='dropdown-class-example']")
# dd=Select(selected)
# dd.select_by_visible_text("Option3")
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# button=driver.find_element(by=By.XPATH,value="//button['Click for JS Confirm']")
# button.click()
# time.sleep(10)
# window=driver.switch_to.alert
# print(window.text)
# window.accept()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# btn=driver.find_element(by=By.XPATH,value="//button['Click for JS Confirm']")
# btn.click()
# w=Alert(driver)
# print("basith is pwolli")
# w.accept()


#dropdwon

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# a=driver.find_element(by=By.XPATH,value="//select[@id='dropdown-class-example']")
# b=Select(a)
# c=b.options
# for i in c:
#     if i.text=="option3":
#         pass
#     else:
#         i.click()


#FRAMES

# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
# driver.switch_to.frame("packageListFrame")
# driver.find_element_by_link_text("org.openqa.selenium.chrome").click()
# driver.switch_to.default_content()
# driver.switch_to.frame("packageFrame")
# driver.find_element_by_link_text("AbstractDriverOptions").click()
# driver.switch_to.default_content()
# driver.switch_to.frame("classFrame")
# driver.find_element_by_link_text("/html/body/div[1]/ul/li[4]/a").click()


# switch to tab
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://login.yahoo.com")
# driver.find_element(by=By.CLASS_NAME,value="privacy").click()
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.window(driver.window_handles[1])
import time

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://accounts.google.com/signin/v2/identifier?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# driver.find_element_by_link_text("Privacy").click()
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.window(driver.window_handles[1])

# finding rows and colounms

# from  selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://testautomationpractice.blogspot.com/")
# a=driver.find_elements_by_xpath("//table[@name='BookTable']//tr")
# c=driver.find_elements_by_xpath("//table[@name='BookTable']//tr[1]/th")
# print(f"num of row:{len(a)}\n num of coloumn:{len(c)}")



# from selenium import  webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# a=driver.find_elements_by_xpath("//*[@id='product']/tbody//tr")
# b=driver.find_elements_by_xpath("//*[@id='product']/tbody//tr[1]/th")
# print(len(a))
# print(len(b))
#
#
# radio button
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# a=driver.find_element_by_class_name("radioButton").click()

