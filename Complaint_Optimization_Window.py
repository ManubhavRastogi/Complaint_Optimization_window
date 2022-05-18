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
    # master.geometry("845x300")

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
        defEmpIdLabel = tkinter.Label(selectionWindow, text="Employee Id",font='ariel 9 bold')
        defEmpIdLabel.grid(row=0, column= 0)

        defNameLabel = tkinter.Label(selectionWindow, text="Emp. Name", font='ariel 9 bold')
        defNameLabel.grid(row=0, column= 2)

        defCityLabel = tkinter.Label(selectionWindow, text="Emp. City",font='ariel 9 bold')
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
            empIdLabel=tkinter.Label(selectionWindow, text=techId)
            empIdLabel.grid(row=rowVar, column=0)

            nameLabel = tkinter.Label(selectionWindow, text=name)
            nameLabel.grid(row=rowVar, column=2)


            cityLabel = tkinter.Label(selectionWindow, text=city)
            cityLabel.grid(row=rowVar, column=4)

            rB = tkinter.Radiobutton(selectionWindow, variable=selectedTechnician,
                value=techId, command=rbOnClick)
            rB.grid(row=rowVar, column=6)

            rowVar = rowVar + 1


        selectionWindow.mainloop()


    def addTechnician():

        window = Toplevel()
        window.config(bg='white')
        

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

            message = """

            <p1> Congratulations! This email is to formally offer you the job of Technician for Royal Tech Support. 
            We strongly believe that your skills and expertise will help our company to reach new heights and hoping to make our costumers a happy and satisfied your work. 
            </p1><br>
            <p2>As we discussed with you previously, you must start on 01-06-2022, and the salary stands at ₹4,00,000 per annum. 
                We have the policy to disburse the salary by 10th of every month, and it will be credited directly to your bank account.
            </p2>

            """

            mailer(email.get(),subject, message)
            # mailsender(reciever= email.get(), subject=subject, message= message)


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

        label = tkinter.Label(window, text="Complaint Optimization Window", background="white",font='ariel 15 bold underline')
        label.grid(row=0, column=1)

        l1 = tkinter.Label(window, text="Enter Employee Id:", background="white", font='ariel 9 bold').grid(row=1,sticky=tkinter.W)
        l2 = tkinter.Label(window, text="Enter Full Name:", background="white", font='ariel 9 bold').grid(row=2,sticky=tkinter.W)
        l3 = tkinter.Label(window, text="Enter Email Adddress:", background="white", font='ariel 9 bold').grid(row=3,sticky=tkinter.W)
        l4 = tkinter.Label(window, text="Enter Mobile Number:", background="white", font='ariel 9 bold').grid(row=4,sticky=tkinter.W)
        l5 = tkinter.Label(window, text="Select Tech Expertise:", background="white", font='ariel 9 bold').grid(row=5,sticky=tkinter.W)
        l6 = tkinter.Label(window, text="Enter city:", background="white", font='ariel 9 bold').grid(row=6,sticky=tkinter.W)
        l7 = tkinter.Label(window, text="Enter district:", background="white", font='ariel 9 bold').grid(row=7, sticky=tkinter.W)
        l8 = tkinter.Label(window, text="Enter address:", background="white", font='ariel 9 bold').grid(row=8,sticky=tkinter.W)
        l9 = tkinter.Label(window, text="Enter state:", background="white", font='ariel 9 bold').grid(row=9,sticky=tkinter.W)
        l10 = tkinter.Label(window, text="Enter pincode:", background="white", font='ariel 9 bold').grid(row=10,sticky=tkinter.W)





        t1 = tkinter.Entry(window, textvariable=empId)
        t1.grid(row=1, column=3)
        t2 = tkinter.Entry(window, textvariable=name)
        t2.grid(row=2, column=3)
        t3 = tkinter.Entry(window, textvariable=email)
        t3.grid(row=3, column=3)
        t4 = tkinter.Entry(window, textvariable=mobile)
        t4.grid(row=4, column=3)
        #t5 = tkinter.Entry(window, textvariable=techExpertise).grid(row=4,column=1)

        techExpertise.set("                               ")
        drop = tkinter.OptionMenu(window, techExpertise, *serviceOptions)
        drop.grid(row=5, column=3)

        t6 = tkinter.Entry(window, textvariable=city)
        t6.grid(row=6, column=3)
        t7 = tkinter.Entry(window, textvariable=district)
        t7.grid(row=7, column=3)
        t8 = tkinter.Entry(window, textvariable=address)
        t8.grid(row=8, column=3)
        t9 = tkinter.Entry(window, textvariable=state)
        t9.grid(row=9, column=3)
        t10 = tkinter.Entry(window, textvariable=pincode)
        t10.grid(row=10, column=3)

        # Button for adding employee
        b = tkinter.Button(window, text="Add Employee", command=addEmployeeHandler)
        b.grid(row=20, column=1, columnspan=1, rowspan=2, sticky=tkinter.W +
            tkinter.E + tkinter.N + tkinter.S, padx=5, pady=5)



        window.mainloop()



        


    # lable = Lable(master,text = "Complaint Optimization Window")
    # label.pack(side = TOP, pady = 10)

    label = tkinter.Label(text="Complaint Optimization Window", font='ariel 15 bold underline')
    label.grid(row=0, column = 3, sticky= W,pady=2)


    #       lable for selecting employee codes

    label = tkinter.Label(text="Costumer Details", font=' ariel 12 bold underline')
    label.grid(row=1, column=3)
    label = tkinter.Label(text="Complaint Detail From", font=' ariel 12 bold underline')
    label.grid(row=6, column=3)
    l1 = tkinter.Label(master, text="Name :").grid(row=2, sticky=tkinter.W)
    l2 = tkinter.Label(master, text="Phone No :").grid(row=2,column=4, sticky=tkinter.W)
    l3 = tkinter.Label(master, text="Costumer Adddress :").grid(row=3, sticky=tkinter.W)
    l4 = tkinter.Label(master, text="City :").grid(row=4,column=0, sticky=tkinter.W)
    emailLabel = tkinter.Label(master, text="Email :").grid(row=5,column=0, sticky=tkinter.W)
    l5 = tkinter.Label(master, text="Pincode :").grid(row=4,column=4, sticky=tkinter.W)
    l6 = tkinter.Label(master, text="Invoice No. :").grid(row=3,column=4, sticky=tkinter.W)
    l7 = tkinter.Label(master, text="Product Serial No.:").grid(row=7, sticky=tkinter.W)
    l8 = tkinter.Label(master, text="Product Type :").grid(row=8, sticky=tkinter.W)
    l8 = tkinter.Label(master, text="Date :").grid(row=7,column=4, sticky=tkinter.W)
    l8 = tkinter.Label(master, text="Product Name :").grid(row=8,column=4, sticky=tkinter.W)
    l9 = tkinter.Label(master, text="Complaint Details :").grid(row=9, sticky=tkinter.W)
    l10 = tkinter.Label(master, text="Allocate Technician :").grid(row=9,column=4, sticky=tkinter.W)


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
        def mailSender():
            customerSubject = """Your complaint has been added"""

            customerMessage = """
                        
                <p1> 
                    Your complaint has been registered successfully.
                </p1><br>
                <p2>
                    We have assigned a technician for your complaints, he will soon contact on behalf of our company.
                </p2>

            """
            mailer(cstmrEmail.get(), customerSubject, customerMessage)


            conn = sqlite3.connect('Complaint_box.db')              # create a database or connect to one
            c = conn.cursor()                                       # create cursor
            
                        # Querying in database
            query = "SELECT employeeId, email FROM employees WHERE employeeId =  '" + selectedTechnician.get() + "'"
            c.execute(query)
            emplyoeeDetail = c.fetchall()

            for(employeeId,email) in emplyoeeDetail:
                technicianEmail = email


            print(technicianEmail)




            technicianSubject = """New Complaint added to you list"""
            technicianMessage = """
                        
                <p1> 
                    A new task has been assigned to you.
                </p1><br>
                <p2>
                    You can login to your account and check for more details about your customer and complaint.
                </p2>

            """

            mailer(technicianEmail, technicianSubject, technicianMessage)



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

        mailSender()

        print("added to db")

        nameEntry.delete(0,END); 
        mobEntry.delete(0, END); addrEntry.delete(0,END); invoiceEntry.delete(0,END); cityEntry.delete(0,END); 
        emailEntry.delete(0,END); pinEntry.delete(0,END); prdctNoEntry.delete(0,END); prdctNameEntry.delete(0,END); 
        complaintDetailsEntry.delete(0,END)



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

    prdctType.set("                               ")
    productDrop = tkinter.OptionMenu(master, prdctType, *serviceOptions)
    productDrop.grid(row=8, column=2)

    prdctNameEntry = tkinter.Entry(master, textvariable=prdctName)
    prdctNameEntry.grid(row=8, column=5)

    complaintDetailsEntry = tkinter.Entry(master, textvariable=complaintDetails)
    complaintDetailsEntry.grid(row=9, column=2)


    selectionButton = tkinter.Button(master, text="Select Technician",font='ariel 8 bold', command=selectTechSupport)
    selectionButton.grid(row=9, column=5, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    complaintAddBtn = tkinter.Button(master, text="Add Complaint", fg="white", background="#262626", font='ariel 8 bold', command=addComplaint)
    complaintAddBtn.grid(row=12, column=3, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S,pady=15)


    # Header in navbar
    def donothing():
        x = 0


    menubar = Menu(master)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add Technician", command=addTechnician)
    filemenu.add_command(label="All Technician", command=viewAllTechnician)
    filemenu.add_command(label="All Complaints", command=viewAllComplaits)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=master.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    master.config(menu=menubar)

    master.mainloop()



# addComplaint()