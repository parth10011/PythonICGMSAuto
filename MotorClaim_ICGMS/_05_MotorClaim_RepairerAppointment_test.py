import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_MotorClaim_RepairAppoint():
    # Login
    setUp()
    time.sleep(1)
    User = Cust_Login.cell(2,1).value
    Pass = Cust_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Open Repairer Appointment
    appoint_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Repairer Appointment'])[1]")))
    appoint_button.click()
    time.sleep(1)

    # Select Repairer Type
    repair_type = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@formcontrolname="repairer_id"]'))))
    repair_type.select_by_visible_text("Parth Repair Corporation")
    # select_repairer.select_by_visible_text("Ehtasham")
    time.sleep(1)

    # Enter Remark
    remark = driver.find_element(By.XPATH, "//textarea[@formcontrolname='repairer_remark']")
    remark.send_keys("Approval Done")

    # Click Appoint
    appoint = driver.find_element(By.XPATH, "//button[@type='submit']")
    appoint.click()

    ToasterPopupClick()
    logOut()
    # time.sleep(10)
