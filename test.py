from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")


driver.get("https://masterprograming.com")
print("driver.title")

time.sleep(1)

from selenium.webdriver.common.keys import Keys
driver.get("https://www.facebook.com/")
FB_ID = 'YOUR_FB_ID'
FB_PSD = 'YOUR_FB_PSD'

email = driver.find_element_by_id("email") ## locating email input
email.send_keys(id)   
                ## Sending Username as input
password = driver.find_element_by_id("pass")

password.send_keys(password)
## Clicking Login Button
button = driver.find_element_by_name("login").click()