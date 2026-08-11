import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoblaze.com/")

contact = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
contact.click()
time.sleep(4)
email = driver.find_element(By.ID, 'recipient-email')
email.send_keys("data@test.com")
time.sleep(1)
name = driver.find_element(By.ID, 'recipient-name')
name.send_keys("Milan Sharma")
time.sleep(1)
messages = driver.find_element(By.ID, 'message-text')
messages.send_keys("This is a message sent from milan using selenium tool...")
time.sleep(2)
send = driver.find_element(By.XPATH,'//*[@id="exampleModal"]/div/div/div[3]/button[2]')
send.click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
