# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://www.python.org/")



# from selenium import webdriver
# # driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# # driver.get("https://www.geeksforgeeks.org/")
# # a=driver.find_elements_by_class_name("header-main__signup")
# # print(len(a))
# # for i in a:
# #     print(i.text)



from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://www.geeksforgeeks.org/")
driver.quit()
driver.implicitly_wait(20)