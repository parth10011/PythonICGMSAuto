import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(Insurer_Email1 , P2ass)

ToasterPopupClick()
time.sleep(0.5)

# Insurer Verification Button click
InsurerVeri_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Insurer Verification'])[1]"))))
InsurerVeri_button.click()

# Enter Claim Number
ClaimNumb_text = wait.until((EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='claim_number']"))))
ClaimNumb_text.send_keys("")

# Enter Remark
remark_text = driver.find_element(By.XPATH ,"//textarea[@placeholder='Enter Your Remark']")
remark_text.send_keys("Approval Done")
time.sleep(2)

# Click on Self Inspection To Be Considered Radio Button
selfReport_radio = driver.find_element(By.XPATH, "//input[@value='no']")
selfReport_radio.click()

# Upload Document
Doc_upload = driver.find_element(By.XPATH, "//input[@accept='application/pdf']")
Doc_upload.send_keys(Doc2_Link)

# # Enter File Name
fileName_text = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
fileName_text.send_keys("d4e5Dummy.a1b2c3pdf")

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

# Click on Approve Button
approve_button = driver.find_element(By.XPATH, "//span[text()='Approve']")
approve_button.click()
ToasterPopupClick()

# Open Claim View List
claimList_button = driver.find_element(By.XPATH ,"//a[@href='/insurer-claim-list']")
claimList_button.click()
logOut()