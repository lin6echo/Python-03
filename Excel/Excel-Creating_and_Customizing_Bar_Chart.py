import openpyxl

from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()

sheet = wb.active

# write 0 to 9 in 1st column of the active sheet
for i in range(10):
    sheet.append([i])

# create data for plotting
values = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# create object of BarChart class
chart = BarChart()

# adding data to the Bar chart object
chart.add_data(values)

# set the title of the chart
chart.title = "BAR-CHART"

# set the title of the x-axis
chart.x_axis.title = "X-AXIS"

# SET the title of y-axis
chart.y_axis.title = "Y-AXIS"

sheet.add_chart(chart, "E2")

wb.save("Excel/sample5.xlsx")




