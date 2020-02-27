from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")



src = driver.find_element_by_id("sub-menu")

actions = ActionChains(driver)
actions.move_to_element(src).perform()


tgt = driver.find_element_by_id("link2")

actions.move_to_element(tgt).click().perform()
driver.back()


actions1 = ActionChains(driver)
d = driver.find_element_by_id("double-click")
actions1.double_click(d).perform()


time.sleep(2)
alert = driver.switch_to_alert()
str1 = alert.text
print(str1)
alert.accept()