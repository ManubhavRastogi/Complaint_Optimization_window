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
    technicianWindow.title("Complaint Optimization Window")
    # technicianWindow = Toplevel()
    # technicianWindow.title("All Technicians")
    # technicianWindow.geometry("800X800")

    # Handling employees of selected product type data from database
    
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

    defMobLabel = tkinter.Label(technicianWindow, text="Mobile", bg ="yellow")
    defMobLabel.grid(row=0, column= 6)

    defExpLabel = tkinter.Label(technicianWindow, text="Expertise", bg ="yellow")
    defExpLabel.grid(row=0, column= 8)

    defCityLabel = tkinter.Label(technicianWindow, text="City", bg ="yellow")
    defCityLabel.grid(row=0, column= 10)

    defDisLabel = tkinter.Label(technicianWindow, text="District", bg ="yellow")
    defDisLabel.grid(row=0, column= 12)

    defAddLabel = tkinter.Label(technicianWindow, text="Address", bg ="yellow")
    defAddLabel.grid(row=0, column= 14)

    defPinLabel = tkinter.Label(technicianWindow, text="Pincode", bg ="yellow")
    defPinLabel.grid(row=0, column= 16)
    

    rowVar = 1

    for(employeeId, fullName, email, mobile, techExpertise, city, district, address, pincode) in listallEmployees:
        empIdLabel = tkinter.Label(technicianWindow, text=employeeId)
        empIdLabel.grid(row=rowVar, column= 0)

        nameLabel = tkinter.Label(technicianWindow, text=fullName)
        nameLabel.grid(row=rowVar, column= 2)


        emailLabel = tkinter.Label(technicianWindow, text=email)
        emailLabel.grid(row=rowVar, column= 4)

        mobileLabel = tkinter.Label(technicianWindow, text=mobile)
        mobileLabel.grid(row=rowVar, column= 6)     

        expertiseLabel = tkinter.Label(technicianWindow, text=techExpertise)
        expertiseLabel.grid(row=rowVar, column= 8)     

        cityLabel = tkinter.Label(technicianWindow, text=city)
        cityLabel.grid(row=rowVar, column= 10)     

        districtLabel = tkinter.Label(technicianWindow, text=district)
        districtLabel.grid(row=rowVar, column= 12)     

        addLabel = tkinter.Label(technicianWindow, text=address)
        addLabel.grid(row=rowVar, column= 14)     

        pinLabel = tkinter.Label(technicianWindow, text=pincode)
        pinLabel.grid(row=rowVar, column= 16)     


        rowVar = rowVar + 1


    # setting space between columns
    technicianWindow.grid_columnconfigure([1,3,5,7,9,11,13,15], minsize=30)  # Here
