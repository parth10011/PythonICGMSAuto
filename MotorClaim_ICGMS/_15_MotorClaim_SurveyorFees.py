import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
User = Surveyor_Login.cell(2,1).value
Pass = Surveyor_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)

ToasterPopupClick()
time.sleep(0.5)

# Open Surveyor Claim View List
survClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/surveyor-claim-list']"))))
survClaimList_link.click()

# Click on Surveyor Fee button
survFee_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Surveyor Fees'])[1]"))))
survFee_button.click()

# Upload Surveyor Bill
surveyBill_upload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
surveyBill_upload.send_keys(Est_Report)

# Upload Other Bill
otherBill_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
otherBill_fileupload.send_keys(Est_Report)

# Enter Remark
remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
remark_text.send_keys("Surveyor Bills Uploaded successfully")

# Upload Document File
document_upload = driver.find_element(By.XPATH, "(//input[@type='file'])[3]")
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

# Open Surveyor Claim View List
survClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/surveyor-claim-list']"))))
survClaimList_link.click()
ToasterPopupClick()
logOut()