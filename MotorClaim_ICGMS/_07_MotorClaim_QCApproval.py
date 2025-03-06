import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(a1dmin , P2ass)

ToasterPopupClick()
time.sleep(0.5)

# Open View List
driver.find_element(By.XPATH, "//a[@href='/claim-details']").click()

# Click On QC Approval Button
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='QC Approval'])[1]"))).click()
time.sleep(0.5)

# Enter Remark
remark = driver.find_element(By.XPATH , "//textarea[@placeholder='Enter Your Remark']")
remark.send_keys("Approval OK Successfull")

# Click On Submit Button
submit = driver.find_element(By.XPATH, "//span[text()='Approve']")
submit.click()
time.sleep(1)

ToasterPopupClick()

# Open View List
driver.find_element(By.XPATH, "//a[@href='/claim-details']").click()
logOut()