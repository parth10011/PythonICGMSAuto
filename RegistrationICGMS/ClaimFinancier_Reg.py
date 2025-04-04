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

# Click on Claim Financier
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financer").click()
except:
    driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financier").click()
time.sleep(0.5)

def ClaimFinanc_BasicDetails_Input():

    # Click on Add New Button
    addNew_button = driver.find_element(By.XPATH, "//button[text()='Add New']")
    addNew_button.click()

    # Enter Financier Name
    financName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='claim_financier_name']")))
    financName.send_keys(getrandomname())

    # Enter Gst Number
    gstNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='gst_no']")
    gstNumb_input.send_keys("22AAAAA0000A1Z5")

    # Enter PAN Number
    panNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pan_no']")
    panNumb_input.send_keys("ABCDE1234F")

    # Enter Permitted Number Of Users
    permUsers_input = driver.find_element(By.XPATH, "//input[@formcontrolname='permitted_users']")
    permUsers_input.send_keys(random.randint(1,10))

    # Upload PAN Copy Document
    panCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='pan_file']")
    panCopyDoc_fileupload.send_keys(panCopy_Link)

    # Upload Gst Copy Document
    gstCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='gst_file']")
    gstCopyDoc_fileupload.send_keys(gstCopy_Link)

    # Upload Logo
    logo_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='logo_file']")
    logo_fileupload.send_keys(getrandomImage())

# Enter Address Details

    # Enter Registered Office Address
    regOffAddr_input = driver.find_element(By.XPATH, "//textarea[@formcontrolname='reg_office_address']")
    regOffAddr_input.send_keys("jds 8735 dshffbds 73rbfu4")
    time.sleep(1)

    # Select Country Name dropdown
    country_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='country_id']"))))
    country_dropdown.select_by_visible_text("India")

    # Select State Name dropdown
    state_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='state_id']/option[@value!= '']")))
    random.choice(state_dropdown).click()

    # Select City Name dropdown
    city_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='city_id']/option[@value!= '']")))
    random.choice(city_dropdown).click()

    # Select zone dropdown
    zone_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='zone_id']/option[@value!= '']")))
    random.choice(zone_dropdown).click()

    # Enter Pincode
    pincode_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pincode']")
    pincode_input.send_keys(getrandom6digit())

# Enter Contact Details

    # Enter Name Of Contact
    nameContact_input = driver.find_element(By.XPATH, "//input[@formcontrolname='contact_name']")
    nameContact_input.send_keys(getrandomname())

    # Enter Contact Number
    contactNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='contact_number']")
    contactNumb_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Contact Number
    altNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='alt_contact_number']")
    altNumb_input.send_keys(generate_random_mobile_number())

    # Enter Email Id
    emailID_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email_id']")
    emailID_input.send_keys(getRandomEmail())
    
    # Scroll to the end of page
    prodName_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Product Name ']/following::div[@aria-haspopup='listbox']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", prodName_dropdown)
    time.sleep(1)
    prodName_dropdown.click()

    # Select a random Product Name
    options_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ng-dropdown-panel//div[@role='option']")))
    random.choice(options_list).click()
    time.sleep(1)

    # Click on Save Button
    save_button = driver.find_element(By.XPATH, "//button[text()=' Save ']")
    save_button.click()
    ToasterPopupClick()

    # Click on Claim Financier
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financer").click()
    except:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financier").click()
    time.sleep(0.5)

ClaimFinanc_BasicDetails_Input()

def ClaimFinanc_BranchDetails_Input():
    

    # Click on Edit Claim Financier Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on Branch Details
    driver.find_element(By.XPATH, "//button[text()=' Branch Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Enter Branch Name
    branchName_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='branch_name']")))
    branchName_input.send_keys(getrandomname()+" Branch Name")

    # Enter Branch Code
    branchCode_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='branch_code']")))
    branchCode_input.send_keys(randomstateCode+random6Number)

    # Enter Address
    branchAddr_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='address']")))
    branchAddr_input.send_keys("kjdsf 43r 34jb")

    # Select Country Name
    country_dropdown = Select(driver.find_element(By.ID, "country_id"))
    country_dropdown.select_by_visible_text("India")
    time.sleep(0.5)

    # Select State Name
    state_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='state_id']//option[@value>='1']")))
    random.choice(state_dropdown).click()
    time.sleep(0.5)

    # Select City Name
    city_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='city_id']//option[@value>='1']")))
    random.choice(city_dropdown).click()
    time.sleep(0.5)

    # Select Zone Name
    zone_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='zone_id']//option[@value>='1']")
    random.choice(zone_dropdown).click()

    # Enter Pin Code
    pinCode_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pincode']")
    pinCode_input.send_keys(getrandom6digit())
    time.sleep(1)

    # Click on Save Button
    save_input = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]/preceding-sibling::button[contains(text(),'Add')]")
    save_input.click()
    ToasterPopupClick()
    time.sleep(0.5)
    ToasterPopupClick()

    # Click on Claim Financier
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financer").click()
    except:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financier").click()
    time.sleep(0.5)


ClaimFinanc_BranchDetails_Input()

def ClaimFinanc_ContactDetails_Input():

    # Click on Edit Claim Financier Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on Contact Details
    driver.find_element(By.XPATH, "//button[text()=' Contact Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Enter Name in Contact Details
    contName_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))
    contName_input.send_keys(getrandomname())

    # Select Designation in Contact Details
    desContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='designation_id']/option[@value !='']")))
    random.choice(desContact_dropdown).click()

    # Select Department in Contact Details
    deptContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='department_id']/option[@value !='']")))
    random.choice(deptContact_dropdown).click()

    # Enter Contact Number
    contNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='contact_number']")
    contNumber_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Number
    altNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='alt_contact_number']")
    altNumber_input.send_keys(generate_random_mobile_number())

    # Enter Email ID
    emailID_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email_id']")
    emailID_input.send_keys(getRandomEmail())

    # Enter Branch Name
    branchName_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_name']")
    branchName_input.send_keys("Named Branch")

    # Enter Branch Code
    branchCode_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_code']")
    branchCode_input.send_keys(randomstateCode+getrandom6digit())
    time.sleep(1)

    # Click on Add button
    addContact_button = driver.find_element(By.XPATH, "//button[text()=' Close ']/preceding-sibling::button[text()=' Add ']")
    addContact_button.click()
    ToasterPopupClick()
    time.sleep(0.5)
    ToasterPopupClick()

    # Click on Claim Financier
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financer").click()
    except:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financier").click()
    time.sleep(0.5)


ClaimFinanc_ContactDetails_Input()

def ClaimFinanc_UserDetails_Input():

    # Click on Edit Claim Financier Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on User Details
    driver.find_element(By.XPATH, "//button[text()=' User Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Enter First Name in User Details
    firstNameUser_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='first_name']")))
    firstNameUser_input.send_keys(getrandomname())

    # Enter Last Name in User Details
    lastNameUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']")
    lastNameUser_input.send_keys("NULL")

    # Select Department in User Details
    deptUser_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='department_id']/option[@value !='']")))
    random.choice(deptUser_dropdown).click()

    # Select Designation in User Details
    desUser_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='designation_id']/option[@value !='']")))
    random.choice(desUser_dropdown).click()

    # Enter Email ID in Use Details
    emailIDUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    emailIDUser_input.send_keys(getRandomEmail())

    # Enter Contact Number in User Details
    contNumberUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='contact_number']")
    contNumberUser_input.send_keys(generate_random_mobile_number())

    # Select User Type in User Details
    userTypeUser_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='role_type']/option[@value !='']")))
    random.choice(userTypeUser_dropdown).click()

    # Enter Branch Name in User Details
    branchNameUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_name']")
    branchNameUser_input.send_keys("Named Branch")

    # Enter Branch Code in User Details
    branchCodeUser_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_code']")
    branchCodeUser_input.send_keys(randomstateCode+getrandom6digit())

    # Click on Add button in User Details
    addUser_button = driver.find_element(By.XPATH, "//button[text()=' Close ']/preceding-sibling::button[text()=' Add ']")
    addUser_button.click()
    ToasterPopupClick()
    time.sleep(0.5)
    ToasterPopupClick()

    # Click on Claim Financier
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financer").click()
    except:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Financier").click()
    logOut()

ClaimFinanc_UserDetails_Input()