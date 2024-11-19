import openpyxl
from openpyxl.drawing.image import Image

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append([10, 2010, "Geeks", 4, "life"])

img = Image("Excel/GeeksforGeeks.png")

sheet.add_image(img, "A2")

wb.save("Excel/sample7.xlsx")