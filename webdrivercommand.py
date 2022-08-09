# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("http://demo.automationtesting.in/FileUpload.html")
# print(driver.title)
# print(driver.current_url)
# driver.fullscreen_window()
# # driver.refresh()
# driver.find_element_by_link_text("Practice Site").click()
# driver.back()
# # driver.forward()
# # driver.close()
# driver.quit()
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://www.freelancer.com/post-project")
# # usr_name=driver.find_element_by_class_name("NativeElement")
# # print(usr_name.is_displayed())

# a=driver.find_element_by_class_name("NextButton ng-star-inserted")
# print(a.is_enabled())

# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://www.geeksforgeeks.org/")
# a=driver.find_element_by_link_text("Courses")
# print(a.text)


# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
# driver.get("https://www.canva.com")
# a=driver.find_element_by_link_text("/signup/")
# print(a.get_attribute("href"))
# print(a.text)


from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://www.geeksforgeeks.org/")
a=driver.find_element_by_link_text("C++")
print(a.get_attribute("href"))
print(a.text)