import sqlite3
from xlsxwriter.workbook import Workbook


def spreadsheetConverter(fileName, tableName):
    outputName = fileName + ".xlsx"

    workbook = Workbook(outputName)
    worksheet = workbook.add_worksheet()

    conn=sqlite3.connect('Complaint_box.db')
    c=conn.cursor()
    # c.execute("select * from employees")
    mysel=c.execute("select * from " + tableName)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)
    workbook.close()