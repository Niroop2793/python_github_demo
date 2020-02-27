from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")


driver.switch_to.frame(0)
src = driver.find_element_by_id("draggable99")
tgt = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
time.sleep(3)
actions.drag_and_drop(src, tgt).perform()
