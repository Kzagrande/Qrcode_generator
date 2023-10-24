import pandas as pd
import qrcode
import sys
import os
import json

project_root = "C:\\Users\\User\\sites\\Qrcode_generator"

sys.path.insert(0, project_root)

spreadsheet = pd.read_excel(r"C:\Users\User\Downloads\hc.xlsx")


# Function to create a QR code and save it to a file
def create_qrcode(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


# Directory to save the QR codes
qr_dir = "src/qrcodes"
os.makedirs(qr_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Iterate over the spreadsheet rows and create QR codes
for index, row in spreadsheet.iterrows():
    # employee_id = int(row["ID EMPLOYER"])  # Convert to integer to remove decimal part
    # employee_id = f"{employee_id}_"
    row_without_employee_id = {
        "employee_id": row["ID EMPLOYER"],
        "name_": row["NAME"],
        "admission_date": row["ADMISSION DT"],
        "company": row["COMPANY"],
        "warehouse": row["WH"],
        "business_zone": row["BZ"],
        "collar": row["COLLAR"],
        "category": row["CATEGORY"],
        "sector": row["SECTOR"],
        "role": row["ROLE"],
        "shift": row["SHIFT"],
        "schedule": row["SCHEDULE"],
        "manager_1": row["MANAGER 1"],
        "status": row["STATUS"],
        "role_2": row["ROLE 2"],
        "user": row["USER"],
    }
    id_employer = int(row_without_employee_id["employee_id"])
    new_id = f"ID{id_employer}"
    row_without_employee_id["employee_id"] = new_id

    employee_name = row["NAME"]
    # Generate a QR code based on the employee ID
    row_json = json.dumps(row_without_employee_id)
    print(row_without_employee_id)
    print("ROW_JSON", row_json)
    filename = os.path.join(qr_dir, f"{employee_name}.png")
    create_qrcode(row_json, filename)

# Now, you can read the generated QR codes using an appropriate library.
