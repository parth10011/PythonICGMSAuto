from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to chromedriver.exe
chrome_driver_path = r"C:\chromedriver.exe"  

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional: Opens Chrome in maximized mode

# Create Service object
service = Service(chrome_driver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Google
driver.get("https://release.icgms.sharajman.com/")
# time.sleep(1)


admin = "superadmnphase1@owleyes.ch" ; Pass = "Admin123"
Login_funct(admin , Pass)


