import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

def MotorClaim_FeedBackFromCustomer():
    # Login
    setUp()
    time.sleep(1)
    Login_ICGMS.login(Cust_Email1 , P2ass)
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
    Login_ICGMS.login(Insurer_Email1 , P2ass)

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
    Login_ICGMS.login(Repairer_Email1 , P2ass)

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
    Login_ICGMS.login(Surveyor_Email1 , P2ass)

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
    Login_ICGMS.login(a1dmin , P2ass)
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
    logOut()

MotorClaim_FinalCompletionFeedback()