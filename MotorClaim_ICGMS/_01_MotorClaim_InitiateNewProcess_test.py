# import sys ; import os
# # Add the parent directory (the root folder) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *

def test_MotorClaim_Initiate():
    # Login
    setUp()
    time.sleep(1)
    custEmail = Cust_Login.cell(2,1).value
    User = Admin_Login.cell(2,1).value
    Pass = Admin_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Initiate Claim
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim']"))).click()
    time.sleep(0.5)

    # Select Product
    product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[1]/div/app-claim-intimation/div[1]/div/div/div[2]/div/div/select'))))
    product.select_by_visible_text("Motor Claim")
    time.sleep(0.5)

    # Select Insurer
    insurerName = MotorClaim_Insurer_Name.cell(2,1).value
    insurer = Select(driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/div[1]/div/app-claim-intimation/div[1]/div/div/div[3]/div/div/select'))
    insurer.select_by_visible_text(insurerName)
    time.sleep(1)

    # // Fill the required details
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@formcontrolname, 'customer_email')]"))).send_keys(custEmail)
    driver.find_element(By.XPATH, "//input[contains(@formcontrolname, 'customer_mobile_no')]").send_keys(randomMobileNumber)
    driver.find_element(By.XPATH, "//input[contains(@formcontrolname, 'policy_number')]").send_keys("MAR"+random6Number)
    driver.find_element(By.XPATH, "//input[contains(@formcontrolname, 'policy_from')]").send_keys("22012024")
    driver.find_element(By.XPATH, "//input[contains(@formcontrolname, 'policy_to')]").send_keys("29012028")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Customer Name')]").send_keys(randomCustomerName)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Repairer Name')]").send_keys(randomRepairerName)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Make')]").send_keys("Honda")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Model')]").send_keys("City")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Type')]").send_keys("Sedan")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Color')]").send_keys(randomColorName)
    driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Enter your remark')])[1]").send_keys("Enter Remark 2")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Registration Number')]").send_keys(randomCarRegNumber)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Repairer Number')]").send_keys(randomRepairerNumber)
    driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Enter your remark')])[2]").send_keys("Enter Remark 1")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Year of Mfg')]").send_keys(randomRegYear)
    ToasterPopupClick()

    # Scroll to the end of page
    Scroll_end = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Submit Details
    submit = driver.find_element(By.XPATH, "//span[text()='Submit']")
    time.sleep(1)
    submit.click()

    ToasterPopupClick()
    logOut()
    time.sleep(1)