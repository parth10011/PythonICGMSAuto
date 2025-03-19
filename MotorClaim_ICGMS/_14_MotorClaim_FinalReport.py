import time
import keyboard
from selenium.webdriver.support.ui import Select
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

# Click on Final Report button
finalReport_button = wait.until((EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Final Report')][1]"))))
finalReport_button.click()

# View Customer Inspection Report
ViewCustReport = wait.until((EC.visibility_of_element_located((By.XPATH, "//button[text()=' View ']"))))
ViewCustReport.click()
ToasterPopupClick()

# Close Customer Inspection Report
close_button = wait.until((EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Close']"))))
close_button.click()

# Download Customer Inspection Report
DownCustReport = driver.find_element(By.XPATH, "//button[text()=' Download ']")
DownCustReport.click()
ToasterPopupClick()
time.sleep(2)

# Upload Final Report
finalReport_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
finalReport_fileupload.send_keys(Est_Report)

# Enter Remark
remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
remark_text.send_keys("Final Report Uploaded Successfuly")

# Upload Document file
docFile_fileupload = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
docFile_fileupload.send_keys(Doc2_Link)

# Enter File Name
fileName_text = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
fileName_text.send_keys("File98234y")

# Set Browser to Mobile View
driver.set_window_size(765,1000)

# Close Menu
driver.find_element(By.XPATH, "//i[@class='ti-close']").click()

# Scroll to the particular web element of page
Image = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[2]")
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
ToasterPopupClick()
time.sleep(1)

# Click on Submit Button
submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()

# Open Surveyor Claim View List
survClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/surveyor-claim-list']"))))
survClaimList_link.click()
ToasterPopupClick()
logOut()