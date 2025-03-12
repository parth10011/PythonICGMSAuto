import time
import keyboard
from selenium.webdriver.support.ui import Select
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(Repairer_Email1 , P2ass)

ToasterPopupClick()
time.sleep(0.5)

# Open Repairer Claim View List
repClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']"))))
repClaimList_link.click()

# Click on Repairer Progress button
repProg_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Repairer Progress'])[1]"))))
repProg_button.click()

# Enter Date Of Completion
dateCompl_datepick = driver.find_element(By.XPATH, "//input[@type='date']")
dateCompl_datepick.send_keys(current_date)

# Enter Remark
remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
remark_text.send_keys("Bills uploaded successfully")

# Upload Repairer Bill
repairerBill_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
repairerBill_fileupload.send_keys(Est_Report)

# Upload Other Bill
otherBill_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
otherBill_fileupload.send_keys(Est_Report)

driver.set_window_size(765,1000)
time.sleep(1)

# Upload Document file
docFile_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[3]")
docFile_fileupload.send_keys(Doc2_Link)

# Enter File Name
fileName_text = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
fileName_text.send_keys("NewFileupload")

# Set Browser to Mobile View
driver.set_window_size(765,1000)

# Close Menu
driver.find_element(By.XPATH, "//i[@class='ti-close']").click()

# Scroll to the particular web element of page
Image = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[3]")
driver.execute_script("arguments[0].scrollIntoView();", Image)
time.sleep(1)

# 
driver.find_element(By.XPATH, "//label[@for='cameraInput0']").click()
time.sleep(1)
keyboard.press_and_release("esc")
time.sleep(1)
driver.maximize_window()

# 
image_fileupload = driver.find_element(By.XPATH, "//input[@accept='image/*']")
image_fileupload.send_keys(Img_Link)
time.sleep(1)

# View Customer Inspection Report
ViewCustReport = driver.find_element(By.XPATH, "//label[text() = 'Customer Inspection report']/following-sibling::button[contains(text(),'View')]")
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

# Click on Confirm Submit Button
confSubmit_button = wait.until((EC.presence_of_element_located((By.XPATH, "//button[text()='Yes, submit it!']"))))
confSubmit_button.click()

# Open Repairer Claim View List
repClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']"))))
repClaimList_link.click()
ToasterPopupClick()
logOut()