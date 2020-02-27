from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
location = "file:///C:/Users/training_d5.01.02/Desktop/niroop/simple_alert.htm"
driver.get(location)

button = driver.find_element_by_name('alert')
button.click()

alert = driver.switch_to_alert()

msg = alert.text
print("txt is:"+msg)
time.sleep(2)
alert.accept()

driver.refresh()

driver.close()
driver.quit()
