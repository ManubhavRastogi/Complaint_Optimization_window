import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect('complaint_box.db')
c=conn.cursor()
# c.execute("select * from employees")
mysel=c.execute("select * from employees ")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
workbook.close()