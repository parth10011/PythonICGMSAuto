# import sys , os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import random 
import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(a1dmin , P2ass)
ToasterPopupClick()

# Click On Registration
wait.until((EC.presence_of_element_located((By.XPATH, "//span[text()='Registration ']")))).click()

# Insurer Basic Details Fill
def BasicDetails_Input():
    # Click on Insurer
    driver.find_element(By.PARTIAL_LINK_TEXT, "Insurer").click()
    time.sleep(0.5)

    # Click on Add New Insurer
    driver.find_element(By.CSS_SELECTOR, "button[ngbtooltip='Add New']").click()

    # Enter Insurer Name
    insuredName_input = wait.until((EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Insurer Name']"))))
    insuredName_input.send_keys(InsuredName)

    # Enter Brand Name
    brandName_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Brand Name']")
    brandName_input.send_keys(randomCustomerName)

    # Select Insurer Type
    insureType = Select(driver.find_element(By.XPATH, "//select[@id='type_of_insurer']"))
    insureType.select_by_visible_text("PRIVATE")

    # Click on Product Name Dropdown
    driver.find_element(By.XPATH, "//div[@aria-haspopup='listbox']").click()

    # Select a random Product Name
    options_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ng-dropdown-panel//div[@role='option']")))
    random.choice(options_list).click()

    # Enter GST Number
    gstNumber = driver.find_element(By.XPATH, "//input[@placeholder='Enter Number']")
    gstNumber.send_keys("45AFZPK7190K5Z0")

    # Enter PAN Number
    pan_Number = driver.find_element(By.XPATH, "//input[@placeholder='Enter Pan Number']")
    pan_Number.send_keys("ABCDE1237D")

    # Upload GST Document
    gst_doc = driver.find_element(By.ID, "gstCopy")
    gst_doc.send_keys(Gst_Doc)

    # Upload PAN Document
    pan_doc = driver.find_element(By.ID, "panCopy")
    pan_doc.send_keys(Pan_Doc)

    # Enter Email Address
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
    email_input.send_keys(randomBasicEmail)

    # Enter Phone Number
    phone_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Personal Phone Number']")
    phone_input.send_keys(randomMobileNumber)

    # Enter Alternate Phone Number
    alternative_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Alternate Number']")
    alternative_input.send_keys(randomAltNumber)

    # Enter Number of Permitted Users
    permUsers_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Permitted Users']")
    permUsers_input.send_keys("3")

    # Enter Brand Code
    brandCode_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Brand Code']")
    brandCode_input.send_keys("MOSA")

BasicDetails_Input()

# Address Details Fill
def AddressDetail():

    # Enter Registered Office Address
    regOfficeAddr_input= driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Address']")
    regOfficeAddr_input.send_keys("uiehrsjbf nsdkjfskf 324353")

    # Select Country Name
    country_dropdown = Select(driver.find_element(By.ID, "country_id"))
    country_dropdown.select_by_visible_text("India")
    time.sleep(0.5)

    # Select Random State Name
    state_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='state_id']//option[@value>='1']")))
    random.choice(state_dropdown).click()
    time.sleep(0.5)

    # Select Random City Name
    city_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='city_id']//option[@value>='1']")))
    random.choice(city_dropdown).click()
    time.sleep(0.5)

    # Select Random Zone Name
    zone_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='zone_id']//option[@value>='1']")
    random.choice(zone_dropdown).click()

     # Enter Latitude
    lat_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Latitude']")
    lat_input.send_keys(latitude)

    # Enter Longitude
    long_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Longitude']")
    long_input.send_keys(longitude)

    # Enter PIN Code
    pinCode_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter PIN Code']")
    pinCode_input.send_keys(random6Number)
    time.sleep(1)

    # Click On Save Button
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    ToasterPopupClick()

AddressDetail()

def ContactDetails_Input():
    # Click on Insurer
    driver.find_element(By.PARTIAL_LINK_TEXT, "Insurer").click()
    time.sleep(0.5)

    # Click on Edit Insurer Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on Contact Details
    driver.find_element(By.XPATH, "//button[text()=' Contact Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Enter Name in Add New Contact
    name_Input = wait.until((EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Name']"))))
    name_Input.send_keys(randomCustomerName)
    time.sleep(0.5)

    # Select Random Department
    department_Input = driver.find_elements(By.XPATH, "//select[@formcontrolname='department_id']//option[@value>'0']")
    random.choice(department_Input).click()
    time.sleep(0.5)

    # Select Random Designation
    designation_Input = driver.find_elements(By.XPATH, "//select[@formcontrolname='designation_id']//option[@value>'0']")
    random.choice(designation_Input).click()

    # Enter Email ID
    email_Input = driver.find_element(By.ID, "email_id")
    email_Input.send_keys(randomContactEmail)

    # Enter Contact Number
    contact_Input = driver.find_element(By.XPATH, "//input[@placeholder= 'Enter Contact Number']")
    contact_Input.send_keys(randomMobileNumber)

    # Enter Alternate Number
    alternate_Input = driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Alternate Number']")
    alternate_Input.send_keys(randomAltNumber)

    # Click On Add New Button
    add_Button = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    add_Button.click()
    ToasterPopupClick()

ContactDetails_Input()

def UserDetails_Input():
    # Click on Insurer
    driver.find_element(By.PARTIAL_LINK_TEXT, "Insurer").click()
    time.sleep(0.5)

    # Click on Edit Insurer Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on User Details
    driver.find_element(By.XPATH, "//button[text()=' User Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Enter First Name in Add New User
    firstName_Input = wait.until((EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='first_name']"))))
    firstName_Input.send_keys(getrandomname())
    time.sleep(0.5)

    # Enter Last Name in Add New User
    lastName_Input = wait.until((EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='last_name']"))))
    lastName_Input.send_keys("random")

    # Select Department dropdown
    dept_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='department_id']/option[@value != '']")
    random.choice(dept_dropdown).click()

    # Select Designation dropdown
    desig_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='designation_id']/option[@value != '']")
    random.choice(desig_dropdown).click()

    # Enter Email Id
    email_input = driver.find_element(By.ID, "email_id")
    email_input.send_keys(randomUserEmail)

    # Enter Phone Number
    phoneNumb_input = driver.find_element(By.ID, "contact_number")
    phoneNumb_input.send_keys(randomMobileNumber)

    # Select User Type
    userType_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname = 'role_type']/option[@value != '']")
    random.choice(userType_dropdown).click()
    
    # Enter Branch Name
    branchName_input = driver.find_element(By.ID, "branch_name")
    branchName_input.send_keys("LpAxQeR")

    # Enter Branch Code
    branchCode_input = driver.find_element(By.ID, "branch_code")
    branchCode_input.send_keys("1Q2W3E4R5T6Y7U")
    time.sleep(1)

    # Click on Add Button
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]//preceding-sibling::button")
    add_button.click()
    ToasterPopupClick()
    time.sleep(1)
    ToasterPopupClick()
    logOut()

UserDetails_Input()