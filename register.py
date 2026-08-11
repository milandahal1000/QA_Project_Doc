from selenium import webdriver
from selenium.webdriver import Keys     #this is used for 'ENTER' key
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select    # This is for the dropdowns to select options
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Register.html')

#Username Field
f_name = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')
f_name.send_keys("Milan")
l_name = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')
l_name.send_keys("Sharma")

#Address, Mail, Phone Field
address = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[2]/div/textarea')
address.send_keys("Kathmandu")
Email = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[3]/div/input')
Email.send_keys("data@test.com")
phone = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[4]/div/input')
phone.send_keys("1234567890")

#Gender, Hobbies Field
gender = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input')
gender.click()
hobbies = driver.find_element(By.ID,'checkbox2')
hobbies.click()

#languages Field
lang = driver.find_element(By.ID,'msdd')
lang.click()
ww = WebDriverWait(driver, 10)
english = ww.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a'))
)
english.click()

# Click somewhere outside to close the dropdown
driver.find_element(By.TAG_NAME, "body").click()

#Skills Field
skills = Select(driver.find_element(By.ID,'Skills'))
skills.select_by_value("C")

#Select Country Field
country = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')
country.click()
input1 = ww.until((EC.element_to_be_clickable((By.XPATH,'/html/body/span/span/span[1]/input'))))
input1.send_keys("India")
input1.send_keys(Keys.ENTER)

#Date of Birth Field
year = Select(driver.find_element(By.ID,'yearbox'))
year.select_by_value("2003")
month = Select(driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[11]/div[2]/select'))
month.select_by_value("December")
day = Select(driver.find_element(By.ID,'daybox'))
day.select_by_value("17")

#Password Field
f_pass = driver.find_element(By.ID,'firstpassword')
f_pass.send_keys("agent123")
cpass = driver.find_element(By.ID,'secondpassword')
cpass.send_keys("agent123")

#Click submit button
submit = driver.find_element(By.ID,'submitbtn')
submit.click()

time.sleep(5)
