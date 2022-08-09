# import time
# from selenium import webdriver
# driver=webdriver.Chrome("C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# driver.get("https://in.search.yahoo.com/?fr2=inr")
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# try:
#     element=WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,"yschsp")))
#     element.send_keys("sherinmariyamma5@gmail.com")
#     time.sleep(30)
# finally:
#     driver.close()
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ed
# from selenium.common.exceptions import ElementNotVisibleException
# from selenium.common.exceptions import NoSuchElementException
# driver=webdriver.Chrome(executable_path="C:\\Users\\conta\\OneDrive\\Desktop\\jishnu\\chromedriver.exe")
# wait=WebDriverWait(driver,20,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
# from selenium.webdriver.common.by import By
#
# driver.get("https://in.search.yahoo.com/?fr2=inr")
# s=wait.until(ed.presence_of_element_located((By.ID,"yschsp")))
# s.send_keys("techols")
# time.sleep(20)
# driver.close()



