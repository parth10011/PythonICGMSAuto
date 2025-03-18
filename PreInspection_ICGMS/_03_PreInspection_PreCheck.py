# import sys ; import os
# Add the parent directory (the root folder) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(a1dmin , P2ass)
ToasterPopupClick()

# Open View List
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']"))).click()
time.sleep(0.5)

# Pre Check button Click
preCheck_Button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Pre Check'])[1]"))))
preCheck_Button.click()

# Giving time to load the page
wait.until((EC.presence_of_element_located((By.XPATH, "//label[text()='Self Inspection (By Customer)']"))))
time.sleep(0.5)

# Photos Available Radio Button Click
photoAvail_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_all_photo_available']")
random.choice(photoAvail_radio).click()

# Photos Clarity Radio Button Click
photoClarity_radio = driver.find_elements(By.XPATH,"//input[@formcontrolname='is_photo_clarity_good']")
random.choice(photoClarity_radio).click()

# Registeration Certificate Radio Button Click
regCert_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_reg_cert_enclosed']")
random.choice(regCert_radio).click()

# Previous Policy Radio Button Click
prevPolicy_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_policy_enclosed']")
random.choice(prevPolicy_radio).click()
time.sleep(1)

# Click on Submit Button
submit_button = driver.find_element(By.XPATH, "//span[text()='Approve']")
submit_button.click()
ToasterPopupClick()
logOut()