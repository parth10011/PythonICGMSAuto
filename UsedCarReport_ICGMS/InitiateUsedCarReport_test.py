# import sys ; import os
# # Add the parent directory (the root folder) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *

def test_UsedCarReport_Initiate():
    # Login
    setUp()
    time.sleep(1)
    User = Admin_Login.cell(2,1).value
    Pass = Admin_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Initiate Claim
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim']"))).click()
    time.sleep(0.5)

    # Select Product as Used Car
    product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[1]/div/app-claim-intimation/div[1]/div/div/div[2]/div/div/select'))))
    product.select_by_visible_text("Used Car")
    time.sleep(0.5)

    # Enter Case Number For Used Car Report
    caseNumb_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='case_no']")))
    caseNumb_input.send_keys("POLI"+getrandom6digit())

    # Enter Branch/Location
    branchLoc_input = driver.find_element(By.XPATH, "//input[@formcontrolname='branch']")
    branchLoc_input.send_keys(randomstateCode)

    # Select State Dropdown
    state_dropdown = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@formcontrolname='state']/option[@value !='']")))
    random.choice(state_dropdown).click()
    time.sleep(1)

    # Select RTO Dropdown
    try:
        rto_dropdown = driver.find_elements(By.XPATH, "//select[@formcontrolname='rto_Name']/option[@value !='']")
        random.choice(rto_dropdown).click()
    except Exception :
        a = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//select[@formcontrolname='state']/option[@value !='']")))
        random.choice(a).click()
        b = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//select[@formcontrolname='rto_Name']/option[@value !='']")))
        random.choice(b).click()

    # Enter Borrower Name
    borrowName_input = driver.find_element(By.XPATH, "//input[@formcontrolname='borrower_name']")
    borrowName_input.send_keys(getrandomname())

    # Enter Registration Number
    regNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='regnumber']")
    regNumber_input.send_keys(randomCarRegNumber)

    # Enter Asset Description
    assetDescription_input = driver.find_element(By.XPATH, "//input[@formcontrolname='asset_description']")
    assetDescription_input.send_keys("Good Asset Working Fine")

    # Enter Present Owner Name
    presOwnName_input = driver.find_element(By.XPATH, "//input[@formcontrolname='owner_name']")
    presOwnName_input.send_keys(getrandomname())

    # Enter Customer Email ID
    custEmail_input = driver.find_element(By.XPATH, "//input[@formcontrolname='customer_email']")
    custEmail_input.send_keys(getRandomEmail())

    # Enter Customer Mobile Number
    custMobNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='mobile_number']")
    custMobNumber_input.send_keys(generate_random_mobile_number())

    # Enter Make of Vehicle
    Make_input = driver.find_element(By.XPATH, "//input[@formcontrolname='make_Name']")
    Make_input.send_keys("Kia")
    ToasterPopupClick()

    # Enter Model of Vehicle
    Model_input = driver.find_element(By.XPATH, "//input[@formcontrolname='model_Name']")
    Model_input.send_keys("Enchiladas")

    # Enter Dealer Name of Vehicle
    dealName_input = driver.find_element(By.XPATH, "//input[@formcontrolname='dealer_name']")
    dealName_input.send_keys("Green Goblin vs Spiderman")

    # Enter Manufacturer of Vehicle
    manufact_input = driver.find_element(By.XPATH, "//input[@formcontrolname='manufacturer']")
    manufact_input.send_keys("Marvel Productions")

    # Enter Registration Date Of Veicle
    regDateVehicle_input = driver.find_element(By.XPATH, "//input[@formcontrolname='registration_date']")
    regDateVehicle_input.send_keys(current_date)

    # Enter Odometer Reading of Vehicle
    odometer_input = driver.find_element(By.XPATH, "//input[@formcontrolname='odometer_reading']")
    odometer_input.send_keys(getrandom6digit())

    # Enter Color of Vehicle
    color_input = driver.find_element(By.XPATH, "//input[@formcontrolname='color']")
    color_input.send_keys(getColor())

    # Enter Seating Capacity of Vehicle
    seatCapacity_input = driver.find_element(By.XPATH, "//input[@formcontrolname='seat_capacity']")
    seatCapacity_input.send_keys(random.randint(1,10))

    # Enter Cubic Capacity of Vehicle
    cubeCapacity_input = driver.find_element(By.XPATH, "//input[@formcontrolname='cubic_capacity']")
    cubeCapacity_input.send_keys(random.randint(1,1000))

    # Select a Fuel Type
    fuelType_select = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[@formcontrolname='fuel_type']/option[@value!='']")))
    random.choice(fuelType_select).click()

    # Enter Variant of Vehicle
    variant_input = driver.find_element(By.XPATH, "//input[@formcontrolname='variant']")
    variant_input.send_keys("SUV")

    # Enter Class of Vehicle
    class_input = driver.find_element(By.XPATH, "//input[@formcontrolname='body_type']")
    class_input.send_keys("CRoss CAr new Gen")

    # Enter Use of Vehicle
    useOfVehicle_input = driver.find_element(By.XPATH, "//input[@formcontrolname='use_of_vehicle']")
    useOfVehicle_input.send_keys("Personal Use")

    # Enter Engine Number of Vehicle
    engineNumber_input = driver.find_element(By.XPATH, "//input[@formcontrolname='vehicle_engine_number']")
    engineNumber_input.send_keys("JBCJ"+getrandom6digit()+"SHD")

    # Enter Chassis Number of Vehicle
    chassNumb_input = driver.find_element(By.XPATH, "//input[@formcontrolname='vehicle_chasi_number']")
    chassNumb_input.send_keys("2HFJ"+getrandom6digit()+"09VBNSA")

    # Enter Credit Valuation Agency
    credValAgency_input = driver.find_element(By.XPATH, "//input[@formcontrolname='credit_valuation']")
    credValAgency_input.send_keys("HDFC ERGO FINANCIER")

    # Enter Invoice/ICN/RC
    invoiceIcnRc_input = driver.find_element(By.XPATH, "//input[@formcontrolname='invoice_rc']")
    invoiceIcnRc_input.send_keys("D876LWC8IA0AW")

    # Enter Date Of Invoice
    dateInvoice_datepick = driver.find_element(By.XPATH, "//input[@formcontrolname='invoice_date']")
    dateInvoice_datepick.send_keys(current_date)

    # Enter Invoice Amount / Sale Value
    invoiceAmt_input = driver.find_element(By.XPATH, "//input[@formcontrolname='invoice_amount']")
    invoiceAmt_input.send_keys(getrandom6digit())

    # Enter Remarks
    remark_input = driver.find_element(By.XPATH, "//textarea[@formcontrolname='remarks']")
    remark_input.send_keys("Need more Customer Information for processing purpose")

    # Scroll to the end of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Click on Submit Button
    submit_button = driver.find_element(By.XPATH, "//button[text()=' Back ']/preceding-sibling::button[@type='button']")
    submit_button.click()

    # Click on Download Used Car Report pdf
    wait.until(EC.element_to_be_clickable((By.XPATH , "(//i[@ngbtooltip='Download Used Car Report'])[1]"))).click()
    ToasterPopupClick()
    time.sleep(1)
    ToasterPopupClick()
    logOut()

# test_UsedCarReport_Initiate()
