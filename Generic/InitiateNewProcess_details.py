import random , os
import openpyxl

PathExcelSheet = openpyxl.load_workbook(r"Test Data\ICGMS Test Data.xlsx")
Admin_Login = PathExcelSheet['SuperAdmin']
Cust_Login = PathExcelSheet['Customer']
Repair_Login = PathExcelSheet['Repairer']
Surveyor_Login = PathExcelSheet['Surveyor']
Insurer_Login = PathExcelSheet['Insurer_Log']
MotorClaim_Insurer_Name = PathExcelSheet['MotorClaim_Insurer']
PreInspection_Type_Name = PathExcelSheet['PreInspection_Type']
url = "https://release.icgms.sharajman.com/"
url_Dev = "https://dev.icgms.sharajman.com/"
url_UAT = "https://uat.icgms.insapp.in/"
url_Local = "https://192.168.32.28:4200/"
url_Local2 = "https://192.168.33.132:4200"
emailer_url = "https://release-api.icgms.sharajman.com/emailer"
Doc_Link = "C:/Users/parth/OneDrive/Desktop/DTU/Dummy.pdf"
Doc2_Link = "C:/Users/Parth Grover/Desktop/DTU/Dummy.pdf"
Img_Link = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work/Reports - Menu - click.png"
Vid_Link = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work/Sample Video.mp4"
panCopy_Link = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work/pan copy.png"
gstCopy_Link = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work/gst copy.png"
Est_Report = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work/New folder (2)/TestNG Report.pdf"
Gst_Doc = "C:/Users/Parth Grover/Desktop/DTU/bug-life-cycle.png"
Pan_Doc = "C:/Users/Parth Grover/Desktop/DTU/ETH Trade.png"

InsuredName = "CJNICPOSCN"
latitude = str(random.randint(-90, 90))
longitude = str(random.randint(-180, 180))
folder = "C:/Users/Parth Grover/Desktop/DTU/Sharajman Work"
files = [f for f in os.listdir(folder) if f.endswith(('.png'))]