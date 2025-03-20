# import sys ; import os
# Add the parent directory (the root folder) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Login
setUp()
time.sleep(1)
custEmail = Cust_Login.cell(2,1).value
User = Admin_Login.cell(2,1).value
Pass = Admin_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)
ToasterPopupClick()

# Initiate Claim
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim']"))).click()
time.sleep(0.5)

# Select Product
product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Product']/following-sibling::div/select"))))
product.select_by_visible_text("Motor Pre Inspection")
time.sleep(0.5)

# Select Type
typeName = PreInspection_Type_Name.cell(2,1).value
type = Select(driver.find_element(By.XPATH, "//label[text()='Type']/following-sibling::div/select"))
type.select_by_visible_text(typeName)
print(typeName)
time.sleep(1)

# Fill the required details
wait.until((EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='customer_email']")))).send_keys(custEmail)
driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='customer_mobile_no']").send_keys(randomMobileNumber)
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Customer Name')]").send_keys(randomCustomerName)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Vehicle Number']").send_keys(randomCarRegNumber)
driver.find_element(By.XPATH, "//input[@placeholder='Enter State']").send_keys(randomStateName)
driver.find_element(By.XPATH, "//input[@placeholder='Enter year of mfg']").send_keys(randomRegYear)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Fuel Type']").send_keys(randomFuelType)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Make']").send_keys("Maruti")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Model']").send_keys("800")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Rreference number']").send_keys(current_date+"MARCH")
driver.find_element(By.XPATH, "//input[@placeholder='Enter City']").send_keys("NULL DATA")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Branch Name']").send_keys("New Road House")
driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Enter your remark')])[1]").send_keys("Please Enter Remark 2")
driver.find_element(By.XPATH, "(//input[contains(@placeholder,'Enter your remark')])[2]").send_keys("Please Enter Remark 1")
ToasterPopupClick()
time.sleep(1)

# Scroll to the end of page
Scroll_end = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Submit Details
submit = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit.click()
ToasterPopupClick()
time.sleep(1)

# Open View List
viewList_button = driver.find_element(By.XPATH, "//span[contains(text(),'View List')]")
viewList_button.click()
logOut()