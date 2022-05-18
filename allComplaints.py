import tkinter
# from main import addTechnician
from emailSender import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry

from converter import *

from map import *

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




    def deleteComplaint():
        # create a database or connect to one
        conn = sqlite3.connect('Complaint_box.db')

                    # create cursor
        c = conn.cursor()


        c.execute("DELETE FROM complaints WHERE invoiceNumber = '" + selectedComplaint.get() + "'")




        # commit changes
        conn.commit()

                    # close connection
        conn.close()

        technicianWindow.destroy()

        viewAllComplaits()

    def exportData():
        spreadsheetConverter("complaintsData", "complaints")
        print("data exported")




    def viewDetailsWindow():
        detailsWindow=Toplevel(technicianWindow)
        detailsWindow.title("Complaint Details")
        # detailsWindow.geometry("800x800")


        conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
        c = conn.cursor()                                       # create cursor
        
                    # Querying in database
        query = "SELECT * FROM complaints WHERE invoiceNumber =  '" + selectedComplaint.get() + "'"
        c.execute(query)
        reqComplaint = c.fetchall()



        l1 = tkinter.Label(detailsWindow, text="Customer Name", font='ariel 9 bold', bg ="yellow")
        l1.grid(row=2, column= 0, sticky=tkinter.W)
        l2 = tkinter.Label(detailsWindow, text="Customer Mobile", font='ariel 9 bold', bg ="yellow")
        l2.grid(row=4, column= 0, sticky=tkinter.W)
        l3 = tkinter.Label(detailsWindow, text="Customer Email", font='ariel 9 bold', bg ="yellow")
        l3.grid(row=2, column= 3, sticky=tkinter.W)
        l4 = tkinter.Label(detailsWindow, text="Customer address", font='ariel 9 bold', bg ="yellow")
        l4.grid(row=6, column= 0, sticky=tkinter.W)
        l6 = tkinter.Label(detailsWindow, text="Customer City", font='ariel 9 bold', bg ="yellow")
        l6.grid(row=4, column= 3, sticky=tkinter.W)
        l7 = tkinter.Label(detailsWindow, text="Customer Pincode", font='ariel 9 bold', bg ="yellow")
        l7.grid(row=6, column= 3, sticky=tkinter.W)
        l18 = tkinter.Label(detailsWindow, text="Complaint's Detail", font='ariel 9 bold', bg ="yellow")
        l18.grid(row=8, column= 2, sticky=tkinter.W)
        l8 = tkinter.Label(detailsWindow, text="Product Serial Number", font='ariel 9 bold', bg ="yellow")
        l8.grid(row=10, column= 0, sticky=tkinter.W)
        l9 = tkinter.Label(detailsWindow, text="Product Type", font='ariel 9 bold', bg ="yellow")
        l9.grid(row=12, column= 0, sticky=tkinter.W)
        l10 = tkinter.Label(detailsWindow, text="Product Name", font='ariel 9 bold', bg ="yellow")
        l10.grid(row=12, column= 3, sticky=tkinter.W)
        l11 = tkinter.Label(detailsWindow, text="Complaint Description", font='ariel 9 bold', bg="yellow")
        l11.grid(row=14, column= 0, sticky=tkinter.W)
        l12 = tkinter.Label(detailsWindow, text="Allocated Technician", font='ariel 9 bold', bg ="yellow")
        l12.grid(row=14, column= 3, sticky=tkinter.W)
        l13 = tkinter.Label(detailsWindow, text="Complaint Date", font='ariel 9 bold', bg ="yellow")
        l13.grid(row=10, column= 3, sticky=tkinter.W)
        l14 = tkinter.Label(detailsWindow, text="Status", font='ariel 9 bold', bg ="yellow")
        l14.grid(row=16, column= 0, sticky=tkinter.W)

        for(customerName, customerNmber, customerEmail, customerAddress, invoiceNumber, customerCity, customerPincode, productSerialNumber, productType, productName, complaintDescription, allocatedTechnician, complaintDate, status) in reqComplaint:
            t1=tkinter.Label(detailsWindow, text=customerName)
            t1.grid(row=2, column=1)
            detailsWindow.grid_rowconfigure([1, 3, 5, 7, 9], minsize=10)  # Here
            t2=tkinter.Label(detailsWindow, text=customerNmber)
            t2.grid(row=4, column=1)
            t2 = tkinter.Label(detailsWindow, text=customerEmail)
            t2.grid(row=2, column=4)
            t3 = tkinter.Label(detailsWindow, text=customerAddress)
            t3.grid(row=6, column=1, columnspan=2)
            t4 = tkinter.Label(detailsWindow, text=invoiceNumber)
            t4.grid(row=0, column=2)
            t5 = tkinter.Label(detailsWindow, text=customerCity)
            t5.grid(row=4, column=4)
            t6 = tkinter.Label(detailsWindow, text=customerPincode)
            t6.grid(row=6, column=4)
            t7 = tkinter.Label(detailsWindow, text=productSerialNumber)
            t7.grid(row=10, column=1)
            t8 = tkinter.Label(detailsWindow, text=productType)
            t8.grid(row=12, column=1)
            t9 = tkinter.Label(detailsWindow, text=productName)
            t9.grid(row=12, column=4)
            t10 = tkinter.Label(detailsWindow, text=complaintDescription)
            t10.grid(row=14, column=1, columnspan=2)
            t11 = tkinter.Label(detailsWindow, text=allocatedTechnician)
            t11.grid(row=14, column=4)
            t12 = tkinter.Label(detailsWindow, text=complaintDate)
            t12.grid(row=10, column=4)
            t13 = tkinter.Label(detailsWindow, text=status)
            t13.grid(row=16, column=1)
            detailsWindow.grid_rowconfigure([1, 3, 5, 7, 9, 11, 13, 15], minsize=10)  # Here


        def mapHandler():

            conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
            c = conn.cursor()                                       # create cursor
            
                        # Querying in database
            query = "SELECT employeeId, address FROM employees WHERE employeeId =  '" + allocatedTechnician + "'"
            c.execute(query)
            emplyoeeDetail = c.fetchall()

            for(employeeId,address) in emplyoeeDetail:
                employeeAddress = address


            # print(customerAddress)

            mapCreator(employeeAddress, customerAddress)


        def emailHandler():

            # print(status)

            if status == "open":
                subject = """Your complaint is in progress"""

                message = """
                        
                <p1> 
                    Your complaint has been registered successfully.
                </p1><br>
                <p2>
                    We are working on your complaint, We will soon contact you.
                </p2>

                """
                mailer(customerEmail, subject, message)

            elif status == "close":
                subject = """Complaint Status"""

                message = """
                        
                <p1> 
                    Your Complaint has been resolved successfully.
                </p1><br>
                <p2>
                    Please provide your feedback on our website.
                </p2>

                """
                mailer(customerEmail, subject, message)



                



        b = tkinter.Button(detailsWindow, text="close complaint", command= closeComplaintHandler)
        b.grid(row=17, column=0, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


        b2 = tkinter.Button(detailsWindow, text="view on map", command=mapHandler)
        b2.grid(row=17, column=2, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


        b3 = tkinter.Button(detailsWindow, text="email status", command= emailHandler)
        b3.grid(row=17, column=4, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)





    
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
    l1.grid(row=0, column= 2)

    l2 = tkinter.Label(technicianWindow, text="Customer Mobile", bg ="yellow")
    l2.grid(row=0, column= 4)

    l5 = tkinter.Label(technicianWindow, text="Invoice Number", bg ="yellow")
    l5.grid(row=0, column= 0)

    l9 = tkinter.Label(technicianWindow, text="Product Type", bg ="yellow")
    l9.grid(row=0, column= 6)

    l10 = tkinter.Label(technicianWindow, text="Product Name", bg ="yellow")
    l10.grid(row=0, column= 8)

    l12 = tkinter.Label(technicianWindow, text="Allocated Technician", bg ="yellow")
    l12.grid(row=0, column= 10)

    l13 = tkinter.Label(technicianWindow, text="Complaint Date", bg ="yellow")
    l13.grid(row=0, column= 12)

    l14 = tkinter.Label(technicianWindow, text="Status", bg ="yellow")
    l14.grid(row=0, column= 14)
    

    rowVar = 1

    for(customerName, customerNmber, customerEmail, customerAddress, invoiceNumber, customerCity, customerPincode, productSerialNumber, productType, productName, complaintDescription, allocatedTechnician, complaintDate, status) in listallComplaints:
        
        t1 = tkinter.Label(technicianWindow, text=invoiceNumber)
        t1.grid(row=rowVar, column= 0)  

        t2 = tkinter.Label(technicianWindow, text=customerName)
        t2.grid(row=rowVar, column= 2)

        t3 = tkinter.Label(technicianWindow, text=customerNmber)
        t3.grid(row=rowVar, column= 4)

        t4 = tkinter.Label(technicianWindow, text=productType)
        t4.grid(row=rowVar, column= 6)     

        t5 = tkinter.Label(technicianWindow, text=productName)
        t5.grid(row=rowVar, column= 8)     

        t6 = tkinter.Label(technicianWindow, text=allocatedTechnician)
        t6.grid(row=rowVar, column= 10)

        t7 = tkinter.Label(technicianWindow, text=complaintDate)
        t7.grid(row=rowVar, column= 12)

        t8 = tkinter.Label(technicianWindow, text=status)
        t8.grid(row=rowVar, column= 14)

        rB = tkinter.Radiobutton(technicianWindow, variable = selectedComplaint, value = invoiceNumber, command= rbOnClick)
        rB.grid(row=rowVar, column= 15)


        rowVar = rowVar + 1



    b = tkinter.Button(technicianWindow, text="view details", command= viewDetailsWindow)
    b.grid(row=rowVar+5, column=2, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    b2 = tkinter.Button(technicianWindow, text="delete complaint", command= deleteComplaint)
    b2.grid(row=rowVar+5, column=7, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    b2 = tkinter.Button(technicianWindow, text="exports all complaints", command= exportData)
    b2.grid(row=rowVar+5, column=12, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    # setting space between columns
    technicianWindow.grid_columnconfigure([1,3,5,7,9,11,13], minsize=10)  # Here
