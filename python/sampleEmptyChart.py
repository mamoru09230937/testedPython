from openpyxl import Workbook
from openpyxl.chart import BarChart , Reference
from openpyxl.chart.layout import Layout, ManualLayout

wb = Workbook()
ws = wb.active

data  =[[]]
def createEmptyChart(ws) :
    
    for row in data:
        ws.append(row)
    values = Reference(ws, min_col = 1, max_col=1,min_row= 1, max_row = 1)
    chart = BarChart()
    chart.add_data(values)
    chart.x_axis.allow_none = True
    chart.y_axis.allow_none = True
    chart.y_axis.majorGridlines = None
    chart.legend = None
    chart.x_axis.delete = True
    chart.y_axis.delete = True
    chart.title ='Test'

    ws.add_chart(chart , 'A1')

createEmptyChart(ws)
wb.save('test.xlsx')