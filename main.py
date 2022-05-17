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



tagLabel = tk.Label(root, text="Single Place For Managing All Your Complaints", font='helvetica 22 bold')
tagLabel.pack(padx=15,pady=15,)
tagLabel.config(background= "white", fg= "#6400F5")


devLabel = tk.Label(root, text="Created By:\nMANUBHAV RASTOGI (20BCS5778) / MUKUL KUMAR (20BCS5769) / ADARSH KUMAR GAUD (20BCS5794)", font='Arial 10 italic')
devLabel.pack(padx=10, pady=10, anchor=CENTER )
devLabel.config(background= "white",fg="#764869")



root.mainloop()


