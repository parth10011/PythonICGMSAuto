import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from Generic.InitiateNewProcess_details import *
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\chromedriver.exe"  # Path to ChromeDriver
options = Options()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# class Basetest(unittest.TestCase):
def setUp():

        """Set up the browser before each test."""
        driver.maximize_window()
        driver.get(url)

    # def tearDown(self):
    #     """Quit the browser after each test."""
    #     self.driver.quit()

def ToasterPopupClick():
       
       toaster = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='alert']")))
       toaster.click()