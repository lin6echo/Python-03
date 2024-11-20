import openpyxl

wb = openpyxl.load_workbook("Python-03/Excel/sample.xlsx")

sheet = wb.active

c = sheet["A3"]
c.value = "New Data"

wb.save("Python-03/Excel/sample.xlsx")