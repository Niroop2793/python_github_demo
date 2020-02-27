from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
window_before1 = driver.window_handles[0]
         
print("First window:"+window_before1) 
title1=driver.title
print("First window title:"+title1)
#          driver.find_element_by_xpath("//a[https://twitter.com]").click()
#driver.switch_to.frame(1)
driver.find_element_by_xpath("//a[contains(.,'AboutUs')]").click()
driver.find_element_by_xpath("//a[contains(.,'Offices')]").click()
driver.find_element_by_xpath("//a[contains(.,'Bangalore')]").click()

window_after = driver.window_handles[1]
print("Second window:"+window_after) 
title2=driver.title
print("Bangalore page title:"+title2)
driver.switch_to.window(window_after)
driver.switch_to.frame("main_page")
text = driver.find_element_by_id("demo3").text
print(text)
driver.quit()