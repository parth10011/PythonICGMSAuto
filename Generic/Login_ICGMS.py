# import os ; import sys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from Generic.BaseClassICGMS import *

class Login_ICGMS:

    @staticmethod
    def login(admin, Pass):
        # driver.get(url)
        driver.find_element(By.XPATH , "//input[@formcontrolname='email']").send_keys(admin)
        driver.find_element(By.XPATH , "//input[@placeholder='Password']").send_keys(Pass)
        driver.find_element(By.XPATH , "(//button[@type='submit'])[1]").click()