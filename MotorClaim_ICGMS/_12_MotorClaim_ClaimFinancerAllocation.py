import time
from selenium.webdriver.support.ui import Select
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
User = Repair_Login.cell(2,1).value
Pass = Repair_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)

ToasterPopupClick()
time.sleep(0.5)

# Open Repairer Claim View List
repClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']"))))
repClaimList_link.click()

# Click on Claim Financer Allocation button
claimFinAlloc_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Claim Financier Allocation'])[1]"))))
claimFinAlloc_button.click()
time.sleep(1.5)

# Click on Claim Financier needed radio button
driver.find_element(By.XPATH, "//input[@formcontrolname='is_financier_required' and @value='yes']").click()

financType_dropdown = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='financier_id']"))
financType_dropdown.select_by_visible_text("Parth Corporation")

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

# Click on Appoint Button
appoint_button = driver.find_element(By.XPATH, "//span[text()='Appoint']")
appoint_button.click()

# Open Repairer Claim View List
repClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']"))))
repClaimList_link.click()
ToasterPopupClick()
logOut()