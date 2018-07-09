
# coding: utf-8

# In[1]:


import time
from selenium import webdriver
user= input("Enter Username")
pwd= input("Enter PAssword")
driverpath="D:\Masters Academic\chromedriver_win32\chromedriver.exe" # chrome driver path
driver=webdriver.Chrome(driverpath)


#gmail link
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# using Xpath to locate used id box
elem=driver.find_element_by_xpath("//*[@id='identifierId']")
# sending credentials
elem.send_keys(user)
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
# Time lapse to undestand what is happening
time.sleep(2)
elem=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
elem.send_keys(pwd)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(10)
driver.close()



