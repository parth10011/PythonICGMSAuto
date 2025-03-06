import time
from Generic.BaseClassICGMS import *
from Generic.Login_ICGMS import *
from selenium.webdriver.common.by import By

# Login
setUp()
time.sleep(1)
Login_ICGMS.login(Cust_Email1 , P2ass)
ToasterPopupClick()

# Open Customer Review
review_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Customer Review'])[1]")))
review_button.click()

# Click Approve
approve_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Approve']")))
approve_button.click()

# Signature
canvas = driver.find_element(By.XPATH, "//canvas[@width='700' and @height='200']")
canvas.click()
time.sleep(1)

submit_sign = driver.find_element(By.XPATH, "//button[text()='Submit the signature']")
submit_sign.click()
time.sleep(1)

close_sign = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
close_sign.click()
time.sleep(1)

logOut()