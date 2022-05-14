def mapCreator(technicianAddress, customerAddress):

    from PIL import Image, ImageTk
    import tkinter
    import os
    from tkintermapview import TkinterMapView

    # create tkinter window
    # root = tkinter.Tk()

    root = tkinter.Toplevel()


    root.title("map_view_simple_example.py")

    # root.geometry("1100x800")


    root_tk = tkinter.LabelFrame(root, padx= 20, pady=20,highlightthickness= 0)
    root_tk.grid(row = 0)

    # create map widget
    map_widget = TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
    map_widget.pack(fill="both", expand=True)


    # technicianAddress = "Chandigarh airport, chandigarh, india"
    # customerAddress = "Chandigarh junction railway station, chandigarh, India"


    map_widget.set_address(technicianAddress)



    technician_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "technician.png")).resize((300, 200)))

    customer_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "customer.png")).resize((300, 200)))

    # airport_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "airport.jpg")).resize((300, 200)))

    # # create marker through .set_address() with image, which is visible at zoom levels 14 to infinity
    technician_marker = map_widget.set_address(technicianAddress, marker=True, image=technician_image, image_zoom_visibility=(14, float("inf")))

    customer_mrker = map_widget.set_address(customerAddress, marker=True, image=customer_image,marker_color_circle="black",marker_color_outside="gray40", image_zoom_visibility=(14, float("inf")))

    addressFrame = tkinter.LabelFrame(root)
    addressFrame.grid(row = 1)

    customerAddressTag = tkinter.Label(addressFrame, text="Customer Address: ", font='Helvetica 16 bold')
    customerAddressTag.grid(row=0,column= 0)

    customerAddressLabel = tkinter.Label(addressFrame, text=customerAddress, justify="left")
    customerAddressLabel.grid(row=0,column= 1)

    technicianAddressTag = tkinter.Label(addressFrame, text="Technician Address: ", font='Helvetica 16 bold')
    technicianAddressTag.grid(row=1,column= 0)

    technicianAddressLabel = tkinter.Label(addressFrame, text=technicianAddress, justify="left")
    technicianAddressLabel.grid(row=1,column= 1)

    root.mainloop()



technicianAddress = "Chandigarh airport, chandigarh, india"
customerAddress = "elante mall, chandigarh, india"



# mapCreator(technicianAddress, customerAddress)

