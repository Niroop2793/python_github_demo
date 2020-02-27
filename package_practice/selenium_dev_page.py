from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()