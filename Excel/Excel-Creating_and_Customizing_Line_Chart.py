import openpyxl

# import LineChart class from openpyxl.chart sub_module
from openpyxl.chart import LineChart, Reference
wb = openpyxl.Workbook()
sheet = wb.active

# write 0 to 9 in 1st column of the active sheet
for i in range(10):
    sheet.append([i])

values = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# create object of LineChart class
chart = LineChart()
chart.add_data(values)

# set the title of the chart
chart.title = ("LINE-CHART")

# set the title of the x-axis
chart.x_axis.title = "X-AXIS"

# set the title of the y-axis
chart.y_axis.title = "Y-AXIS"
sheet.add_chart(chart, "E2")

wb.save("Excel/sample6.xlsx")