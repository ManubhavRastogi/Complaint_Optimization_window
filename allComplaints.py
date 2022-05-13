import tkinter
# from main import addTechnician
from emailSender import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry

import sqlite3


def viewAllComplaits():


    technicianWindow = tkinter.Tk()
    technicianWindow.title("All Complaints")
    # technicianWindow = Toplevel()
    # technicianWindow.title("All Technicians")
    # technicianWindow.geometry("12000X800")

    # Handling employees of selected product type data from database

    selectedComplaint = tkinter.StringVar(technicianWindow)

    

    def rbOnClick():
        print(selectedComplaint.get())


    def closeComplaintHandler():
        conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
        c = conn.cursor()                                       # create cursor

         # Querying in database
        query = "UPDATE complaints SET  status = 'close' WHERE invoiceNumber = '" + selectedComplaint.get() + "'"
        # print(query)
        c.execute(query)
        # allComplaints = c.fetchall()
        # listallComplaints = list(allComplaints)


        # commit changes
        conn.commit()

        # close connection
        conn.close()

        technicianWindow.destroy()

        viewAllComplaits()





    
    conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
    c = conn.cursor()                                       # create cursor
    
                # Querying in database
    query = "SELECT * FROM complaints"
    c.execute(query)
    allComplaints = c.fetchall()
    listallComplaints = list(allComplaints)
    # print(listallEmployees)


    # Setting labels for selection window
    l1 = tkinter.Label(technicianWindow, text="Customer Name", bg ="yellow")
    l1.grid(row=0, column= 0)

    l2 = tkinter.Label(technicianWindow, text="Customer Number", bg ="yellow")
    l2.grid(row=0, column= 2)

    l3 = tkinter.Label(technicianWindow, text="Customer Email", bg ="yellow")
    l3.grid(row=0, column= 4)

    l4 = tkinter.Label(technicianWindow, text="Customer address", bg ="yellow")
    l4.grid(row=0, column= 6)

    l5 = tkinter.Label(technicianWindow, text="Invoice Number", bg ="yellow")
    l5.grid(row=0, column= 8)

    l6 = tkinter.Label(technicianWindow, text="Customer City", bg ="yellow")
    l6.grid(row=0, column= 10)

    l7 = tkinter.Label(technicianWindow, text="Customer Pincode", bg ="yellow")
    l7.grid(row=0, column= 12)

    l8 = tkinter.Label(technicianWindow, text="Product Serial Number", bg ="yellow")
    l8.grid(row=0, column= 14)

    l9 = tkinter.Label(technicianWindow, text="Product Type", bg ="yellow")
    l9.grid(row=0, column= 16)

    l10 = tkinter.Label(technicianWindow, text="Product Name", bg ="yellow")
    l10.grid(row=0, column= 18)

    l11 = tkinter.Label(technicianWindow, text="Complaint Description", bg ="yellow")
    l11.grid(row=0, column= 20)

    l12 = tkinter.Label(technicianWindow, text="Allocated Technician", bg ="yellow")
    l12.grid(row=0, column= 22)

    l13 = tkinter.Label(technicianWindow, text="Complaint Date", bg ="yellow")
    l13.grid(row=0, column= 24)

    l14 = tkinter.Label(technicianWindow, text="Status", bg ="yellow")
    l14.grid(row=0, column= 26)
    

    rowVar = 1

    for(customerName, customerNmber, customerEmail, customerAddress, invoiceNumber, customerCity, customerPincode, productSerialNumber, productType, productName, complaintDescription, allocatedTechnician, complaintDate, status) in listallComplaints:
        t1 = tkinter.Label(technicianWindow, text=customerName)
        t1.grid(row=rowVar, column= 0)

        t2 = tkinter.Label(technicianWindow, text=customerNmber)
        t2.grid(row=rowVar, column= 2)

        t2 = tkinter.Label(technicianWindow, text=customerEmail)
        t2.grid(row=rowVar, column= 4)


        t3 = tkinter.Label(technicianWindow, text=customerAddress)
        t3.grid(row=rowVar, column= 6)

        t4 = tkinter.Label(technicianWindow, text=invoiceNumber)
        t4.grid(row=rowVar, column= 8)     

        t5 = tkinter.Label(technicianWindow, text=customerCity)
        t5.grid(row=rowVar, column= 10)     

        t6 = tkinter.Label(technicianWindow, text=customerPincode)
        t6.grid(row=rowVar, column= 12)     

        t7 = tkinter.Label(technicianWindow, text=productSerialNumber)
        t7.grid(row=rowVar, column= 14)     

        t8 = tkinter.Label(technicianWindow, text=productType)
        t8.grid(row=rowVar, column= 16)     

        t9 = tkinter.Label(technicianWindow, text=productName)
        t9.grid(row=rowVar, column= 18)     

        t10 = tkinter.Label(technicianWindow, text=complaintDescription)
        t10.grid(row=rowVar, column= 20)

        t11 = tkinter.Label(technicianWindow, text=allocatedTechnician)
        t11.grid(row=rowVar, column= 22)

        t12 = tkinter.Label(technicianWindow, text=complaintDate)
        t12.grid(row=rowVar, column= 24)

        t13 = tkinter.Label(technicianWindow, text=status)
        t13.grid(row=rowVar, column= 26)

        rB = tkinter.Radiobutton(technicianWindow, variable = selectedComplaint, value = invoiceNumber, command= rbOnClick)
        rB.grid(row=rowVar, column= 28)


        rowVar = rowVar + 1



    # selectedComplaint = tkinter.StringVar()

    b = tkinter.Button(technicianWindow, text="close Complaint", command= closeComplaintHandler)
    b.grid(row=rowVar+5, column=12, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    # selectionLabel = tkinter.Entry(technicianWindow, textVariable= selectedComplaint.set() )
    # selectionLabel.grid(row = rowVar+4, column = 12, rowspan=3, columnspan=3)

    # print(rowVar)
    # setting space between columns
    technicianWindow.grid_columnconfigure([1,3,5,7,9,11,13,15,17,19,21,23,25,27], minsize=10)  # Here

    # h = Scrollbar(technicianWindow, orient='horizontal')
    # h.grid(row = rowVar +1,side = BOTTOM, fill = X)
