import tkinter
# from main import addTechnician
from emailSender import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry

import sqlite3


def viewAllTechnician():
    technicianWindow = tkinter.Tk()
    technicianWindow.title("Tech Support Partners")
    # technicianWindow = Toplevel()
    # technicianWindow.title("All Technicians")
    # technicianWindow.geometry("800X800")

    # Handling employees of selected product type data from database

    selectedEmployee = tkinter.StringVar(technicianWindow)

    def rbOnClick():
        print(selectedEmployee.get())



    def viewDetailsWindow():
        detailsWindow = Toplevel(technicianWindow)
        detailsWindow.title("Technician's Details")
        # detailsWindow.geometry("800x800")


        conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
        c = conn.cursor()                                       # create cursor
        
                    # Querying in database
        query = "SELECT employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode FROM employees WHERE employeeId =  '" + selectedEmployee.get() + "'"
        c.execute(query)
        reqEmployee = c.fetchall()



        defNameLabel = tkinter.Label(detailsWindow, text="Emp. Name: ", bg ="yellow")
        defNameLabel.grid(row=2, column= 0, sticky=tkinter.W)

        defEmailLabel = tkinter.Label(detailsWindow, text="Email: ", bg ="yellow")
        defEmailLabel.grid(row=4, column= 0, sticky=tkinter.W)

        defMobLabel = tkinter.Label(detailsWindow, text="Mobile: ", bg ="yellow")
        defMobLabel.grid(row=4, column= 3, sticky=tkinter.W)

        defExpLabel = tkinter.Label(detailsWindow, text="Expertise: ", bg ="yellow")
        defExpLabel.grid(row=2, column= 3, sticky=tkinter.W)

        defCityLabel = tkinter.Label(detailsWindow, text="City: ", bg ="yellow")
        defCityLabel.grid(row=6, column= 0, sticky=tkinter.W)

        defDisLabel = tkinter.Label(detailsWindow, text="District: ", bg ="yellow")
        defDisLabel.grid(row=6, column= 3, sticky=tkinter.W)

        defAddLabel = tkinter.Label(detailsWindow, text="Address: ", bg ="yellow")
        defAddLabel.grid(row=10, column= 0, sticky=tkinter.W)

        defPinLabel = tkinter.Label(detailsWindow, text="Pincode: ", bg ="yellow")
        defPinLabel.grid(row=8, column= 0, sticky=tkinter.W)



        for(employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode) in reqEmployee:
            empIdLabel = tkinter.Label(detailsWindow, text=employeeId)
            empIdLabel.grid(row=0, column= 2)

            nameLabel = tkinter.Label(detailsWindow, text=fullName)
            nameLabel.grid(row=2, column= 1)


            emailLabel = tkinter.Label(detailsWindow, text=email)
            emailLabel.grid(row=4, column= 1)

            mobileLabel = tkinter.Label(detailsWindow, text=mobile)
            mobileLabel.grid(row=4, column= 4)     

            expertiseLabel = tkinter.Label(detailsWindow, text=techExpertise)
            expertiseLabel.grid(row=2, column= 4)     

            cityLabel = tkinter.Label(detailsWindow, text=city)
            cityLabel.grid(row=6, column= 1)     

            districtLabel = tkinter.Label(detailsWindow, text=district)
            districtLabel.grid(row=6, column= 4)     

            addLabel = tkinter.Label(detailsWindow, text=address)
            addLabel.grid(row=10, column= 1, columnspan=3)     

            pinLabel = tkinter.Label(detailsWindow, text=pincode)
            pinLabel.grid(row=8, column= 1)     

            detailsWindow.grid_rowconfigure([1,3,5,7,9], minsize=10)  # Here


        

    
    conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
    c = conn.cursor()                                       # create cursor
    
                # Querying in database
    query = "SELECT employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode FROM employees"
    c.execute(query)
    allEmployees = c.fetchall()
    listallEmployees = list(allEmployees)
    # print(listallEmployees)


    # Setting labels for selection window
    defEmpIdLabel = tkinter.Label(technicianWindow, text="Emp. Id", bg ="yellow")
    defEmpIdLabel.grid(row=0, column= 0)

    defNameLabel = tkinter.Label(technicianWindow, text="Emp. Name", bg ="yellow")
    defNameLabel.grid(row=0, column= 2)

    defEmailLabel = tkinter.Label(technicianWindow, text="Email", bg ="yellow")
    defEmailLabel.grid(row=0, column= 4)

    # defMobLabel = tkinter.Label(technicianWindow, text="Mobile", bg ="yellow")
    # defMobLabel.grid(row=0, column= 6)

    defExpLabel = tkinter.Label(technicianWindow, text="Expertise", bg ="yellow")
    defExpLabel.grid(row=0, column= 6)

    # defCityLabel = tkinter.Label(technicianWindow, text="City", bg ="yellow")
    # defCityLabel.grid(row=0, column= 10)

    # defDisLabel = tkinter.Label(technicianWindow, text="District", bg ="yellow")
    # defDisLabel.grid(row=0, column= 12)

    # defAddLabel = tkinter.Label(technicianWindow, text="Address", bg ="yellow")
    # defAddLabel.grid(row=0, column= 14)

    # defPinLabel = tkinter.Label(technicianWindow, text="Pincode", bg ="yellow")
    # defPinLabel.grid(row=0, column= 16)
    

    rowVar = 1

    for(employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode) in listallEmployees:
        empIdLabel = tkinter.Label(technicianWindow, text=employeeId)
        empIdLabel.grid(row=rowVar, column= 0)

        nameLabel = tkinter.Label(technicianWindow, text=fullName)
        nameLabel.grid(row=rowVar, column= 2)


        emailLabel = tkinter.Label(technicianWindow, text=email)
        emailLabel.grid(row=rowVar, column= 4)

        # mobileLabel = tkinter.Label(technicianWindow, text=mobile)
        # mobileLabel.grid(row=rowVar, column= 6)     

        expertiseLabel = tkinter.Label(technicianWindow, text=techExpertise)
        expertiseLabel.grid(row=rowVar, column= 6)     

        # cityLabel = tkinter.Label(technicianWindow, text=city)
        # cityLabel.grid(row=rowVar, column= 10)     

        # districtLabel = tkinter.Label(technicianWindow, text=district)
        # districtLabel.grid(row=rowVar, column= 12)     

        # addLabel = tkinter.Label(technicianWindow, text=address)
        # addLabel.grid(row=rowVar, column= 14)     

        # pinLabel = tkinter.Label(technicianWindow, text=pincode)
        # pinLabel.grid(row=rowVar, column= 16)     

        rB = tkinter.Radiobutton(technicianWindow, variable = selectedEmployee, value = employeeId, command= rbOnClick)
        rB.grid(row=rowVar, column= 7)


        rowVar = rowVar + 1
    

    b = tkinter.Button(technicianWindow, text="view Details", command= viewDetailsWindow)
    b.grid(row=rowVar+2, column=4, columnspan=1, rowspan=2, sticky=tkinter.W +
        tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


    # setting space between columns
    technicianWindow.grid_columnconfigure([1,3,5], minsize=30)  # Here
