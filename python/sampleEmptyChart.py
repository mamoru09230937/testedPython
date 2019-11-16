from openpyxl import Workbook
from openpyxl.chart import BarChart

wb = Workbook()
ws = wb.active

def createEmptyChart(ws) :
    chart = BarChart()
    chart.title ='Test'
    ws.add_chart(chart , 'A1')

createEmptyChart(ws)
wb.save('test.xlsx')