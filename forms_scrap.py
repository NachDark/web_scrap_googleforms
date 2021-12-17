import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time
import tkinter as tk
from tkinter import messagebox
from xml.dom import minidom
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

#read xml file
mydoc = minidom.parse("C:/Users/ignacio.gaona/Documents/Phyton/DESKTOP/web_scrp_HORAS/horas.xml") # place here the filepath from xml where you want to make the bucle

items = mydoc.getElementsByTagName('horas')
web_horas = items[0].attributes['name'].value

#setup the Selenium driver

web_horas_Array = web_horas.split('https')
DRIVER_PATH = 'C:/WebDriver/bin/chromedriver.exe'      #here where you have your webdriver
service = Service(DRIVER_PATH)
service.creationflags = CREATE_NO_WINDOW
driver = webdriver.Chrome(DRIVER_PATH)
#driver.set_window_position(-10000,0)   this is to hide the execution
#here it´s bucle for scrap the google forms
count = 0
for i in web_horas_Array:  
    count = count+1
    if i!="":
          driver.get("https"+i)
          print("https"+i)
          time.sleep(1)  #you can try to reduce the time little bit depend of your system
          try:
            Save = driver.find_element_by_class_name("appsMaterialWizButtonEl")
          except NoSuchElementException:
            print('Incorrect form' + str(count))
          Save.click()
          time.sleep(0.7)
          
          try:
              Save = driver.find_element_by_class_name("freebirdFormviewerViewResponseLinksContainer")
              print('Successfully logged in ' + str(count))
              time.sleep(0.7)
          except NoSuchElementException:
              print('Incorrect form' + str(count))
              time.sleep(0.7)
   
    else:
      pass
    


