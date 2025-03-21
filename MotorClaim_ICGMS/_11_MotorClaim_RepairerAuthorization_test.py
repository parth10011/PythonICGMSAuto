import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

def test_MotorClaim_RepairAuth():
    # Login
    setUp()
    time.sleep(1)
    User = Insurer_Login.cell(2,1).value
    Pass = Insurer_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)

    ToasterPopupClick()
    time.sleep(0.5)

    # Click on Repairer Authorization button
    repAuth_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[contains(text(),'Repairer Authorization')])[1]"))))
    repAuth_button.click()
    time.sleep(1.5)

    # Enter Pre Approved Amount
    preApprovAmt_text = wait.until((EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))))
    preApprovAmt_text.send_keys(random6Number)

    # Enter Remark
    remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
    remark_text.send_keys("Repairer Authorization Completed")

    # Upload Document File
    document_upload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
    document_upload.send_keys(Doc2_Link)

    # Enter File Name
    fileName_text = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
    fileName_text.send_keys("giveNameFile")

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

    # Click on Submit Button
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    # Open Insurer View List
    insurerViewList_button = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/insurer-claim-list']"))))
    insurerViewList_button.click()
    ToasterPopupClick()
    logOut()