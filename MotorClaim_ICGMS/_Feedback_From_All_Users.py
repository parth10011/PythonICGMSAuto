import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

def MotorClaim_FeedBackFromCustomer():
    # Login
    setUp()
    time.sleep(1)
    User = Cust_Login.cell(2,1).value
    Pass = Cust_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Click on Give Feedback button
    custFeedback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Give Feedback'])[1]")))
    custFeedback_button.click()
    time.sleep(1)

    # Give Overall rating to process
    overallRating_stars = wait.until((EC.presence_of_all_elements_located((By.XPATH, "//label[text()='How would you rate the overall experience?']/following-sibling::div//span[text() ='★']"))))
    random.choice(overallRating_stars).click()

    # Give recommendation rating to others for process
    recommendOthers_stars = driver.find_elements(By.XPATH, "//label[text()='Would you recommend this service to others?']/following-sibling::div//span[text() ='★']")
    random.choice(recommendOthers_stars).click()

    # Give easiness rating to process
    easinessRating_stars = driver.find_elements(By.XPATH, "//label[text()='Was the process easy to understand?']/following-sibling::div//span[text() ='★']")
    random.choice(easinessRating_stars).click()

    # Click Submit Button
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    time.sleep(1)
    logOut()


MotorClaim_FeedBackFromCustomer()

def MotorClaim_FeedbackFromInsurer():

    # Login
    setUp()
    time.sleep(1)
    User = Insurer_Login.cell(2,1).value
    Pass = Insurer_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)

    ToasterPopupClick()
    time.sleep(0.5)

    # Click on Give Feedback button
    insurerFeedback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Give Feedback'])[1]")))
    insurerFeedback_button.click()
    time.sleep(1)

    # Give Overall rating to process
    overallRating_stars = wait.until((EC.presence_of_all_elements_located((By.XPATH, "//label[text()='How would you rate the overall experience?']/following-sibling::div//span[text() ='★']"))))
    random.choice(overallRating_stars).click()

    # Give recommendation rating to others for process
    recommendOthers_stars = driver.find_elements(By.XPATH, "//label[text()='Would you recommend this service to others?']/following-sibling::div//span[text() ='★']")
    random.choice(recommendOthers_stars).click()

    # Give easiness rating to process
    easinessRating_stars = driver.find_elements(By.XPATH, "//label[text()='Was the process easy to understand?']/following-sibling::div//span[text() ='★']")
    random.choice(easinessRating_stars).click()

    # Click Submit Button
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    time.sleep(1)
    logOut()

MotorClaim_FeedbackFromInsurer()

def MotorClaim_FeedbackFromRepairer():
    setUp()
    time.sleep(1)
    User = Repair_Login.cell(2,1).value
    Pass = Repair_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)

    ToasterPopupClick()
    time.sleep(0.5)

    # Open Repairer Claim View List
    repClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/repairer-claim-list']"))))
    repClaimList_link.click()

    # Click on Give Feedback button
    repairerFeedback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Give Feedback'])[1]")))
    repairerFeedback_button.click()
    time.sleep(1)

    # Give Overall rating to process
    overallRating_stars = wait.until((EC.presence_of_all_elements_located((By.XPATH, "//label[text()='How would you rate the overall experience?']/following-sibling::div//span[text() ='★']"))))
    random.choice(overallRating_stars).click()

    # Give recommendation rating to others for process
    recommendOthers_stars = driver.find_elements(By.XPATH, "//label[text()='Would you recommend this service to others?']/following-sibling::div//span[text() ='★']")
    random.choice(recommendOthers_stars).click()

    # Give easiness rating to process
    easinessRating_stars = driver.find_elements(By.XPATH, "//label[text()='Was the process easy to understand?']/following-sibling::div//span[text() ='★']")
    random.choice(easinessRating_stars).click()

    # Click Submit Button
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    time.sleep(1)
    logOut()

MotorClaim_FeedbackFromRepairer()

def MotorClaim_FeedbackFromSurveyor():
    setUp()
    time.sleep(1)
    User = Surveyor_Login.cell(2,1).value
    Pass = Surveyor_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)

    ToasterPopupClick()
    time.sleep(0.5)

    # Open Surveyor Claim View List
    survClaimList_link = wait.until((EC.presence_of_element_located((By.XPATH, "//a[@href='/surveyor-claim-list']"))))
    survClaimList_link.click()

    # Click on Give Feedback button
    surveyorFeedback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Give Feedback'])[1]")))
    surveyorFeedback_button.click()
    time.sleep(1)

    # Give Overall rating to process
    overallRating_stars = wait.until((EC.presence_of_all_elements_located((By.XPATH, "//label[text()='How would you rate the overall experience?']/following-sibling::div//span[text() ='★']"))))
    random.choice(overallRating_stars).click()

    # Give recommendation rating to others for process
    recommendOthers_stars = driver.find_elements(By.XPATH, "//label[text()='Would you recommend this service to others?']/following-sibling::div//span[text() ='★']")
    random.choice(recommendOthers_stars).click()

    # Give easiness rating to process
    easinessRating_stars = driver.find_elements(By.XPATH, "//label[text()='Was the process easy to understand?']/following-sibling::div//span[text() ='★']")
    random.choice(easinessRating_stars).click()

    # Click Submit Button
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    # submit_button = driver.find_element(By.XPATH, "//button[text()='Close']")
    submit_button.click()
    time.sleep(1)
    logOut()

MotorClaim_FeedbackFromSurveyor()

def MotorClaim_FinalCompletionFeedback():
    setUp()
    time.sleep(1)
    User = Admin_Login.cell(2,1).value
    Pass = Admin_Login.cell(2,2).value
    Login_ICGMS.login(User , Pass)
    ToasterPopupClick()

    # Open View List
    view_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/claim-details']")))
    view_list.click()

    # Final Completion Button Click
    finalComplete_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Final Completion'])[1]"))))
    finalComplete_button.click()

    # Complete Claim Button Click
    completeClaim_button = wait.until((EC.presence_of_element_located((By.XPATH, "(//button[text()='Complete Claim'])[1]"))))
    completeClaim_button.click()
    time.sleep(3)

    logOut()

MotorClaim_FinalCompletionFeedback()