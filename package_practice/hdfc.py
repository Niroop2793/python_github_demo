from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to_frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("AYRDF4566")
driver.find_element_by_xpath("//img[@alt='continue']").click()


driver.switch_to_default_content()
driver.switch_to_frame("footer")
driver.find_element_by_link_text("Privacy Policy").click()


continue_link = driver.find_element_by_link_text('Continue')
continue_link.click()