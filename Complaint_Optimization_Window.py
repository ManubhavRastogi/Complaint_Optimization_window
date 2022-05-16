import email
import tkinter
    # from main import addTechnician
from emailSender import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
from allTechnician import *
from allComplaints import *
import sqlite3


def addComplaint():

    # creates a Tk() object
    master = tkinter.Tk()
    master.title("Complaint Optimization Window")
    #master.geometry("680x300")
    serviceOptions = [
            "Air Conditioner and fans",
            "Washing Machine",
            "Audio and Video electronic",
        ]

    selectedTechnician = tkinter.StringVar()




    def selectTechSupport():


        # settig window for selection of technician
        selectionWindow = Toplevel()
        selectionWindow.title("Select Support Partner")
        selectionWindow.geometry("600x600")


        # Handling employees of selected product type data from database
        
        conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
        c = conn.cursor()                                       # create cursor
        
                    # Querying in database
        query = "SELECT employeeId, fullName, city, oid FROM employees WHERE techExpertise = '" + prdctType.get() + "'"
        c.execute(query)
        records = c.fetchall()
        listRecords = list(records)
        # print(listRecords)


        

        # Setting labels for selection window
        defEmpIdLabel = tkinter.Label(selectionWindow, text="Emp. Id")
        defEmpIdLabel.grid(row=0, column= 0)

        defNameLabel = tkinter.Label(selectionWindow, text="Emp. Name")
        defNameLabel.grid(row=0, column= 2)

        defCityLabel = tkinter.Label(selectionWindow, text="Emp. City")
        defCityLabel.grid(row=0, column= 4)



        # setting space between columns
        selectionWindow.grid_columnconfigure([1,3,5], minsize=75)  # Here
        # selectionWindow.grid_columnconfigure(3, minsize=75)  # Here
        # selectionWindow.grid_columnconfigure(5, minsize=75)  # Here


        rowVar = 1               # declaring variable to icrement between rows for selecting employees


        #  radio button controller
        def rbOnClick():
            print(selectedTechnician.get())
            # selectionVariable = v.get()
            selectionButton.config(text=selectedTechnician.get())
            selectionWindow.destroy()




        #  Updating tech support partner details from databse on basis of Product type
        for(techId, name, city, oid) in listRecords:
            empIdLabel = tkinter.Label(selectionWindow, text=techId)
            empIdLabel.grid(row=rowVar, column= 0)

            nameLabel = tkinter.Label(selectionWindow, text=name)
            nameLabel.grid(row=rowVar, column= 2)


            cityLabel = tkinter.Label(selectionWindow, text=city)
            cityLabel.grid(row=rowVar, column= 4)        

            rB = tkinter.Radiobutton(selectionWindow, variable = selectedTechnician,
                value = techId, command= rbOnClick)
            rB.grid(row=rowVar, column= 6)

            rowVar = rowVar + 1


        selectionWindow.mainloop()


    def addTechnician():

        window = Toplevel()
        

        empId = tkinter.StringVar()
        name = tkinter.StringVar()
        email = tkinter.StringVar()
        mobile = tkinter.StringVar()
        techExpertise = tkinter.StringVar()
        city = tkinter.StringVar()
        district = tkinter.StringVar()
        address = tkinter.StringVar()
        state = tkinter.StringVar()
        pincode = tkinter.StringVar()

        result = tkinter.StringVar()




        def addEmployeeHandler():

            # create a database or connect to one
            conn = sqlite3.connect('Complaint_box.db')

            # create cursor
            c = conn.cursor()

            # Insert into table

            c.execute("INSERT INTO employees VALUES (:employeeId, :fullName, :email, :mobile, :techExpertise, :city, :district, :address, :state, :pincode) ",
            {
                'employeeId': empId.get(),
                'fullName': name.get(),
                'email': email.get(),
                'mobile': mobile.get(),
                'techExpertise': techExpertise.get(),
                'city': city.get(),
                'district': district.get(),
                'address': address.get(),
                'state': state.get(),
                'pincode': pincode.get()
            })

            # commit changes
            conn.commit()

            # close connection
            conn.close()

            
            # configuring job confirmation mail to tech support employee
            subject = 'Hired as technician in Royal Tech Support'

            message = 'This is my message'

            mailsender(reciever= email.get(), subject=subject, message= message)


            # print(name.get())
            # print(empId.get())
            # print(techExpertise.get())

            t1.delete(0,END); 
            t2.delete(0, END); t3.delete(0,END); t4.delete(0,END); t6.delete(0,END); 
            t7.delete(0,END); t8.delete(0,END); t9.delete(0,END); t10.delete(0,END); 
            techExpertise.set("                               ")



        def query():
            # create a database or connect to one
            conn = sqlite3.connect('Complaint_box.db')

            # create cursor
            c = conn.cursor()

            c.execute("SELECT *, oid FROM employees")
            records = c.fetchall()
            print(list(records))

        

        # create a database or connect to one
        conn = sqlite3.connect('Complaint_box.db')

        # create cursor
        c = conn.cursor()


        # create table

        # c.execute(""" CREATE TABLE employees (
        #     employeeId text,
        #     fullName text,
        #     email text,
        #     mobile text,
        #     techExpertise text,
        #     city text,
        #     district text,
        #     address text,
        #     state text,
        #     pincode text
        #     )""")

        # commit changes
        conn.commit()

        # close connection
        conn.close()





        l1 = tkinter.Label(window, text="Enter Employee Id:").grid(row=0, sticky=tkinter.W)
        l2 = tkinter.Label(window, text="Enter Full Name:").grid(row=1, sticky=tkinter.W)
        l3 = tkinter.Label(window, text="Enter Email Adddress:").grid(row=2, sticky=tkinter.W)
        l4 = tkinter.Label(window, text="Enter Mobile Number:").grid(row=3, sticky=tkinter.W)
        l5 = tkinter.Label(window, text="Select Tech Expertise:").grid(row=4, sticky=tkinter.W)


        l6 = tkinter.Label(window, text="Enter city:").grid(row=5, sticky=tkinter.W)
        l7 = tkinter.Label(window, text="Enter district:").grid(row=6, sticky=tkinter.W)
        l8 = tkinter.Label(window, text="Enter address:").grid(row=7, sticky=tkinter.W)
        l9 = tkinter.Label(window, text="Enter state:").grid(row=8, sticky=tkinter.W)
        l10 = tkinter.Label(window, text="Enter pincode:").grid(row=9, sticky=tkinter.W)


        t1 = tkinter.Entry(window, textvariable=empId)
        t1.grid(row=0, column=3)
        t2 = tkinter.Entry(window, textvariable=name)
        t2.grid(row=1, column=3)
        t3 = tkinter.Entry(window, textvariable=email)
        t3.grid(row=2, column=3)
        t4 = tkinter.Entry(window, textvariable=mobile)
        t4.grid(row=3, column=3)
        #t5 = tkinter.Entry(window, textvariable=techExpertise).grid(row=4,column=1)

        techExpertise.set("                               ")
        drop = tkinter.OptionMenu(window, techExpertise, *serviceOptions)
        drop.grid(row=4, column=3)

        t6 = tkinter.Entry(window, textvariable=city)
        t6.grid(row=5, column=3)
        t7 = tkinter.Entry(window, textvariable=district)
        t7.grid(row=6, column=3)
        t8 = tkinter.Entry(window, textvariable=address)
        t8.grid(row=7, column=3)
        t9 = tkinter.Entry(window, textvariable=state)
        t9.grid(row=8, column=3)
        t10 = tkinter.Entry(window, textvariable=pincode)
        t10.grid(row=9, column=3)

        # Button for adding employee
        b = tkinter.Button(window, text="Add Employee", command=addEmployeeHandler)
        b.grid(row=20, column=1, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


        # Button for querying in employee
        b = tkinter.Button(window, text="show Employees", command=query)
        b.grid(row=24, column=1, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)


        window.mainloop()



        


    # lable = Lable(master,text = "Complaint Optimization Window")
    # label.pack(side = TOP, pady = 10)

    label = tkinter.Label(text="Complaint Optimization Window")
    label.grid(row=0, column = 3, sticky= W,pady=2)


    # lable for selecting employee codes
    label = tkinter.Label(text="Costumer Details")
    label.grid(row=1, column=3)
    #l1 = tkinter.Label(master, text='Costumer Name') l1.grid(row=3,column=0)
    #l1 = tkinter.Label(master, text='Phone No. ') l1.grid(row=3,column=4)
    #l1 = tkinter.Label(master, text='Select the employee code') l1.grid(row=2,column=0)
    #emp_list = ["53258xed","67062bhd","84754geu","72209yei"] empId = tkinter.StringVar()
    #empId.set("                               ")
    #drop = tkinter.OptionMenu(master, empId, *emp_list)
    #drop.grid(row=2, column=2)
    l1 = tkinter.Label(master, text="Name :").grid(row=2, sticky=tkinter.W)
    l2 = tkinter.Label(master, text="Phone No :").grid(row=2,column=4, sticky=tkinter.W)
    l3 = tkinter.Label(master, text="Costumer Adddress :").grid(row=3, sticky=tkinter.W)
    l4 = tkinter.Label(master, text="City :").grid(row=4,column=0, sticky=tkinter.W)
    emailLabel = tkinter.Label(master, text="Email :").grid(row=5,column=0, sticky=tkinter.W)
    l5 = tkinter.Label(master, text="Pincode :").grid(row=4,column=4, sticky=tkinter.W)
    l6 = tkinter.Label(master, text="Invoice No. :").grid(row=3,column=4, sticky=tkinter.W)

    label = tkinter.Label(text="Complaint Detail From")
    label.grid(row=6, column=3)

    l7 = tkinter.Label(master, text="Product Serial No.:").grid(row=7, sticky=tkinter.W)
    l8 = tkinter.Label(master, text="Product Type :").grid(row=8, sticky=tkinter.W)
    l8 = tkinter.Label(master, text="Complaint date :").grid(row=7,column=4)
    l8 = tkinter.Label(master, text="Product Name :").grid(row=8,column=4)

    l9 = tkinter.Label(master, text="Complaint Details").grid(row=9, sticky=tkinter.W)
    l10 = tkinter.Label(master, text="Allocate technician").grid(row=9,column=4, sticky=tkinter.W)
    # l11 = tkinter.Label(master, text="Enter state :").grid(row=10, sticky=tkinter.W)
    # l12 = tkinter.Label(master,text="Enter pincode :").grid(row=11, sticky=tkinter.W)


    # Custmer detail Variable initialised
    cstmrName = tkinter.StringVar()
    cstmrNmbr = tkinter.StringVar()
    cstmrAdrs = tkinter.StringVar()
    invoiceNo = tkinter.StringVar()
    cstmrCity = tkinter.StringVar()
    cstmrEmail = tkinter.StringVar()
    cstmrPincode = tkinter.StringVar()

    # Product detail Variable initialised
    prdctNo = tkinter.StringVar()
    prdctType = tkinter.StringVar()
    prdctName = tkinter.StringVar()
    complaintDetails = tkinter.StringVar()
    # allocateTechnician = tkinter.StringVar()
    complaintDate = tkinter.StringVar()
    # address = tkinter.StringVar()
    # state = tkinter.StringVar()
    # pincode = tkinter.StringVar()

    def addComplaint():
        # create a database or connect to one
        conn = sqlite3.connect('Complaint_box.db')

        # create cursor
        c = conn.cursor()

        # create complaint table
        # c.execute(""" CREATE TABLE complaints (
        #     customerName text,
        #     customerNumber text,
        #     customerEmail text,
        #     customerAddress text,
        #     invoiceNumber text,
        #     customerCity text,
        #     customerPincode text,
        #     productSerialNumber text,
        #     productType text,
        #     productName text,
        #     complaintDescription text,
        #     allocatedTechnician text,
        #     complaintDate text,
        #     status text
        #     )""")

        # Insert into table

        c.execute("INSERT INTO complaints VALUES (:customerName, :customerNumber, :customerEmail, :customerAddress, :invoiceNumber, :customerCity, :customerPincode, :productSerialNumber, :productType, :productName, :complaintDescription, :allocatedTechnician, :complaintDate, :status) ",
        {
            'customerName': cstmrName.get(),
            'customerNumber': cstmrNmbr.get(),
            'customerEmail': cstmrEmail.get(),
            'customerAddress': cstmrAdrs.get(),
            'invoiceNumber': invoiceNo.get(),
            'customerCity': cstmrCity.get(),
            'customerPincode': cstmrPincode.get(),
            'productSerialNumber': prdctNo.get(),
            'productType': prdctType.get(),
            'productName': prdctName.get(),
            'complaintDescription': complaintDetails.get(),
            'allocatedTechnician': selectedTechnician.get(),
            'complaintDate': cal.get_date(),
            'status': 'open'
            })

        # c.execute("DROP TABLE complaints")
        # commit changes
        conn.commit()

        # close connection
        conn.close()

        print("added to db")

        nameEntry.delete(0,END); 
        mobEntry.delete(0, END); addrEntry.delete(0,END); invoiceEntry.delete(0,END); cityEntry.delete(0,END); 
        emailEntry.delete(0,END); pinEntry.delete(0,END); prdctNoEntry.delete(0,END); prdctNameEntry.delete(0,END); 
        complaintDetailsEntry.delete(0,END)


    # def dropTable():
    #     # create a database or connect to one
    #     conn = sqlite3.connect('Complaint_box.db')

    #     # create cursor
    #     c = conn.cursor()

    #     c.execute("DROP TABLE complaints")
    #     # commit changes
    #     conn.commit()

    #     # close connection
    #     conn.close()

        


    # Customer Details entry box
    nameEntry = tkinter.Entry(master, textvariable=cstmrName)
    nameEntry.grid(row=2, column=2)

    mobEntry = tkinter.Entry(master, textvariable=cstmrNmbr)
    mobEntry.grid(row=2, column=5)

    addrEntry = tkinter.Entry(master, textvariable=cstmrAdrs)
    addrEntry.grid(row=3, column=2)

    invoiceEntry = tkinter.Entry(master, textvariable=invoiceNo)
    invoiceEntry.grid(row=3, column=5)

    cityEntry = tkinter.Entry(master, textvariable=cstmrCity)
    cityEntry.grid(row=4, column=2)

    emailEntry = tkinter.Entry(master, textvariable=cstmrEmail)
    emailEntry.grid(row=5, column=2)

    pinEntry = tkinter.Entry(master, textvariable=cstmrPincode)
    pinEntry.grid(row=4, column=5)

    cal= DateEntry(master,selectmode='day')
    cal.grid(row=7,column=5)

    # Complaint detail entry box
    prdctNoEntry = tkinter.Entry(master, textvariable=prdctNo)
    prdctNoEntry.grid(row=7, column=2)
    # prdctNameEntry = tkinter.Entry(master, textvariable=prdctName).grid(row=7, column=2)

    prdctType.set("                               ")
    productDrop = tkinter.OptionMenu(master, prdctType, *serviceOptions)
    productDrop.grid(row=8, column=2)

    prdctNameEntry = tkinter.Entry(master, textvariable=prdctName)
    prdctNameEntry.grid(row=8, column=5)

    complaintDetailsEntry = tkinter.Entry(master, textvariable=complaintDetails)
    complaintDetailsEntry.grid(row=9, column=2)

    # allocateTechnicianEntry = tkinter.Entry(master, textvariable=allocateTechnician).grid(row=9, column=2)
    # Header in navbar
    def donothing():
        x = 0


    selectionButton = tkinter.Button(master, text="select tech support", command=selectTechSupport)
    selectionButton.grid(row=9, column=5, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    complaintAddBtn = tkinter.Button(master, text="Add Complaint", command=addComplaint)
    complaintAddBtn.grid(row=12, column=3, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S,pady=15)





    menubar = Menu(master)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Add Technician", command=addTechnician)
    filemenu.add_command(label="All Technician", command=viewAllTechnician)
    filemenu.add_command(label="All Complaints", command=viewAllComplaits)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=master.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    master.config(menu=menubar)

    master.mainloop()



# addComplaint()