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

# Click on Bill Verification button
billVer_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Bill Verification'])[1]"))))
billVer_button.click()

# View Inspection Report
viewInspecReport_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='View'])[1]"))))
viewInspecReport_button.click()
ToasterPopupClick()

# Close Inspection Report
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Inspection Report
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[1]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Inspection Key Report
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[2]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Inspection Key Report
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Inspection Key Report
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[2]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Repairer Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[3]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Repairer Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Repairer Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[3]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Other Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[4]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Other Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Other Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[4]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Final Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[5]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Final Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Final Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[5]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Surveyor Survey Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[6]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Surveyor Survey Bill Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Surveyor Survey Bill Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[6]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Optional Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[7]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Optional Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Optional Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[7]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Surveyor Other Bill Doc
viewInspecReport_button = driver.find_element(By.XPATH, "(//button[text()='View'])[8]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Surveyor Other Bill Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Surveyor Other Bill Doc
DownCustReport = driver.find_element(By.XPATH, "(//button[text()='Download'])[8]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# View Customer Inspection Doc
viewInspecReport_button = driver.find_element(By.XPATH, "//label[text()='Customer Inspection report']/following-sibling::button[contains(text(),'View')]")
viewInspecReport_button.click()
ToasterPopupClick()

# Close Customer Inspection Doc
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()

# Download Customer Inspection Doc
DownCustReport = driver.find_element(By.XPATH, "//label[text()='Customer Inspection report']/following-sibling::button[contains(text(),'Download')]")
DownCustReport.click()
ToasterPopupClick()
time.sleep(1)

# Enter Remark
remark_text = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Remark']")
remark_text.send_keys("All bills viewed and downloaded successfully")

# Click on Approve Button
approve_button = driver.find_element(By.XPATH, "//span[text()='Approve']")
approve_button.click()

# Open Surveyor Claim View List
survClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/surveyor-claim-list']"))))
survClaimList_link.click()
ToasterPopupClick()
logOut()