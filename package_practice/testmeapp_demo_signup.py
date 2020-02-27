from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
driver.find_element_by_name("userName").send_keys("Niroop")
driver.find_element_by_id("firstName").send_keys("Niroop")
driver.find_element_by_name("lastName").send_keys("Mohan")
driver.find_element_by_id("password").send_keys("Iloveyou")
driver.find_element_by_name("confirmPassword").send_keys("Iloveyou")

driver.find_element_by_name("emailAddress").send_keys("uppi.benki@gmail.com")
driver.find_element_by_name("mobileNumber").send_keys("1234567890")
driver.find_element_by_name("address").send_keys("12,LA,USA")
driver.find_element_by_name("answer").send_keys("Bengaluru")
select = Select(driver.find_element_by_name('secutrityQuestion'))
select.select_by_value("411012")

driver.find_element_by_xpath("//img[@alt='Ch']").click()
select1 = Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select1.select_by_value('May')