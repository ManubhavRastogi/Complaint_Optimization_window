import tkinter
# from main import addTechnician
from emailSender import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
from converter import *

import sqlite3


def viewAllTechnician():
    complaintWindow = tkinter.Tk()
    complaintWindow.title("Tech Support Partners")

    # technicianWindow = Toplevel()
    # technicianWindow.title("All Technicians")
    # technicianWindow.geometry("800X800")

    # Handling employees of selected product type data from database

    selectedEmployee = tkinter.StringVar(complaintWindow)

    def rbOnClick():
        print(selectedEmployee.get())


    def deleteTechnician():

        # create a database or connect to one
        conn = sqlite3.connect('Complaint_box.db')

                    # create cursor
        c = conn.cursor()


        c.execute("DELETE FROM employees WHERE employeeId = '" + selectedEmployee.get() + "'")



        # commit changes
        conn.commit()

                    # close connection
        conn.close()

        complaintWindow.destroy()

        viewAllTechnician()

    def exportData():
        spreadsheetConverter("employeesData", "employees")
        print("data exported")





    def viewDetailsWindow():
        detailsWindow = Toplevel(complaintWindow)
        detailsWindow.title("Technician's Details")
        detailsWindow.config(background="white")
        # detailsWindow.geometry("800x800")


        conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
        c = conn.cursor()                                       # create cursor
        
                    # Querying in database
        query = "SELECT employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode FROM employees WHERE employeeId =  '" + selectedEmployee.get() + "'"
        c.execute(query)
        reqEmployee = c.fetchall()



        defNameLabel = tkinter.Label(detailsWindow, text="Emp. Name : ", bg ="yellow")
        defNameLabel.grid(row=2, column= 0, sticky=tkinter.W)

        defEmailLabel = tkinter.Label(detailsWindow, text="Email : ", bg ="yellow")
        defEmailLabel.grid(row=4, column= 0, sticky=tkinter.W)

        defMobLabel = tkinter.Label(detailsWindow, text="Mobile : ", bg ="yellow")
        defMobLabel.grid(row=4, column= 3, sticky=tkinter.W)

        defExpLabel = tkinter.Label(detailsWindow, text="Expertise : ", bg ="yellow")
        defExpLabel.grid(row=2, column= 3, sticky=tkinter.W)

        defCityLabel = tkinter.Label(detailsWindow, text="City : ", bg ="yellow")
        defCityLabel.grid(row=6, column= 0, sticky=tkinter.W)

        defDisLabel = tkinter.Label(detailsWindow, text="District : ", bg ="yellow")
        defDisLabel.grid(row=6, column= 3, sticky=tkinter.W)

        defAddLabel = tkinter.Label(detailsWindow, text="Address : ", bg ="yellow")
        defAddLabel.grid(row=10, column= 0, sticky=tkinter.W)

        defPinLabel = tkinter.Label(detailsWindow, text="Pincode : ", bg ="yellow")
        defPinLabel.grid(row=8, column= 0, sticky=tkinter.W)



        for(employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode) in reqEmployee:
            empIdLabel = tkinter.Label(detailsWindow, text=employeeId, font='ariel 9 ')
            empIdLabel.grid(row=0, column= 2)

            nameLabel = tkinter.Label(detailsWindow, text=fullName, font='ariel 9 ')
            nameLabel.grid(row=2, column= 1)


            emailLabel = tkinter.Label(detailsWindow, text=email, font='ariel 9 ')
            emailLabel.grid(row=4, column= 1)

            mobileLabel = tkinter.Label(detailsWindow, text=mobile, font='ariel 9')
            mobileLabel.grid(row=4, column= 4)     

            expertiseLabel = tkinter.Label(detailsWindow, text=techExpertise, font='ariel 9 ')
            expertiseLabel.grid(row=2, column= 4)     

            cityLabel = tkinter.Label(detailsWindow, text=city,  font='ariel 9 ')
            cityLabel.grid(row=6, column= 1)     

            districtLabel = tkinter.Label(detailsWindow, text=district, font='ariel 9 ')
            districtLabel.grid(row=6, column= 4)     

            addLabel = tkinter.Label(detailsWindow, text=address, font='ariel 9 ')
            addLabel.grid(row=10, column= 1, columnspan=3)     

            pinLabel = tkinter.Label(detailsWindow, text=pincode, font='ariel 9 ')
            pinLabel.grid(row=8, column= 1)     

            detailsWindow.grid_rowconfigure([1, 3, 5, 7, 9], minsize=10)  # Here


        

    
    conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
    c = conn.cursor()                                       # create cursor
    
                # Querying in database
    query = "SELECT employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode FROM employees"
    c.execute(query)
    allEmployees = c.fetchall()
    listallEmployees = list(allEmployees)
    # print(listallEmployees)


    # Setting labels for selection window
    defEmpIdLabel = tkinter.Label(complaintWindow, text="Employee Id :", bg ="yellow", font='ariel 10 bold')
    defEmpIdLabel.grid(row=0, column= 0)
    defNameLabel = tkinter.Label(complaintWindow, text="Employee Name :", bg ="yellow", font='ariel 10 bold')
    defNameLabel.grid(row=0, column= 2)
    defEmailLabel = tkinter.Label(complaintWindow, text="Email :", bg="yellow", font='ariel 10 bold')
    defEmailLabel.grid(row=0, column= 4)
    defExpLabel = tkinter.Label(complaintWindow, text="Expertise :", bg ="yellow", font='ariel 10 bold')
    defExpLabel.grid(row=0, column= 6)
    rowVar = 1

    for(employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode) in listallEmployees:
        empIdLabel = tkinter.Label(complaintWindow, text=employeeId,font='ariel 9')
        empIdLabel.grid(row=rowVar, column=0)
        nameLabel = tkinter.Label(complaintWindow, text=fullName, font='ariel 9')
        nameLabel.grid(row=rowVar, column=2)
        emailLabel = tkinter.Label(complaintWindow, text=email, font='ariel 9')
        emailLabel.grid(row=rowVar, column=4)
        expertiseLabel = tkinter.Label(complaintWindow, text=techExpertise, font='ariel 9')
        expertiseLabel.grid(row=rowVar, column=6)

        rB = tkinter.Radiobutton(complaintWindow, variable=selectedEmployee, value=employeeId, command=rbOnClick)
        rB.grid(row=rowVar, column=7)


        rowVar = rowVar + 1
    

    b = tkinter.Button(complaintWindow, text="view Details", command= viewDetailsWindow)
    b.grid(row=rowVar+2, column=0, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    b2 = tkinter.Button(complaintWindow, text="delete technician", command= deleteTechnician)
    b2.grid(row=rowVar+2, column=4, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)

    b2 = tkinter.Button(complaintWindow, text="export all technician data", command= exportData)
    b2.grid(row=rowVar+2, column=6, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


    # setting space between columns
    complaintWindow.grid_columnconfigure([1,3,5], minsize=30)  # Here
