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

# Click on User
driver.find_element(By.PARTIAL_LINK_TEXT, "Users").click()
time.sleep(0.5)

def PersonalInfo_Input():
    
    # Click on Add New User
    driver.find_element(By.CSS_SELECTOR, "button[ngbtooltip='Add User']").click()

    # Enter First Name
    firstName_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='first_name']")))
    firstName_input.send_keys(getrandomname())

    # Enter Last Name
    lastName_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='last_name']")
    lastName_input.send_keys("TTEESSTT")

    # Enter Email ID
    emailID_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
    emailID_input.send_keys(getRandomEmail())

    # Enter Phone Number
    phoneNumb_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='contact_number']")
    phoneNumb_input.send_keys(generate_random_mobile_number())

    # Select Department dropdown
    dept_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='department']/option[@value !='']")))
    random.choice(dept_dropdown).click()

    # Select Designation dropdown
    desig_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id='designation']/option[@value !='']")))
    random.choice(desig_dropdown).click()

    # Select User Type
    userType_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@id = 'role_type']/option[@value != '']")))
    random.choice(userType_dropdown).click()

    # Click on Save button
    save_button = driver.find_element(By.XPATH, "//button[text() = ' Save ']")
    save_button.click()
    time.sleep(1)
    ToasterPopupClick()
    logOut()

PersonalInfo_Input()