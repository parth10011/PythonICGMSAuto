import sys ; import os
# Add the parent directory (the root folder) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

def test_PreInsp_QC():
    # Login
    setUp()
    time.sleep(1)
    User = Admin_Login.cell(2,1).value
    Pass = Admin_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Open View List
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']"))).click()
    time.sleep(0.5)

    # Quality Check button Click
    qualityCheck_Button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Quality Check'])[1]"))))
    qualityCheck_Button.click()

    # Locate And Reach Enter Details Column
    enterDet_text = driver.find_element(By.XPATH, "//label[text()='Enter Details']")
    driver.execute_script("arguments[0].scrollIntoView(true);", enterDet_text)

    # Enter Chassis Number Details
    chassis_input = wait.until(EC.presence_of_element_located((By.ID, "chassisNumber")))
    chassis_input.send_keys("MBHEWB22SLA435287")

    # Enter Engine Number Details
    engine_input = driver.find_element(By.ID, "engineNumber")
    engine_input.send_keys("ENGINE00202")

    # Enter Aadhar Number Details
    aadhar_input = driver.find_element(By.ID, "aadharNumber")
    aadhar_input.send_keys("987654646456")

    # Enter PAN Number Details
    pan_input = driver.find_element(By.ID, "panNumber")
    pan_input.send_keys("CFQPJ5545G")

    # Select Chasis Number Tampered radio button
    chassisTamp_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_chassis_no_tempered']")
    random.choice(chassisTamp_radio).click()

    # Select Chasis Number mismatch with RC / Parivahan data radio button
    chassisMismatch_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_chassis_no_mismatch']")
    random.choice(chassisMismatch_radio).click()

    # Select Is there any change in class of vehicle to that mentioned in RC / Parivahan data radio button
    changeClassRc_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_change_in_rc']")
    random.choice(changeClassRc_radio).click()

    # Select Engine found running radio button
    engineRun_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_engine_running']")
    random.choice(engineRun_radio).click()

    # Select Age of vehicle as on date of inspection as per UW approval radio button
    ageVehicle_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='is_age_of_vehicle']")
    random.choice(ageVehicle_radio).click()
    time.sleep(2)

    # Select Image Type dropdown
    imageType_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='imageType']/option[@value!='']")
    random.choice(imageType_dropdown).click()
    time.sleep(0.5)

    # Select Component Type dropdown
    component_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='component']/option[@value!='']")))
    random.choice(component_dropdown).click()
    time.sleep(0.5)

    # Select Damage Noticed radio button
    damageNot_radio = driver.find_elements(By.XPATH, "//input[@formcontrolname='action']")
    random.choice(damageNot_radio).click()
    time.sleep(0.5)

    # Enter Remark
    remark_text = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Enter Your Remark']")
    remark_text.send_keys("QC is Successful and Approved")

    # Click on Approve Button
    approve_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Approve']")))
    approve_button.click()
    ToasterPopupClick()

    # Open View List
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']"))).click()
    time.sleep(2)

    # Download Pre Inspection pdf
    DownCustReport = wait.until(EC.presence_of_element_located((By.XPATH, "//th[text()='1']/following-sibling::td//i[@ngbtooltip='Download Acknowledged Report']")))
    DownCustReport.click()
    ToasterPopupClick()
    logOut()
# test_PreInsp_QC()