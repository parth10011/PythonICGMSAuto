import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(Repairer_Email1 , P2ass)
ToasterPopupClick()

# Open View List
claim_list = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']")))
claim_list.click()

# Open Repairer Report
report_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[text()='Repairer Report'])[1]")))
report_button.click()

# Enter Amount for repair
amt_rep = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Amount']")))
amt_rep.send_keys("6433")

# Enter Days for repair
days_rep = driver.find_element(By.XPATH, "//input[@placeholder='Enter Required number of days']")
days_rep.send_keys("20")

# Upload Estimation Report
report_upload = driver.find_element(By.XPATH, "//input[@accept='application/pdf']")
report_upload.send_keys(Est_Report)

# Enter Remark
remark = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Your Remark']")
remark.send_keys("Ok Go Ahead")

# Upload Document Files
doc_upload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
doc_upload.send_keys(Doc2_Link)

# Enter File Name
file_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter filename']")
file_name.send_keys("Dummy2point0")

# View Customer Inspection Report
view_button = driver.find_element(By.XPATH, "//button[text()=' View ']")
view_button.click()

ToasterPopupClick()

# Close Button Click
close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_button.click()
time.sleep(1)

# Click Submit
submit = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit.click()

ToasterPopupClick()

# Open View List
claim_list = driver.find_element(By.XPATH, "//a[@href='/repairer-claim-list']")
claim_list.click()

logOut()
# time.sleep(10)