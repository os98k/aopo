# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:32:24 2022

@author: Global Computers
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= "C:\\Users\\Global Computers\\Desktop\Selenium\\chromedriver.exe")
driver.get("https://xplorefree.com/contact/")

var = driver.find_element_by_name("your-name")
var.send_keys("os98k")

var = driver.find_element_by_name("your-email")
var.send_keys("os98k1@gmail.com")

var1 = driver.find_element_by_name("your-subject")
var1.send_keys("Want to Contact ")

var2 = driver.find_element_by_name("your-message")
var2.send_keys("Hi, I have read your blog and find it quite interesting and want to contact you with this regards")

var3 = driver.find_element_by_class_name("wpcf7-submit")
var3.click()

#driver.find.element_by_xpath("wpcf7-form-control has-spinner wpcf7-submit").click()
time.sleep(2)
