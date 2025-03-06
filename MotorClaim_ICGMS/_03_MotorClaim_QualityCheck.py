import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(a1dmin , P2ass)
ToasterPopupClick()

# Open View List
view_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']")))
view_list.click()

# Quality Check Button click
quality_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Quality Check'])[1]")))
quality_button.click()
time.sleep(1)

# Claim Number Enter
claim_number = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Claim Number' or @placeholder='Claim Number']")))
claim_number.send_keys(current_date)

# Enter Date Of Accident
date_accident = driver.find_element(By.XPATH, "//input[@placeholder='Enter Date and Time of Accident/Loss']")
date_accident.send_keys(current_date)

# Enter Place of Accident
place_accident = driver.find_element(By.XPATH, "//input[@placeholder='Enter Place of Accident/Loss:']")
place_accident.send_keys("Red Light")

# Enter Purpose Of Vehicle
purpose_vehicle = driver.find_element(By.XPATH, "//input[@placeholder='Enter Purpose of use of vehicle at the time of Accident/Loss']")
purpose_vehicle.send_keys("Private")

# Enter Details of existing policies
existing_policies = driver.find_element(By.XPATH, "//input[@placeholder='Enter Details of other existing insurance policies for the vehicle']")
existing_policies.send_keys("No other policies of user")

# Select Financier's Interest radio button 
financier_radio = driver.find_element(By.XPATH , "(//div[text()=' No '])[1]")
financier_radio.click()

# Enter Narration of cause of incident
incident_narration = driver.find_element(By.XPATH , "//textarea[@placeholder='(Do not state police report attached or as per police report )']")
incident_narration.send_keys("dark night accident, very bad")

# Enter nature of weight and goods
goods_details = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Nature and weight of goods carried (for Goods Carrying Vehicle)']")
goods_details.send_keys("Fruit Basket and vegetables")

# Enter number of occupants
num_occupants = driver.find_element(By.XPATH , "//input[@placeholder='Enter Number of occupants in the vehicle at the time of accident']")
num_occupants.send_keys("10 people were in car at the time")

# Select Incident reported to police radio button
police_report_radio = driver.find_element(By.XPATH, "(//div[text()=' No '])[2]")
police_report_radio.click()

# Enter date
police_report_date = driver.find_element(By.XPATH, "(//input[@placeholder='Enter If yes, FIR/GD Entry No.'])[2]")
police_report_date.send_keys(current_date)

# Enter name of police station
police_station = driver.find_element(By.XPATH, "//input[@placeholder='Enter Police Station']")
police_station.send_keys("Thana Raj Nagar")

# Enter name of Driver
driver_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter Name of driver at time of accident']")
driver_name.send_keys("Python Developer")

# Enter date of birth of driver
driver_dob = driver.find_element(By.XPATH, "//input[@placeholder='Enter Date of birth of driver']")
driver_dob.send_keys("22011990")

# Enter driving license number of driver
driver_license = driver.find_element(By.XPATH, "//input[@placeholder='Enter Driving License No.']")
driver_license.send_keys("DL09OL0912")

# Select relationship of driver to insured radio button
driver_relation = driver.find_element(By.XPATH, "//input[following-sibling::text()[contains(., 'Paid Driver')]]")
driver_relation.click()

# Enter Other field
other_details = driver.find_element(By.XPATH, "//input[@placeholder='(Please Specify)']")
other_details.send_keys("No specific data required for this space")

# Select accident resulted in any death radio button
accident_death_radio = driver.find_element(By.XPATH, "(//div[text()=' No '])[3]")
accident_death_radio.click()

# Enter Name of person with Injury or Death inside vehicle
injured_name_inside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Name'])[1]")
injured_name_inside.send_keys(randomCustomerName)

# Enter Age of person with Injury or Death inside vehicle
injured_age_inside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Age'])[1]")
injured_age_inside.send_keys("23")

# Enter Gender of person with Injury or Death inside vehicle
injured_gender_inside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Gender'])[1]")
injured_gender_inside.send_keys("Male")

# Select Death or Injury radio button of person inside vehicle
injury_radio_inside = driver.find_element(By.XPATH, "(//div[contains(text(), 'Injury')]//input)[1]")
injury_radio_inside.click()

# Enter Nature of Injury of person inside vehicle
injury_nature_inside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Nature of injury'])[1]")
injury_nature_inside.send_keys("head hurt")

# Enter Name of person with Injury or Death outside vehicle
injured_name_outside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Name'])[2]")
injured_name_outside.send_keys(randomRepairerName)

# Enter Age of person with Injury or Death outside vehicle
injured_age_outside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Age'])[2]")
injured_age_outside.send_keys("51")

# Enter Gender of person with Injury or Death outside vehicle
injured_gender_outside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Gender'])[2]")
injured_gender_outside.send_keys("Male")

# Select Death or Injury radio button of person outside vehicle
injury_radio_outside = driver.find_element(By.XPATH, "(//div[contains(text(), 'Injury')]//input)[2]")
injury_radio_outside.click()

# Enter Nature of Injury of person outside vehicle
injury_nature_outside = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Nature of injury'])[2]")
injury_nature_outside.send_keys("leg hurt")

# Select Notice of third party claim radio button
third_party_claim_radio = driver.find_element(By.XPATH, "(//div[contains(text(), 'No')]//input)[4]")
third_party_claim_radio.click()

# Enter Details of witness to the accident
witness_details = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Please specify any details of witnesses to the accident']")
witness_details.send_keys("No witness at the scene")

# Enter Details of third party damage
third_party_damage = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='(including details of other vehicle, if any involved)']")
third_party_damage.send_keys("No damage to third party")

# Enter Remark
remark = driver.find_element(By.XPATH, "//textarea[@formcontrolname='qc_remark']")
remark.send_keys("Approval Done")

# Click Submit
submit = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
submit.click()

ToasterPopupClick()
logOut()
# time.sleep(10)