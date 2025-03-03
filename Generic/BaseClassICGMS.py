import random
import string
import datetime
import unittest
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
wait = WebDriverWait(driver, 20)

# class Basetest(unittest.TestCase):
def setUp():

        """Set up the browser before each test."""
        driver.maximize_window()
        driver.get(url)

    # def tearDown(self):
    #     """Quit the browser after each test."""
    #     self.driver.quit()

def ToasterPopupClick():
       
       toaster = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='alert']")))
       toaster.click()

def logOut():
       
       Profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-toggle='dropdown']")))
       Profile.click()
       logout = driver.find_element(By.XPATH , "//a[@style='cursor: pointer;']")
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

def getrandomname():
	
    names = ["Mathias", "Tobias", "Cristopher", "Ronald", "Donovan", "Fabian", "Luciano", "Masao",
    "Moses", "Angel", "Zaid", "Conner", "Jared", "Jasper", "Larry", "Eugene","Devyn", "Kamden",
    "Armani", "Derick", "Ellis", "Ali", "Camron", "Darrell", "Cortez", "Peter", "Jerome", "Pierre",
    "Sage", "Sheldon", "Hassan", "Kristopher", "Darryl", "Trey", "Russell","Korbin", "Abram", "Anton",
    "Cason", "Frederick", "Collin", "Aditya", "Aurther", "Kazama", "Ravi","Bikash","Rajat", "Diwakar", "Asim", "Roop"]

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

      return stateCode+districtcode+r1+r2+uniqueNumber
randomCarRegNumber = getrandomregnumber()


Date = datetime.datetime.now()
current_year = Date.year
current_date = Date.strftime("%d%m%Y")
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