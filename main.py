from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

from Complaint_Optimization_Window import *


root = Tk()
root.title("Complaint Optimization Window")
root.geometry("800x500")
root.configure(bg='white')

def donothing():
    x = 0
    
def newHnadler():
    root.destroy()
    addComplaint()

menubar=Menu(root)
menubar = Menu(menubar, tearoff=0)
menubar.add_command(label="New", command=newHnadler)
menubar.add_separator()
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

# root.iconbitmap('icon.ico')
#my_img = ImageTk.PhotoImage(Image.open("Image.jpeg"))
#my_label = Label(image=my_img)
#my_label.grid(row=0, column=0)
#my_label.place(relx=0.5, rely=0.5,anchor=CENTER)

frameCnt = 40
frames = [PhotoImage(file='card-03-customersupport(2).gif', format='gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label= Label(root)
label.pack(padx=20,pady=20)
root.after(0, update, 0)

# label2 = Label(root, text="Single Place For Managing All Your Complaints",fg="#6400F5", font='helvetica 22 bold')
# label2.place(relx=0.5, rely=0.8, anchor=CENTER)
# label2.config(bg="white")


label2 = Label(root, text="Single Place For Managing All Your Complaints", font='helvetica 22 bold')
# label2.place(relx=0.5, rely=0.8, anchor=CENTER)
label2.pack(padx=15,pady=15)


label1 = Label(root, text="                                                                         Created By:\nMANUBHAV RASTOGI (20BCS5778) / MUKUL KUMAR (20BCS5769) / ADARSH KUMAR GAUD (20BCS5794)", font='Arial 10 italic')
label1.pack(padx=10, pady=10, anchor=CENTER )


root.mainloop()


# from tkinter import *
# import tkinter as tk
# from PIL import ImageTk, Image


# root = Tk()
# root.title("Complaint Optimization Window")
# root.geometry("800x450")
# root.configure(bg='white')

# def donothing():
#     x = 0

# menubar=Menu(root)
# menubar = Menu(menubar, tearoff=0)
# menubar.add_command(label="New", command=donothing)
# menubar.add_separator()
# menubar.add_command(label="Exit", command=root.quit)
# root.config(menu=menubar)

# root.iconbitmap('icon.ico')
# #my_img = ImageTk.PhotoImage(Image.open("Image.jpeg"))
# #my_label = Label(image=my_img)
# #my_label.grid(row=0, column=0)
# #my_label.place(relx=0.5, rely=0.5,anchor=CENTER)
# label3 = Label(root, text="                  ", font='Helvetica 15 bold')
# label3.place(relx=0.5, rely=0.1, anchor=CENTER)

# frameCnt = 40
# frames = [PhotoImage(file='card-03-customersupport(2).gif', format='gif -index %i' %(i)) for i in range(frameCnt)]


# label2 = Label(root, text="Single Place For Managing All Your Complaints",fg="#6400F5", font='helvetica 22 bold')
# label2.place(relx=0.5, rely=0.8, anchor=CENTER)
# label2.config(bg="white")
# label1 = Label(root, text="Created By:\nMANUBHAV RASTOGI (20BCS5778) / MUKUL KUMAR (20BCS5769) / ADARSH KUMAR GAUD (20BCS5794)",fg="#764869", font='Arial 10 italic underline')
# label1.place(relx=0.5, rely=0.9, anchor=CENTER)
# label1.config(bg="white")

# def update(ind):

#     frame = frames[ind]
#     ind += 1
#     if ind == frameCnt:
#         ind = 0
#     label.configure(image=frame)
#     root.after(100, update, ind)
# label= Label(root)
# label.pack(padx=20,pady=20)
# root.after(0, update, 0)
# root.mainloop()