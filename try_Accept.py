import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()  #opens chrome
driver.maximize_window()    #maximize the window
driver.get('https://www.demoblaze.com/')    #opens the linked site

try:
    try:
        nav_login = driver.find_element("id", "login2")
        nav_login.click()
        # driver.implicitly_wait(10)
        txt_box = driver.find_element(By.ID, "loginusername")
        txt_box.send_keys("testmorning")
        txt_password = driver.find_element(By.ID, "loginpassword")
        txt_password.send_keys("test123")
        login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()
        time.sleep(5)  # waits for 5 seconds
    except ElementNotInteractableException as e:
        print("Element Not Interactable")
        driver.implicitly_wait(10)
        txt_box = driver.find_element(By.ID, "login")
        txt_box.send_keys("testmorning")
        txt_password = driver.find_element(By.ID, "loginpassword")
        txt_password.send_keys("test123")
        login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()
        time.sleep(5)  # waits for 5 seconds

except Exception as e:
    print(f"An error occured: {e}")
driver.quit()