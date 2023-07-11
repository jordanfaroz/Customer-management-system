import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

class Customer:
    def __init__(self, source, destination, source_location, destination_location, call_duration, roaming, call_charge):
        self.source = source
        self.destination = destination
        self.source_location = source_location
        self.destination_location = destination_location
        self.call_duration = call_duration
        self.roaming = roaming
        self.call_charge = call_charge

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Management System by Jordan Faroz")
        self.geometry("500x500")

        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["project"]
        self.collection = db["customer"]

        # Set background color
        self.configure(background='cyan')

        tk.Label(self, text="Source", foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=0, column=0, pady=10, padx=10)

        self.source1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.source1_entry.place(x=650, y=10)

        # Add id destination and entry
        tk.Label(self, text="Destination",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=1, column=0)

        self.destination1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.destination1_entry.place(x=650, y=50)

        # Add source location label and entry
        tk.Label(self, text="Source Location",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=2, column=0)
        self.sourceloc1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.sourceloc1_entry.place(x=650, y=95)

        # Add name destination_location and entry
        tk.Label(self, text="Destination Location",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=3, column=0)
        self.destinationloc1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.destinationloc1_entry.place(x=650, y=135)

        # Add call duration and entry
        tk.Label(self, text="Call Duration",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=4, column=0)
        self.calldur1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.calldur1_entry.place(x=650, y=170)

        # Add name roaming and entry
        tk.Label(self, text="Roaming",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=5, column=0)
        self.roaming1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.roaming1_entry.place(x=650, y=210)

        # Add name call_charges and entry
        tk.Label(self, text="Call Charges",foreground="magenta", background="cyan", font=("times new roman", 20, "bold italic")).grid(row=6, column=0)
        self.callcharge1_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.callcharge1_entry.place(x=650, y=250)

        # Add submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit, bg="green", fg="white",
                                  font=("Helvetica", 14))
        submit_button.place(x=475, y=600, width=100, height=50)

        # Add update button
        update_button = tk.Button(self, text="Update", command=self.update, bg="blue", fg="white",
                                  font=("Helvetica", 14))
        update_button.place(x=275, y=600, width=100, height=50)

        # Add delete button
        delete_button = tk.Button(self, text="Delete", command=self.delete_employee, bg="red", fg="white",
                                  font=("Helvetica", 14))
        delete_button.place(x=675, y=600, width=100, height=50)

        clear_button = tk.Button(self, text="Clear", command=self.clear, bg="orange", fg="white",
                                 font=("Helvetica", 14))
        clear_button.place(x=875, y=600, width=100, height=50)

        # Add search label and entry

        self.search_entry = tk.Entry(self, font=("Helvetica", 14), borderwidth=2, relief="solid")
        self.search_entry.place(x=650, y=290)

        # Add search button
        search_button = tk.Button(self, text="Search", command=self.search, bg="purple", fg="white",
                                  font=("Helvetica", 14))
        search_button.place(x=75, y=600, width=100, height=50)

        # Add tree view to display customers
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = (
            "source", "destination", "source_location", "destination_location", "call_duration", "roaming",
            "call_charge")
        self.tree.heading("source", text="Source", anchor=tk.CENTER)
        self.tree.heading("destination", text="Destination", anchor=tk.CENTER)
        self.tree.heading("source_location", text="Source Location", anchor=tk.CENTER)
        self.tree.heading("destination_location", text="Destination Location", anchor=tk.CENTER)
        self.tree.heading("call_duration", text="Call Duration", anchor=tk.CENTER)
        self.tree.heading("roaming", text="Roaming", anchor=tk.CENTER)
        self.tree.heading("call_charge", text="Call Charge", anchor=tk.CENTER)

        # Set treeview style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Helvetica", 12), background="#f9f9f9", fieldbackground="#f9f9f9",
                        foreground="black")
        style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), background="#c3d0f0",
                        foreground="black", relief="raised", anchor=tk.CENTER)
        style.configure("Treeview.Row", background="#f0f0ff")
        style.configure("Treeview.Tree", background="#f0f0ff")

        # Set treeview columns width
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("source", width=150, minwidth=100, stretch=tk.NO)
        self.tree.column("destination", width=150, minwidth=100, stretch=tk.NO)
        self.tree.column("source_location", width=200, minwidth=150, stretch=tk.NO)
        self.tree.column("destination_location", width=200, minwidth=150, stretch=tk.NO)
        self.tree.column("call_duration", width=150, minwidth=100, stretch=tk.NO)
        self.tree.column("roaming", width=150, minwidth=100, stretch=tk.NO)
        self.tree.column("call_charge", width=150, minwidth=100, stretch=tk.NO)
        self.tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)



        # Add treeview tags for alternate row colors
        self.tree.tag_configure("evenrow", background="#f0f0ff")
        self.tree.tag_configure("oddrow", background="#f0f0e0")

        # Create a custom style for the scrollbar
        style = ttk.Style()
        style.theme_use("clam")  # choose a theme

        # Modify the scrollbar colors and thickness
        style.configure("Vertical.TScrollbar",
                        gripcount=0,
                        background="gray",
                        darkcolor="gray",
                        lightcolor="gray",
                        troughcolor="white",
                        bordercolor="white",
                        arrowcolor="white",
                        arrowpadding=4,
                        width=12)

        # Add scrollbar to tree view
        self.tree_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview,
                                            style="Vertical.TScrollbar")
        self.tree_scrollbar.place(x=1165, y=287, height=239)
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)

        # Create form to update employee data
        self.source_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.source_location_var = tk.StringVar()
        self.destination_location_var = tk.StringVar()
        self.call_duration_var = tk.StringVar()
        self.roaming_var = tk.StringVar()
        self.call_charge_var = tk.StringVar()











        # Load employees from MongoDB
        for customer in self.collection.find():
            self.tree.insert("", "end", values= (customer["source"],customer["destination"], customer["source_location"], customer["destination_location"], customer["call_duration"], customer["roaming"], customer["call_charge"]))

        self.tree.bind("<Double-1>", self.show_selected_record)
        '''<< TreeviewSelect >>'''

    def load_customers(self):
        for customer in self.collection.find():
            values = (customer["source"], customer["destination"], customer["source_location"], customer["destination_location"], customer["call_duration"], customer["roaming"], customer["call_charge"])
            self.tree.insert("", "end", values=values)

    def show_selected_record(self,event):
        self.clear1()
        print("im in show select")
        for selection in self.tree.selection():
            '''item = self.tree.selection()[0]'''
            values = self.tree.item(selection)
            print(values)

            i1,i2,i3,i4,i5,i6,i7=values["values"][0:7]
        #print(i1)

            self.source1_entry.insert(0,i1)
            self.destination1_entry.insert(0,i2)
            self.sourceloc1_entry.insert(0,i3)
            self.destinationloc1_entry.insert(0,i4)
            self.calldur1_entry.insert(0,i5)
            self.roaming1_entry.insert(0,i6)
            self.callcharge1_entry.insert(0,i7)







    def clear1(self):
        self.source1_entry.delete(0,tk.END)
        self.destination1_entry.delete(0, tk.END)
        self.sourceloc1_entry.delete(0, tk.END)
        self.destinationloc1_entry.delete(0, tk.END)
        self.calldur1_entry.delete(0, tk.END)
        self.roaming1_entry.delete(0, tk.END)
        self.callcharge1_entry.delete(0, tk.END)



    def submit(self):
        # Get values from entries
        source = self.source1_entry.get()
        destination = self.destination1_entry.get()
        source_location = self.sourceloc1_entry.get()
        destination_location = self.destinationloc1_entry.get()
        call_duration = self.calldur1_entry.get()
        roaming = self.roaming1_entry.get()
        call_charge = self.callcharge1_entry.get()

        # Create a new customer object with the input data
        new_customer = Customer(source, destination, source_location, destination_location, call_duration, roaming,
                                call_charge)

        # Insert the new customer into the MongoDB collection
        self.collection.insert_one({
            "source": new_customer.source,
            "destination": new_customer.destination,
            "source_location": new_customer.source_location,
            "destination_location": new_customer.destination_location,
            "call_duration": new_customer.call_duration,
            "roaming": new_customer.roaming,
            "call_charge": new_customer.call_charge
        })

        # Clear the entries and reload the treeview
        self.source1_entry.delete(0, tk.END)
        self.destination1_entry.delete(0, tk.END)
        self.sourceloc1_entry.delete(0, tk.END)
        self.destinationloc1_entry.delete(0, tk.END)
        self.calldur1_entry.delete(0, tk.END)
        self.roaming1_entry.delete(0, tk.END)
        self.callcharge1_entry.delete(0, tk.END)

        self.tree.delete(*self.tree.get_children())
        self.load_customers()

    def update(self):
        # Retrieve the selected record from the Treeview
        selected_record = self.tree.focus()
        record_values = self.tree.item(selected_record)["values"]

        # Retrieve the updated data from the Entry widgets
        new_values = (
            self.source1_entry.get(),
            self.destination1_entry.get(),
            self.sourceloc1_entry.get(),
            self.destinationloc1_entry.get(),
            self.calldur1_entry.get(),
            self.roaming1_entry.get(),
            self.callcharge1_entry.get()
        )

        # Update the record in the MongoDB collection
        self.collection.update_one(
            {"source": record_values[0]},
            {"$set": {
                "source": new_values[0],
                "destination": new_values[1],
                "source_location": new_values[2],
                "destination_location": new_values[3],
                "call_duration": new_values[4],
                "roaming": new_values[5],
                "call_charge": new_values[6]
            }}
        )

        # Update the record in the Treeview
        for i in range(7):
            self.tree.set(selected_record, column=i, value=new_values[i])
    def delete_employee(self):
        # get the currently selected customer's ID
        selection = self.tree.selection()
        if not selection:
            return
        customer_id = self.tree.item(selection[0])["values"][0]

        # delete the customer from the database
        self.collection.delete_one({"_id": customer_id})

        # remove the customer from the tree view display
        self.tree.delete(selection[0])

    def clear(self):
        self.source1_entry.delete(0, tk.END)
        self.destination1_entry.delete(0, tk.END)
        self.sourceloc1_entry.delete(0, tk.END)
        self.destinationloc1_entry.delete(0, tk.END)
        self.calldur1_entry.delete(0, tk.END)
        self.roaming1_entry.delete(0, tk.END)
        self.callcharge1_entry.delete(0, tk.END)

    # Define search_customer function
    def search(self):
        source_number = self.source1_entry.get()
        result = self.collection.find_one({"source": source_number})
        if result:
            self.tree.delete(*self.tree.get_children())
            self.tree.insert("", tk.END, values=(
                result["source"], result["destination"], result["source_location"], result["destination_location"],
                result["call_duration"], result["roaming"], result["call_charge"]))
        else:
            messagebox.showerror("Error", "Customer not found!")


if __name__ == "__main__":
    app = Application()
    app.mainloop()