from selenium import webdriver
import time
driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(2)
driver.find_element_by_name("btnK").click()
