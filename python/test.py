from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    BarChart,
    Reference,
    Series,
)

wb = Workbook()
ws = wb.active

rows = [
    ['Aliens', 2, 3, 4, 5, 6, 7],
    ['Humans', 100, 100, 100, 100, 100, 100],
    ['Humans2', 50, 50, 50, 50, 50, 50],
    ['Humans3', 20, 20, 20, 20, 20, 20],
    ['Humans5', 2.67, 16.5, 17.5, 10],
]

for row in rows:
    ws.append(row)

c1 = BarChart()
v1 = Reference(ws, min_col=1, min_row=1, max_col=7)
c1.add_data(v1, titles_from_data=True, from_rows=True)

c1.x_axis.title = 'Days'
c1.y_axis.title = 'Aliens'
c1.y_axis.majorGridlines = None
c1.title = 'Survey results'


# Create a second chart
c2 = LineChart()
v2 = Reference(ws, min_col=1, min_row=2, max_col=7)
v3 = Reference(ws, min_col=1, min_row=3, max_col=7)
v4 = Reference(ws, min_col=1, min_row=4, max_col=7)
v5 = Reference(ws, min_col=1, min_row=5, max_col=7)
c2.add_data(v2, titles_from_data=True, from_rows=True)
c2.y_axis.axId = 200
c2.y_axis.title = "Humans"
c2.add_data(v3, titles_from_data=True, from_rows=True)
c2.add_data(v4, titles_from_data=True, from_rows=True)
c2.add_data(v5, titles_from_data=True, from_rows=True)
s1 = c2.series[3]
s1.graphicalProperties.line.noFill = True
s1.marker.symbol = "circle"
s1.marker.size = 14 # width in EMUs

# Display y-axis of the second chart on the right by setting it to cross the x-axis at its maximum
c1.y_axis.crosses = "max"
c1 += c2 
ws.add_chart(c1, "D4")

wb.save("secondary.xlsx")