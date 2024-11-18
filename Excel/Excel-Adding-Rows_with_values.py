import openpyxl

wb = openpyxl.load_workbook("Python-03/Excel/sample.xlsx")

sheet = wb.active

data = (
    (1, 2, 3),
    (4, 5, 6)
)

for row in data:
    sheet.append(row)

wb.save("Python-03/Excel/sample.xlsx")