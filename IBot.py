import time
import sys
import os
import autoit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PathFinder import img 


class InstaBot:
    def __init__(self,username,password):
        mobile_emulation = { "deviceName": "Nexus 5X" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome(chrome_options=chrome_options)
        

    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)       
        login_b = driver.find_element_by_xpath("//button[contains(text(), 'Log In')]")  
        login_b.click()
        time.sleep(3)
        username_element=driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        time.sleep(3)
        username_element.send_keys(self.username)
        password_element=driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")  #  write if condition for the popup
            not_now_button.click()
            time.sleep(2)
        except:
            pass
        try:
            not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")  #  write if condition for the popup
            not_now_button.click()
        except:
            pass

    def upload(self,a):
        driver=self.driver
        upload_button=driver.find_element_by_xpath("//div[@role='menuitem']")
        upload_button.click()
        time.sleep(2)
        autoit.win_active("Open") 
        time.sleep(2)
        #for x in range(n): #  multiple pics
        autoit.control_send("Open","Edit1",img[a])  #  check later
        time.sleep(2)
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(1.5)
        next_button=driver.find_element_by_class_name('UP43G')
        next_button.click()
        time.sleep(1.5)
        caption_area=driver.find_element_by_class_name('_472V_')
        caption_area.send_keys("Wow it got uploaded!!! ")
        share_but=driver.find_element_by_class_name('UP43G')
        share_but.click()
        time.sleep(5)        
        try:
            noti_pop_up=driver.find_element_by_class_name('piCib')
            noti_pop_up.click()
        except:
            pass
        time.sleep(3)
        
        try:
            noti_pop_up=driver.find_element_by_class_name('aOOlW   HoLwm ')
            noti_pop_up.click()
        except:
            pass

        try:
            not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")  #  write if condition for the popup
            not_now_button.click()
            time.sleep(2)
        except:
            pass

        time.sleep(2)

        



if __name__ == "__main__":

    username=""     #  user username
    password=""     #  matching password

    ib=InstaBot(username,password)
    ib.login()
    time.sleep(1)
    z=0
    for i in img:
        ib.upload(z)
        z=z+1
        time.sleep(2400)     #  managing the frequency of upload as instagram would not allow more than 2/3 images an hour
