import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(Cust_Email1 , P2ass)
ToasterPopupClick()

# Open View Details
view_details = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='View Details'])[3]")))
view_details.click()
time.sleep(1)

# Fill the required details
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Date of inward' or @placeholder='Date of inward']"))).send_keys("22122009")
driver.find_element(By.XPATH, "(//input[@placeholder='dd/mm/yyyy'])[3]").send_keys("22122025")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Insured Name']").send_keys("Write Your Name Below")
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Address for Communication']").send_keys("Rohtak Road , Banaras")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Pincode']").send_keys("112213")
driver.find_element(By.XPATH, "//input[@placeholder='Enter PAN Number']").send_keys("DL986GVK6F")
driver.find_element(By.XPATH, "(//input[@placeholder='dd/mm/yyyy'])[4]").send_keys("22122022")

# Choose location on map
loc = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='address_map']")))
loc.click()
close_loc = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_loc.click()

# Signature
Sigarea = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Sign here.........' or @placeholder='  ']")))
Sigarea.click()
time.sleep(1)

canvas = driver.find_element(By.XPATH, "//canvas[@width='700' and @height='200']")
canvas.click()
time.sleep(1)

submit_sign = driver.find_element(By.XPATH, "//button[text()='Submit the signature']")
submit_sign.click()

close_sign = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_sign.click()
time.sleep(1)

# PAN CARD Upload
PAN_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[1]")
PAN_input.send_keys(Doc_Link)
time.sleep(0.5)

# Aadhar Card Upload
Aadhar_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[2]")
Aadhar_input.send_keys(Doc_Link)
time.sleep(0.5)

# Passport Upload
Passport_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[3]")
Passport_input.send_keys(Doc_Link)
time.sleep(0.5)

# Voter ID Upload
Voter_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[4]")
Voter_input.send_keys(Doc_Link)
time.sleep(0.5)

# DL Upload
DL_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[5]")
DL_input.send_keys(Doc_Link)
time.sleep(0.5)

# RC Upload
RC_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[6]")
RC_input.send_keys(Doc_Link)
time.sleep(0.5)

# Insurance Upload
Insurance_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[7]")
Insurance_input.send_keys(Doc_Link)
time.sleep(0.5)

# GovID Upload
GovID_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[8]")
GovID_input.send_keys(Doc_Link)
time.sleep(0.5)

# Other 1 Upload
Other1_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[9]")
Other1_input.send_keys(Doc_Link)
time.sleep(0.5)

# Other 2 Upload
Other2_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[10]")
Other2_input.send_keys(Doc_Link)
time.sleep(0.5)

# Repairer Estimation Upload
Repairer_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[11]")
Repairer_input.send_keys(Doc_Link)
time.sleep(0.5)

# FIR Upload
FIR_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[12]")
FIR_input.send_keys(Doc_Link)
time.sleep(0.5)

# Other 3 Upload
Other3_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[13]")
Other3_input.send_keys(Doc_Link)
time.sleep(1)

# Submit Customer Form
submit = driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
submit.click()
time.sleep(5)
# time.sleep(10)

ToasterPopupClick()

logOut()