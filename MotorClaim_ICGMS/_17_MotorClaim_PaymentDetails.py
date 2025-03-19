import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

# Login
setUp()
time.sleep(1)
User = Insurer_Login.cell(2,1).value
Pass = Insurer_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)

ToasterPopupClick()
time.sleep(0.5)

# Payment Details Button click
payDetails_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Payment Details'])[1]"))))
payDetails_button.click()

# Enter Amount Paid by Repairer
amtPaidRep_text = wait.until((EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='amountPaid']"))))
amtPaidRep_text.send_keys(random6Number)

# Enter Date of Payment by Repairer
datePayRep_datepick = driver.find_element(By.XPATH, "//input[@formcontrolname='dateOfPayment']")
datePayRep_datepick.send_keys(current_date)

# Select random Mode Of Payment by Repairer
modePayRep = driver.find_elements(By.XPATH, "//select[@formcontrolname='paymentMode']//option[@value !='']")
random.choice(modePayRep).click()

# Enter Repairer Reference Number
refRepNumb_text = driver.find_element(By.XPATH, "//input[@formcontrolname='refNumber']")
refRepNumb_text.send_keys("ABCD1234")

# Enter Repairer Remark
repRemark = driver.find_element(By.XPATH, "//textarea[@formcontrolname='paymentRemarks']")
repRemark.send_keys("Payment Repair Records Completed")

# Enter Amount Paid by Surveyor
amtPaidSurv_text = wait.until((EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='surveyoramountPaid']"))))
amtPaidSurv_text.send_keys(random6Number)

# Enter Date of Payment by Surveyor
datePaySurv_datepick = driver.find_element(By.XPATH, "//input[@formcontrolname='surveyordateOfPayment']")
datePaySurv_datepick.send_keys(current_date)

# Select random Mode Of Payment by Surveyor
modePaySurv = driver.find_elements(By.XPATH, "//select[@formcontrolname='surveyorpaymentMode']//option[@value!='']")
random.choice(modePaySurv).click()

# Enter Surveyor Reference Number
refSurvNumb_text = driver.find_element(By.XPATH, "//input[@formcontrolname='surveyorrefNumber']")
refSurvNumb_text.send_keys("EFGH5678")

# Enter Surveyor Remark
survRemark = driver.find_element(By.XPATH, "//textarea[@formcontrolname='surveyorpaymentRemarks']")
survRemark.send_keys("Payment Survey Records Completed")

# Upload Document File
document_upload = driver.find_element(By.XPATH, "//td//input[@type='file']")
document_upload.send_keys(Doc2_Link)

# Enter File Name
fileName_text = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
fileName_text.send_keys("OptionalFileOfPAymentDetails")

# Click on Submit Button
submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()
ToasterPopupClick()

# Open Claim View List
claimList_button = driver.find_element(By.XPATH ,"//a[@href='/insurer-claim-list']")
claimList_button.click()
logOut()