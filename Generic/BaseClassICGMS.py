import random
import unittest
import time
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

def logOut():
       
       Profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-toggle='dropdown']")))
       Profile.click()
       logout = driver.find_element(By.XPATH , "//a[@style='cursor: pointer;']")
       logout.click()

       ToasterPopupClick()

       driver.get(emailer_url)
       time.sleep(2.5)


def generate_random_mobile_number():
    n = ["9", "8", "7", "6"]
    n1 = random.choice(n)  # Indian mobile number starting with 9, 8, 7, 6
    mobile_number = [n1] + [str(random.randint(0, 9)) for _ in range(9)]
    return "".join(mobile_number)
randomMobileNumber = generate_random_mobile_number()
randomRepairerNumber = generate_random_mobile_number()
# Example usage
print(generate_random_mobile_number())

    #    if (driver != null):
              
    #    driver.quit()