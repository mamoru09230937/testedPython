data = [
    # first chart
    ['title' , 'test'],
    ['A' , 10 ,10],
    ['Arange' , 0 ,8],
    ['B' , 15 , 15] ,
    ['Brange' , 0 , 15] ,
    ['from' , 5 , 5],
    ['value' , 0 , 20],
    ['from' , 3 , 3],
    ['value' , 0 , 6],
    ['from' , 15 , 15],
    ['value' , 0 , 25],
    ['C' , 5 , 5],
    ['Crange' , 0 , 20] , 
    # Scond Chart
    ['title' , 'test2'],
    ['A' , 10 ,10],
    ['Arange' , 0 ,8],
    ['B' , 15 , 15] ,
    ['Brange' , 0 , 15] ,
    ['from' , 10, 10],
    ['value' , 0 , 20],
    ['from' , 13 , 13],
    ['value' , 0 , 6],
    ['from' , 20 , 20],
    ['value' , 0 , 25],
    ['C' , 5 , 5],
    ['Crange' , 0 , 20],
    ['end']
]

from openpyxl import Workbook
from openpyxl.chart import ScatterChart , Reference , Series

def createWorkBook () :
    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    chart = ScatterChart()
    chart.title = "Scatter Chart"
    chart.style = 13
    chart.x_axis.title = 'Size'
    chart.y_axis.title = 'Percentage'
    j = 1
    valueList = []
    for row in ws :
        for cell in row :
            chart = ScatterChart()
            if str(cell.value) == 'from' :
                xvalues = Reference(ws, min_col = 2, max_col=3, min_row = cell.row +1, max_row= cell.row +1)
                values = Reference(ws, min_col = 2, max_col=3,min_row= cell.row +2, max_row = cell.row +2)
                series = Series(values,xvalues ,  title_from_data=False)
                valueList.append(series)
            elif (str(cell.value) == 'title' and cell.row > 1) or str(cell.value) == 'end':
                for value in valueList :
                    chart.series.append(value)
                ws.add_chart(chart, "A10")
                valueList =  []
    wb.save('test.xlsx')

createWorkBook()