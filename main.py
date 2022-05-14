from tkinter import *
import tkinter
from PIL import ImageTk, Image

root = Tk()
root.title("Complaint Optimization Window")
root.geometry("800x450")

root.iconbitmap('icon.ico')
#QWERTYUIOPASDFGHJKLZXCVBNM,./
my_img = ImageTk.PhotoImage(Image.open("Image.jpeg"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0)
my_label.place(relx=0.5, rely=0.5,anchor=CENTER)

# Set the geometry of the window

# Create a frame widget
# frame = Frame(root, width=300, height=300)
# frame.grid(row=2, column=0)


# Create a label widget
label = Label(root, text="COMPLAINT OPTIMIZATION WINDOW", font='Arial 17 bold')
label.place(relx=0.5, rely=0.1, anchor=CENTER)
lable1 = Label(root, text="Created By:\nMANUBHAV RASTOGI (20BCS5778) / MUKUL KUMAR (20BCS5769) / ADARSH KUMAR GAUD (20BCS5794)", font='Arial 10 italic')
lable1.place(relx=0.5, rely=0.9, anchor=CENTER)


root.mainloop()
