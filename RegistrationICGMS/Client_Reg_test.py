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
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Registration ']"))).click()

# Click on Client 
driver.find_element(By.PARTIAL_LINK_TEXT, "Client").click()
time.sleep(0.5)

# Client Basic Details Fill
def Client_BasicDetails_Input():

    # Click on Add New Client
    driver.find_element(By.CSS_SELECTOR, "button[ngbtooltip='Add New']").click()

    # Enter Client Name
    clientName_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='client_name']")))
    clientName_input.send_keys(getrandomname())

    # Select Client Type
    clientType_dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@formcontrolname='client_type']/option[@value != '']")))
    random.choice(clientType_dropdown).click()

    # Enter Contact Number
    contNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='contact_number']")
    contNumb_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Contact Number
    altcontNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='alt_contact_number']")
    altcontNumb_input.send_keys(generate_random_mobile_number())

    # Enter Email ID
    emailID_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email_id']")
    emailID_input.send_keys(getRandomEmail())

    # Upload Logo for Client
    logo_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='logo_file']")
    logo_fileupload.send_keys(getrandomImage())

    # Enter Address for the Client
    addr_input = driver.find_element(By.XPATH, "//textarea[@formcontrolname='reg_office_address']")
    addr_input.send_keys("dhbvd o7t dsul giue83989")

    # Select Country Dropdown
    country_dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@formcontrolname='country_id']/option[@value !='']")))
    random.choice(country_dropdown).click()

    # Select State Dropdown
    state_dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@formcontrolname='state_id']/option[@value !='']")))
    random.choice(state_dropdown).click()
    time.sleep(1)

    # Select City Dropdown
    try:
        city_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='city_id']/option[@value !='']")
        random.choice(city_dropdown).click()
    except Exception :
        a = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//select[@formcontrolname='state_id']/option[@value !='']")))
        random.choice(a).click()
        b = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//select[@formcontrolname='city_id']/option[@value !='']")))
        random.choice(b).click()

    # Select Zone Dropdown
    zone_dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@formcontrolname='zone_id']/option[@value !='']")))
    random.choice(zone_dropdown).click()

    # Enter Pin Code
    pinCode_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pincode']")
    pinCode_input.send_keys(getrandom6digit())

    # Enter Gst Number
    gstNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='gst_no']")
    gstNumb_input.send_keys("22AAAAA0000A1Z5")

    # Enter PAN Number
    panNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='pan_no']")
    panNumb_input.send_keys("ABCDE1234F")

    # Enter Permitted number of users
    permUsers_input = driver.find_element(By.XPATH, "//input[@formcontrolname='permitted_users']")
    permUsers_input.send_keys("5")

    # Upload PAN Copy Document
    panCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='pan_file']")
    panCopyDoc_fileupload.send_keys(panCopy_Link)

    # Upload Gst Copy Document
    gstCopyDoc_fileupload = driver.find_element(By.XPATH, "//input[@formcontrolname='gst_file']")
    gstCopyDoc_fileupload.send_keys(gstCopy_Link)

    # Scroll to the end of page
    Scroll_end = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Click Save Button
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']")))
    save_button.click()
    ToasterPopupClick()

    # Click on Client 
    driver.find_element(By.PARTIAL_LINK_TEXT, "Client").click()


Client_BasicDetails_Input()


def Client_BranchDetails_Input():
    

    # Click on Edit Client Icon
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

     # Click on Client 
    driver.find_element(By.PARTIAL_LINK_TEXT, "Client").click()


Client_BranchDetails_Input()


def Client_ContactDetails_Input():

    # Click on Edit Client Icon
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
    nameClientContact_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))
    nameClientContact_input.send_keys(getrandomname())

    # Select Designation dropdown in Add New Contact
    designationClientContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='designation_id']/option[@value !='' ]")))
    random.choice(designationClientContact_dropdown).click()

    # Select Department dropdown in Add New Contact
    departmentClientContact_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='department_id']/option[@value !='' ]")))
    random.choice(departmentClientContact_dropdown).click()

    # Enter Contact Number in Add New Contact
    contactNumberContact_input = driver.find_element(By.ID, "contact_number")
    contactNumberContact_input.send_keys(generate_random_mobile_number())

    # Enter Alternate Number in Add New Contact
    altNumberContact_input = driver.find_element(By.ID, "alt_contact_number")
    altNumberContact_input.send_keys(generate_random_mobile_number())

    # Enter Email ID in Add New Contact
    emailIDContact_input = driver.find_element(By.ID, "email_id")
    emailIDContact_input.send_keys(getRandomEmail())

    # Enter Branch Name in Add New Contact
    branchnameContact_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_name']")
    branchnameContact_input.send_keys(randomstateCode)

    # Enter Branch Code in Add New Contact
    branchcodeContact_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch_code']")
    branchcodeContact_input.send_keys("BB"+getrandom6digit())

    # Click on Add Button
    addContact_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]/preceding-sibling::button[contains(text(),'Add')]")
    addContact_button.click()
    ToasterPopupClick()
    time.sleep(0.3)
    ToasterPopupClick()
    time.sleep(0.3)

    # Click on Client Registration List
    driver.find_element(By.PARTIAL_LINK_TEXT, "Client").click()


Client_ContactDetails_Input()


def Client_UserDetails_Input():

    # Click on Edit Client Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on User Details
    driver.find_element(By.XPATH, "//button[text()=' User Details ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

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

    # Click on Client Registration List
    driver.find_element(By.PARTIAL_LINK_TEXT, "Client").click()


Client_UserDetails_Input()


def Client_ProdMapping_Input():

    # Click on Edit Client Icon
    edit_icon = wait.until((EC.presence_of_element_located((By.XPATH, "(//i[@name='edit-2'])[1]"))))
    edit_icon.click()
    time.sleep(1)

    # Click on Product Mapping
    driver.find_element(By.XPATH, "//button[text()=' Product Mapping ']").click()
    ToasterPopupClick()

    # Click On Add New Button
    addNew_Button = driver.find_element(By.XPATH, "//button[text()=' Add New ']")
    addNew_Button.click()

    # Select Product Name dropdown in Add Product
    prodName_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='product_id']/option[@value != '']")))
    random.choice(prodName_dropdown).click()

    # Enter SLA/Agreement Date
    slaDate_datepicker = driver.find_element(By.XPATH, "//div[label[text()='SLA/Agreement Date']]/div/input[@formcontrolname='sla_date']")
    slaDate_datepicker.send_keys(current_date)

    # Enter Agreement Valid From Date
    argmntFrom_datepicker = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='agreement_valid_from']")
    argmntFrom_datepicker.send_keys("01012023")

    # Enter Agreement Valid Upto Date
    argmntUpto_datepicker = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='agreement_valid_upto']")
    argmntUpto_datepicker.send_keys("01012028")

    # Click on Add Button
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]//preceding-sibling::button")
    add_button.click()
    ToasterPopupClick()
    time.sleep(1)
    ToasterPopupClick()
    logOut()

Client_ProdMapping_Input()