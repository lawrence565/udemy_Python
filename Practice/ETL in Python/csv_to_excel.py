import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "MyFile"

data = [feilds for feilds in csv.reader(open("Practice/ETL in Python/file.csv", newline=""))]
for row in data:
    ws.append(row)

wb.save("Practice/ETL in Python/Myfile.xlsx")