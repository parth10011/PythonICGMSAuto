import sys ; import os
# Add the parent directory (the root folder) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import string
import datetime
import unittest
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from Generic.InitiateNewProcess_details import *
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\chromedriver.exe"  # Path to ChromeDriver
options = Options()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30)

# class Basetest(unittest.TestCase):
def setUp():

        """Set up the browser before each test."""
        driver.maximize_window()
        driver.get(url)
        try:
             driver.find_element(By.ID, "details-button").click()
             driver.find_element(By.ID, "proceed-link").click()
        except TimeoutException:
             pass
        except Exception:
             pass

    # def tearDown(self):
    #     """Quit the browser after each test."""
    #     self.driver.quit()

def ToasterPopupClick():
    wait = WebDriverWait(driver, 20)
    try:
        toaster = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='alert']")))
        print(toaster.text)
        toaster.click()
    except TimeoutException:
        print("Error: Toaster popup did not appear or was not clickable within the timeout period.")

def NEWToasterPopupClick():
    try:
        toaster = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='alert']")))

        message = toaster.text

        print("Message Of TOASTER : "+message)

        toaster.click()
        
    except TimeoutException:
        print("Error: Toaster popup did not appear or was not clickable within the timeout period.")

def logOut():
       
       Profile = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-toggle='dropdown']")))
       Profile.click()
       logout = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@style='cursor: pointer;']")))
       logout.click()

       ToasterPopupClick()

       driver.get(emailer_url)
       time.sleep(2.5)


def generate_random_mobile_number():
    n = ["9", "8", "7", "6"]
    n1 = random.choice(n)  # Indian mobile number starting with 9, 8, 7, 6
    mobile_number = [n1] + [str(random.randint(0, 9)) for _ in range(9)]
    return "".join(mobile_number)
randomMobileNumber = generate_random_mobile_number()
randomRepairerNumber = generate_random_mobile_number()
randomAltNumber = generate_random_mobile_number()

def getrandomname():
	
    names = ["Mathias", "Tobias", "Cristopher", "Ronald", "Donovan", "Fabian", "Luciano", "Masao",
    "Moses", "Angel", "Zaid", "Conner", "Jared", "Jasper", "Larry", "Eugene","Devyn", "Kamden",
    "Armani", "Derick", "Ellis", "Ali", "Camron", "Darrell", "Cortez", "Peter", "Jerome", "Pierre",
    "Sage", "Sheldon", "Hassan", "Kristopher", "Darryl", "Trey", "Russell","Korbin", "Abram", "Anton",
    "Cason", "Frederick", "Collin", "Aditya", "Aurther", "Kazama", "Ravi","Bikash","Rajat", "Diwakar", "Asim", "Roop",
    "Ashish", "Mahesh"]

    return random.choice(names)
randomCustomerName = getrandomname()
randomRepairerName = getrandomname()

def getrandomregnumber():
      stateCodes = ["AP", "MH", "KA", "DL", "TN", "GJ", "UP", "RJ", "WB", "KL","JK",
                    "OD","CH","CG","NL","PY","PB","HP","MP","AS","BR","HR","TS","TR",
                    "UK","DD","GA","SK"]
      stateCode = random.choice(stateCodes)
      districtcode = str(random.randint(1,99)).zfill(2)
      r1 = random.choice(string.ascii_uppercase)
      r2 = random.choice(string.ascii_uppercase)
      uniqueNumber = str(random.randint(1000,9999))

      return stateCode+districtcode+r1+r2+uniqueNumber , stateCode
randomCarRegNumber, randomstateCode = getrandomregnumber()
random6Number = str(random.randint(100000, 999999))


Date = datetime.datetime.now()
current_year = Date.year
current_date = Date.strftime("%d%m%Y")
current_time = Date.strftime("%I%M%p")
def getRegYear():
      year = str(random.randint(2000 , current_year))
      return year
randomRegYear = getRegYear()

def getColor():
      Colornames =  [
		            "Red", "Green", "Blue", "Yellow", "Cyan", "Magenta", "Black", "White",
		            "Gray", "Orange", "Pink", "Purple", "Brown", "Lime", "Teal", "Indigo",
		            "Violet", "Olive", "Maroon", "Beige", "Coral", "Turquoise", "Lavender",
		            "Gold", "Silver", "Bronze", "Charcoal", "Ivory", "Salmon", "Peach", 
		            "Crimson", "Azure", "Amber", "Mint", "Plum", "Chocolate", "Navy", "Sienna",
		            "Forest Green", "Slate", "Sky Blue", "Sand", "Rust", "Periwinkle", "Mustard", 
		            "Burgundy", "Fuchsia", "Tan", "Emerald", "Ruby", "Topaz", "Pine", "Jet",
		            "Apricot", "Sapphire", "Olive Drab", "Wheat", "Mauve", "Lilac", "Magenta", 
		            "Papaya", "Pea Green", "Copper", "Khaki", "Royal Blue", "Electric Blue",
		            "Sea Green", "Mint Cream", "Snow", "Lemon", "Pistachio", "Almond", "Grape",
		            "Watermelon", "Mint Green", "Lilac", "Lavender Blush", "Blush", "Seashell", 
		            "Raspberry", "Caramel", "Celeste", "Cantaloupe", "Frost", "Pineapple"
                ]
      Colorname = random.choice(Colornames)
      return Colorname
randomColorName = getColor()

def getFuelType():
     fuel = ["PETROL", "DIESEL", "CNG", "ELECTRIC"]
     return random.choice(fuel)
randomFuelType = getFuelType()

def getStateName():
     States = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
               "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh",
               "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
               "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
               "Andaman and Nicobar","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
               "NCT of Delhi","Puducherry"]
     return random.choice(States)
randomStateName = getStateName()

def getRandomEmail():
    username_length = random.randint(3, 10)
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
    
    domain_length = random.randint(3, 10)
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))
    
    tld = random.choice(["com", "net", "org", "io", "xyz"])
    
    email = f"{username}@{domain}.{tld}"
    return email
randomBasicEmail = getRandomEmail()
randomContactEmail = getRandomEmail()
randomUserEmail = getRandomEmail()