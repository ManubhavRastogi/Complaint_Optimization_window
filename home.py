import tkinter

from tkinter import *


home = Tk()

home.title("Home Page")

# create a toplevel menu  
menubar = Menu(home)  
menubar.add_command(label="Hello!")  
menubar.add_command(label="Quit!")  
  
# display the menu  
home.config(menu=menubar)  

home.mainloop()