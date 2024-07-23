import openpyxl
from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Define the header
ws.append(["Test ID", "Username", "Password", "Date", "Time of Test", "Name of Tester", "Test Result"])

# Add test data
test_data = [
    (1, "Admin", "admin123", "2024-07-23", "10:00", "Tester1", ""),
    (2, "Admin1", "admin123", "2024-07-23", "10:05", "Tester2", ""),
    (3, "Admin2", "admin123", "2024-07-23", "10:10", "Tester3", ""),
    (4, "Admin3", "admin123", "2024-07-23", "10:15", "Tester4", ""),
    (5, "Admin4", "admin123", "2024-07-23", "10:20", "Tester5", "")
]

for data in test_data:
    ws.append(data)

# Save the workbook
wb.save("test_data.xlsx")
