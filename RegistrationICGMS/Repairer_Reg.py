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
User = Admin_Login.cell(2,1).value
Pass = Admin_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)
ToasterPopupClick()

# Click On Registration
wait.until((EC.presence_of_element_located((By.XPATH, "//span[text()='Registration ']")))).click()

# Click on Repairer
driver.find_element(By.PARTIAL_LINK_TEXT, "Repairer").click()
time.sleep(0.5)

def BasicDetails_Input():
    # Click on Add New Button
    addNew_button = driver.find_element(By.XPATH, "//button[text()='Add New']")
    addNew_button.click()

    # Enter Service Center Name
    scName_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='scName']")))
    scName_input.send_keys(getrandomname())

    # Enter Address
    addr_input = driver.find_element(By.XPATH, "//input[@formcontrolname='address']")
    addr_input.send_keys("ivm pofewpjf 2422")

    # Enter Pin Code
    pinCode_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pinCode']")
    pinCode_input.send_keys(random6Number)

    # Select Country Name dropdown
    country_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "country"))))
    country_dropdown.select_by_visible_text("India")

    # Select State Name dropdown
    state_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='state']/option[@value!= '']")))
    random.choice(state_dropdown).click()

    # Select City Name dropdown
    city_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='city']/option[@value!= '']")))
    random.choice(city_dropdown).click()

    # Select zone dropdown
    zone_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='zone']/option[@value!= '']")))
    random.choice(zone_dropdown).click()

    # Enter Latitude Coordinate
    latitude_input = driver.find_element(By.XPATH, "//input[@formcontrolname='latitude']")
    latitude_input.send_keys(latitude)

    # Enter Longitude Coordinate
    longitude_input = driver.find_element(By.XPATH, "//input[@formcontrolname='longitude']")
    longitude_input.send_keys(longitude)

    # Enter Email
    email_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    email_input.send_keys(getRandomEmail())

    # Enter Mobile Number
    mobileNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='mobile']")
    mobileNumber_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Mobile Number
    altNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='altMobile']")
    altNumber_input.send_keys(generate_random_mobile_number())

    # Select Category Dropdown
    category_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname = 'category']/option[@value !='']")))
    random.choice(category_dropdown).click()

    # Enter Permitted Number Of Users
    permUsers_input = driver.find_element(By.XPATH, "//input[@formcontrolname='permitted_users']")
    permUsers_input.send_keys("8")
BasicDetails_Input()

def RepairDocs_Input():

    # Enter Gst Number
    gstNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='gstNo']")
    gstNumb_input.send_keys("435345435435435")

    # Enter PAN Number
    panNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='panNo']")
    panNumb_input.send_keys("DLOB274892")

    # Upload PAN Copy Document
    panCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='pan_file']")
    panCopyDoc_fileupload.send_keys(panCopy_Link)

    # Upload Gst Copy Document
    gstCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='gst_file']")
    gstCopyDoc_fileupload.send_keys(gstCopy_Link)
    time.sleep(1)

    # Click on Save Button
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
    save_button.click()
    ToasterPopupClick()
    time.sleep(1)
    ToasterPopupClick()

RepairDocs_Input()

def RepairContactDetails_Input():

    # Click on Eye Button 
    eye_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@ngbtooltip='View'])[1]")))
    eye_button.click()
    time.sleep(1)

    # Click on Contact Details Button
    repairContact_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Contact Details')]")
    repairContact_button.click()
    ToasterPopupClick()

    # Click on Add New contact details button
    addNewContact_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add New')]")))
    addNewContact_button.click()

    # Enter Name in Add New Contact
    nameRepContact_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))
    nameRepContact_input.send_keys(getrandomname())

    # Select Department dropdown in Add New Contact
    departmentRepContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='department_id']/option[@value !='' ]")))
    random.choice(departmentRepContact_dropdown).click()

    # Select Designation dropdown in Add New Contact
    designationRepContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='designation_id']/option[@value !='' ]")))
    random.choice(designationRepContact_dropdown).click()

    # Enter Contact Number in Add New Contact
    contactNumberContact_input = driver.find_element(By.ID, "contact_number")
    contactNumberContact_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Number in Add New Contact
    altNumberContact_input = driver.find_element(By.ID, "alt_contact_number")
    altNumberContact_input.send_keys(generate_random_mobile_number())

    # Enter Email ID in Add New Contact
    emailIDContact_input = driver.find_element(By.ID, "email_id")
    emailIDContact_input.send_keys(getRandomEmail())
    time.sleep(1)

    # Click on Add Button
    addContact_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]/preceding-sibling::button[contains(text(),'Add')]")
    addContact_button.click()
    ToasterPopupClick()
    time.sleep(0.3)
    ToasterPopupClick()
    time.sleep(0.3)
    ToasterPopupClick()

    # Click on Repairer Registration List
    driver.find_element(By.PARTIAL_LINK_TEXT, "Repairer").click()

RepairContactDetails_Input()

def RepairUserDetails_Input():

    # Click on Eye Button 
    eye_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@ngbtooltip='View'])[1]")))
    eye_button.click()
    time.sleep(1)

    # Click on User Details Button
    repairUser_button = driver.find_element(By.XPATH, "//button[contains(text(), 'User Details')]")
    repairUser_button.click()
    ToasterPopupClick()

    # Click on Add New user details button
    addNewUser_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add New')]")))
    addNewUser_button.click()

    # Enter First Name in Add User Detail
    firstNameUser_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='first_name']")))
    firstNameUser_input.send_keys(getrandomname())

    # Enter Last Name in Add User Detail
    lastNameUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']")
    lastNameUser_input.send_keys("CODE")

    # Select Department dropdown in Add New User
    departmentRepUser_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='department_id']/option[@value !='' ]")))
    random.choice(departmentRepUser_dropdown).click()

    # Select Designation dropdown in Add New User
    designationRepUser_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='designation_id']/option[@value !='' ]")))
    random.choice(designationRepUser_dropdown).click() 

    # Enter Email ID in Add New User
    emailIDUser_input = driver.find_element(By.ID, "email_id")
    emailIDUser_input.send_keys(getRandomEmail())

    # Enter Phone Number in Add New User
    phoneNumberContact_input = driver.find_element(By.ID, "contact_number")
    phoneNumberContact_input.send_keys(generate_random_mobile_number())

    # Select User Type dropdown
    userType_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname = 'role_type']/option[@value !='']")))
    random.choice(userType_dropdown).click()

    # Enter Branch Name in Add New User
    branchNameUser_input = driver.find_element(By.ID, "branch_name")
    branchNameUser_input.send_keys("BBRRAAANNCCHH")

    # Enter Branch Code in Add New User
    branchCodeUser_input = driver.find_element(By.ID, "branch_code")
    branchCodeUser_input.send_keys("BBR019228")

    # Click on Add Button
    addUser_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]/preceding-sibling::button[contains(text(),'Add')]")
    addUser_button.click()

    ToasterPopupClick()
    time.sleep(0.3)
    ToasterPopupClick()
    time.sleep(0.3)
    ToasterPopupClick()
    # time.sleep(10)
    logOut()

RepairUserDetails_Input()