import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

sheet["A1"] = 200
sheet["A2"] = 300
sheet["A3"] = 400
sheet["A4"] = 500
sheet["A5"] = 600

sheet["A7"] = "= SUM(A1:A5)"

wb.save("Python-03/Excel/sum.xlsx")