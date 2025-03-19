# import sys ; import os
# Add the parent directory (the root folder) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import keyboard

# Login
setUp()
time.sleep(1)
User = Cust_Login.cell(2,1).value
Pass = Cust_Login.cell(2,2).value
Login_ICGMS.login(User , Pass)
ToasterPopupClick()

# Open View Details
view_details = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='View Details'])[1]")))
view_details.click()
time.sleep(1)

# Set Browser to Mobile View
driver.set_window_size(765,1000)

# Upload Front View Selfie Image
Front_View_Selfie = driver.find_element(By.XPATH, "//label[@for='front_view_selfie']")
Front_View_Selfie.click()
time.sleep(1)
keyboard.press_and_release("esc")
time.sleep(1)
driver.maximize_window()

Front_View_Input = driver.find_element(By.XPATH, "//input[@id='front_view_selfie']")
Front_View_Input.send_keys(Img_Link)

# Upload Chassis Number Image
Chassis_Number_Input = driver.find_element(By.XPATH, "//input[@id='chassis_number']")
Chassis_Number_Input.send_keys(Img_Link)

# Upload Odometer Number Image
Odometer_Number_Input = driver.find_element(By.XPATH, "//input[@id='odometer_reading']")
Odometer_Number_Input.send_keys(Img_Link)

# Upload Front Rh View Image
Front_Rh_View_Input = driver.find_element(By.XPATH, "//input[@id='front_rh_view']")
Front_Rh_View_Input.send_keys(Img_Link)

# Upload Front Lh View Image
Front_Lh_View_Input = driver.find_element(By.XPATH, "//input[@id='front_lh_view']")
Front_Lh_View_Input.send_keys(Img_Link)

# Upload Rear View Image
Rear_View_Input = driver.find_element(By.XPATH, "//input[@id='rear_view']")
Rear_View_Input.send_keys(Img_Link)

# Upload Rear Lh View Image
Rear_Lh_View_Input = driver.find_element(By.XPATH, "//input[@id='rear_lh_view']")
Rear_Lh_View_Input.send_keys(Img_Link)

# Upload Rear Rh View Image
Rear_Rh_View_Input = driver.find_element(By.XPATH, "//input[@id='rear_rh_view']")
Rear_Rh_View_Input.send_keys(Img_Link)

# Upload RC Copy Image
RC_Copy_Input = driver.find_element(By.XPATH, "//input[@id='rc_copy']")
RC_Copy_Input.send_keys(Img_Link)

# Upload Front Windscreen Inside Image
Front_Windscreen_Inside_Input = driver.find_element(By.XPATH, "//input[@id='front_windscreen_inside']")
Front_Windscreen_Inside_Input.send_keys(Img_Link)

# Upload Engine Compartment Image
Engine_Compartment_Input = driver.find_element(By.XPATH, "//input[@id='engine_compartment_photo']")
Engine_Compartment_Input.send_keys(Img_Link)

# Upload Front Windscreen Outside Image
Front_Windscreen_Outside_Input = driver.find_element(By.XPATH, "//input[@id='front_windscreen_outside']")
Front_Windscreen_Outside_Input.send_keys(Img_Link)

# Upload Dashboard Image
Dashboard_Input = driver.find_element(By.XPATH, "//input[@id='dashboard']")
Dashboard_Input.send_keys(Img_Link)

# Upload Under Chassis Image
Under_Chassis_Input = driver.find_element(By.XPATH, "//input[@id='under_chassis']")
Under_Chassis_Input.send_keys(Img_Link)

# Upload Walkaround Video
Video_Input = driver.find_element(By.XPATH, "//input[@id='walkaround_video']")
Video_Input.send_keys(Vid_Link)
time.sleep(1)

# PAN CARD Upload
PAN_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[1]")
PAN_input.send_keys(Doc2_Link)

# Aadhar Card Upload
Aadhar_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[2]")
Aadhar_input.send_keys(Doc2_Link)

# Passport Upload
Passport_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[3]")
Passport_input.send_keys(Doc2_Link)

# Voter ID Upload
Voter_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[4]")
Voter_input.send_keys(Doc2_Link)

# DL Upload
DL_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[5]")
DL_input.send_keys(Doc2_Link)

# RC Upload
RC_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[6]")
RC_input.send_keys(Doc2_Link)

# Insurance Upload
Insurance_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[7]")
Insurance_input.send_keys(Doc2_Link)

# GovID Upload
GovID_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[8]")
GovID_input.send_keys(Doc2_Link)

# Other 1 Upload
Other1_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[9]")
Other1_input.send_keys(Doc2_Link)

# Other 2 Upload
Other2_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[10]")
Other2_input.send_keys(Doc2_Link)

# Other 3 Upload
Other3_input = driver.find_element(By.XPATH, "(//input[@accept='application/pdf'])[11]")
Other3_input.send_keys(Doc2_Link)
time.sleep(5)

# Signature
Sigarea = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Sign here.........' or @placeholder='  ']")))
Sigarea.click()
time.sleep(1)

canvas = driver.find_element(By.XPATH, "//canvas[@width='700' and @height='200']")
canvas.click()
time.sleep(1)

submit_sign = driver.find_element(By.XPATH, "//button[text()='Submit the signature']")
submit_sign.click()
time.sleep(1)

close_sign = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_sign.click()
time.sleep(1)

# Submit Customer Form
submit = driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
submit.click()
time.sleep(5)
ToasterPopupClick()
logOut()