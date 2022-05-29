# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:11:38 2022

@author: Global Computers
"""

from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")
driver.get("https://masterprograming.com/contact-us/")

var = driver.find_element_by_name("email")
print(var.is_displayed())  
print(var.is_enabled())

var = driver.find_element_by_name("gender")
print(var.is_selected())
driver.quit()