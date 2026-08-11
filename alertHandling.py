from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

simp_alert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simp_alert.click()
button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button1.click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

verify_alert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
verify_alert.click()
button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button2.click()
time.sleep(2)
alert.dismiss()
time.sleep(3)


alert_txt_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
alert_txt_box.click()
button3 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button3.click()
time.sleep(2)
alert.send_keys("Ujawl")
time.sleep(2)
alert.accept()
time.sleep(5)