import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test_MotorClaim_SurvAppoint():
    # Login
    setUp()
    time.sleep(1)
    User = Insurer_Login.cell(2,1).value
    Pass = Insurer_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)

    ToasterPopupClick()
    time.sleep(0.5)

    # Click on Surveyor Appointment button
    SurvAppoint_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[contains(text(),'Surveyor Appointment')])[1]"))))
    SurvAppoint_button.click()
    time.sleep(1.5)

    # Select Surveyor Name Dropdown
    SurvName_dropdown = Select(wait.until((EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='surveyor_id']")))))
    SurvName_dropdown.select_by_visible_text("Surveyor Phase I Corporation")
    # SurvName_dropdown.select_by_visible_text("Ehtasham Husain")

    # Enter Date Of Visit
    dateVisit_datepick = driver.find_element(By.XPATH, "//input[@type='date']")
    dateVisit_datepick.send_keys(current_date)

    # Enter Time Of Visit
    timeVisit_timepick = driver.find_element(By.XPATH, "//input[@type='time']")
    timeVisit_timepick.send_keys(current_time)

    # Enter Remark
    remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
    remark_text.send_keys("Surveyor Appointed Successfuly")

    # View Customer Inspection Report
    ViewCustReport = driver.find_element(By.XPATH, "//button[text()=' View ']")
    ViewCustReport.click()
    ToasterPopupClick()

    # Close Customer Inspection Report
    close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
    close_button.click()

    # Download Customer Inspection Report
    DownCustReport = driver.find_element(By.XPATH, "//button[text()=' Download ']")
    DownCustReport.click()
    ToasterPopupClick()
    time.sleep(2)

    # Click on Appoint Button
    appoint_button = driver.find_element(By.XPATH, "//span[text()='Appoint']")
    appoint_button.click()

    # Open Insurer View List
    insurerViewList_button = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/insurer-claim-list']"))))
    insurerViewList_button.click()
    ToasterPopupClick()
    logOut()
 
# test_MotorClaim_SurvAppoint()