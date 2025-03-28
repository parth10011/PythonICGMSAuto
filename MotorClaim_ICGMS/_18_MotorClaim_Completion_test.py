import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

def test_MotorClaim_Complete():
    # Login
    setUp()
    time.sleep(1)
    User = Admin_Login.cell(2,1).value
    Pass = Admin_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Open View List
    view_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']")))
    view_list.click()

    # Completion Button Click
    complete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Completion'])[1]")))
    complete_button.click()

    # Enter Date of Delivery of vehicle
    dateDelivery_datepick = wait.until((EC.presence_of_element_located((By.ID, "vehicle_delivery"))))
    dateDelivery_datepick.send_keys(current_date)

    # Select Process Completed radio button (either yes or no)
    processComplete_radio = driver.find_elements(By.XPATH, "//input[@value='yes'] | //input[@value='no']")
    random.choice(processComplete_radio).click()
    time.sleep(1)

    # Click on Submit Button
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()
    ToasterPopupClick()

    # Open Claim View List
    view_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']")))
    view_list.click()
    logOut()