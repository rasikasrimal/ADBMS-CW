from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

from tkinter import ttk

import exit_operations as exit_ops
import export_operations as export_ops
import delete_operations as delete_ops

import customer
import product
import order
import orderdetail
import employee
import sale
import promotion
import promotionusage
import inventory
import supplier
import transaction
import storelocation
import visits
import customers_

import add_student

import add_customer_top




count = 0
text = ''

def show_customer():
    query='SELECT * FROM customers'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    customer_table.delete(*customer_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        customer_table.insert('',END,values=data_list)


def add_customer():
    def add_customer_data():
        if (
            idEntry.get() == '' or 
            firstnameEntry.get() == '' or 
            lastnameEntry.get() == '' or 
            emailEntry.get() == '' or 
            phoneEntry.get() == '' or 
            addressEntry.get() == '' # or 
            # registrationdateEntry.get() == '' or 
            # loyaltypointsEntry.get() == ''
        ):
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            query = '''
            INSERT INTO customers (
                customer_id, first_name, last_name, 
                Email, Phone, Address
            ) VALUES (%s, %s, %s, %s, %s, %s);
            '''
            values = (
                idEntry.get(),
                firstnameEntry.get(),
                lastnameEntry.get(),
                emailEntry.get(),
                phoneEntry.get(),
                addressEntry.get()
            )
            mycursor.execute(query, values)

            # Insert trigger for customer_details
            query = '''
            INSERT INTO customer_details (customer_id, registration_date, loyalty_points)
            VALUES (%s, NOW(), 0);
            '''
            mycursor.execute(query, (idEntry.get(),))  # Pass the customer_id here

            con.commit()
            result = messagebox.askyesno('Confirm', 'Do you want to clear the form?')
            if result:
                idEntry.delete(0, END)
                firstnameEntry.delete(0, END)
                lastnameEntry.delete(0, END)
                emailEntry.delete(0, END)
                phoneEntry.delete(0, END)
                addressEntry.delete(0, END)
                registrationdateEntry.delete(0, END)
                loyaltypointsEntry.delete(0, END)



    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False, False)

    idlable = Label(add_window, text='customerID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    firstnamelable = Label(add_window, text='first Name', font=('Helvetica', 15, 'bold'))
    firstnamelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    firstnameEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    firstnameEntry.grid(row=1, column=1, padx=10, pady=10)

    lastnamelable = Label(add_window, text='last Name', font=('Helvetica', 15, 'bold'))
    lastnamelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    lastnameEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    lastnameEntry.grid(row=2, column=1, padx=10, pady=10)

    emaillable = Label(add_window, text='Email', font=('Helvetica', 15, 'bold'))
    emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    emailEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    phonelable = Label(add_window, text='phone', font=('Helvetica', 15, 'bold'))
    phonelable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    phoneEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    phoneEntry.grid(row=4, column=1, padx=10, pady=10)

    addresslable = Label(add_window, text='Address', font=('Helvetica', 15, 'bold'))
    addresslable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    addressEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    addressEntry.grid(row=5, column=1, padx=10, pady=10)


    add_customer_button = ttk.Button(add_window, text="Add Customer", command=add_customer_data)
    add_customer_button.grid(row=8, columnspan =2, pady=10)

#################################################################################################
#################################################################################################
from tkinter import messagebox, ttk, END

def add_product():
    def add_product_data():
        if (
            idEntry.get() == '' or 
            nameEntry.get() == '' or 
            categoryEntry.get() == '' or 
            priceEntry.get() == '' or 
            quantityEntry.get() == '' or 
            profit_per_unitEntry.get() == '' or 
            supplier_idEntry.get() == ''
        ):
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            try:
                # Check if the selected supplier_id exists in the suppliers table
                supplier_id = int(supplier_idEntry.get())
                query = "SELECT supplier_id FROM suppliers WHERE supplier_id = %s;"
                mycursor.execute(query, (supplier_id,))
                if not mycursor.fetchone():
                    messagebox.showerror('Error', 'Invalid supplier_id', parent=add_window)
                    return

                # Insert into products table
                query = '''
                INSERT INTO products (
                    product_id, name, category, 
                    price, stock_quantity, profit_per_unit, supplier_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s);
                '''
                values = (
                    idEntry.get(),
                    nameEntry.get(),
                    categoryEntry.get(),
                    priceEntry.get(),
                    quantityEntry.get(),
                    profit_per_unitEntry.get(),
                    supplier_id
                )
                mycursor.execute(query, values)
                con.commit()

                result = messagebox.askyesno('Confirm', 'Do you want to clear the form?')
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    categoryEntry.delete(0, END)
                    priceEntry.delete(0, END)
                    quantityEntry.delete(0, END)
                    profit_per_unitEntry.delete(0, END)
                    supplier_idEntry.set('')  # Clear the supplier_id dropdown

            except ValueError:
                messagebox.showerror('Error', 'Invalid input for supplier_id', parent=add_window)


    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False, False)

    idlable = Label(add_window, text='Product ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(add_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    categorylable = Label(add_window, text='Category', font=('Helvetica', 15, 'bold'))
    categorylable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    categoryEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    categoryEntry.grid(row=2, column=1, padx=10, pady=10)

    pricelable = Label(add_window, text='Price', font=('Helvetica', 15, 'bold'))
    pricelable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    priceEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    priceEntry.grid(row=3, column=1, padx=10, pady=10)

    quantitylable = Label(add_window, text='Quantity', font=('Helvetica', 15, 'bold'))
    quantitylable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    quantityEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    quantityEntry.grid(row=4, column=1, padx=10, pady=10)

    profit_per_unitlable = Label(add_window, text='Profit per Unit', font=('Helvetica', 15, 'bold'))
    profit_per_unitlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    profit_per_unitEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    profit_per_unitEntry.grid(row=5, column=1, padx=10, pady=10)

    supplier_idlable = Label(add_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    supplier_idlable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    supplier_idEntry = ttk.Combobox(add_window, font=('Helvetica', 15, 'bold'), state='readonly', width=22)
    supplier_idEntry.grid(row=6, column=1, padx=10, pady=10)

    # Populate the supplier_id dropdown
    mycursor.execute("SELECT supplier_id FROM suppliers;")
    suppliers = mycursor.fetchall()
    supplier_ids = [str(s[0]) for s in suppliers]
    supplier_idEntry['values'] = supplier_ids

    add_button = Button(add_window, text='Add Product', font=('Helvetica', 15, 'bold'), command=add_product_data)
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

    add_window.mainloop()
#################################################################################################
import tkinter as tk
from tkinter import ttk
import pymysql

def update_customer():
    # Create a new window for updating customer details
    update_window = tk.Toplevel(root)
    update_window.title("Update Customer Details")

    # Create and place labels and entry widgets for each customer detail
    labels = ["Customer ID", "First Name", "Last Name", "Email", "Phone", "Address"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(update_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    # Function to update customer details in the database
    def save_changes():
        # Get the updated values from entry widgets
        updated_values = [entry.get() for entry in entries]

        # Update the customer details in the database
        update_query = "UPDATE customers SET first_name=%s, last_name=%s, email=%s, phone=%s, address=%s WHERE customer_id=%s"
        cursor.execute(update_query, (updated_values[1], updated_values[2], updated_values[3], updated_values[4], updated_values[5], updated_values[0]))
        db.commit()

        # Close the update window after saving changes
        update_window.destroy()

    # Create a button to save changes
    tk.Button(update_window, text="Save Changes", command=save_changes).grid(row=len(labels), column=0, columnspan=2, pady=10)

#################################################################################################

# Function to handle exit button click
def exit_program():
    root.destroy()

# Function to handle connect database button click
def connect_database():

    # Function to handle connect button click
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            # con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=PasswordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showinfo('Success', 'Connected to Database')
            return
        try:
            query = 'CREATE DATABASE IF NOT EXISTS supermarket'
            mycursor.execute(query)
            query = 'USE supermarket'
            mycursor.execute(query)
            
            query = ''' 
            CREATE TABLE IF NOT EXISTS employee (
                employee_id INT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                phone VARCHAR(15) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                salary DECIMAL(10, 2) NOT NULL,
                position_id INT,
                exp_id INT,
                hire_date DATE NOT NULL,
                FOREIGN KEY (position_id) REFERENCES positions(position_id),
                FOREIGN KEY (exp_id) REFERENCES experience(exp_id)
            );

            CREATE TABLE IF NOT EXISTS experience (
                exp_id INT PRIMARY KEY NOT NULL,
                exp_level VARCHAR(255) NOT NULL,
                exp_factor DECIMAL(10, 2) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS positions (
                position_id INT PRIMARY KEY NOT NULL,
                position_name VARCHAR(255) NOT NULL,
                base_salary DECIMAL(10, 2) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS store_locations (
                store_id INT PRIMARY KEY NOT NULL,
                store_name VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                phone VARCHAR(15) NOT NULL,
                manager VARCHAR(255),
                opening_date DATE
            ); 

            CREATE TABLE IF NOT EXISTS visits (
                visit_id INT PRIMARY KEY,
                date DATE NOT NULL,
                customer_id INT,
                store_id INT,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (store_id) REFERENCES store_locations(store_id)
            );

            CREATE TABLE IF NOT EXISTS inventory (
                inventory_id INT PRIMARY KEY,
                stock_quantity INT NOT NULL,
                restock_threshold INT NOT NULL,
                product_id INT,
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            );

            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(15) UNIQUE NOT NULL,
                address VARCHAR(255) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS customer_details (
                customer_id INT,
                registration_date DATE DEFAULT CURRENT_DATE NOT NULL,
                loyalty_points INT NOT NULL DEFAULT 0,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            );

            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT PRIMARY KEY,
                transaction_type VARCHAR(255) NOT NULL,
                date DATETIME NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                order_id INT,
                visit_id INT,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (visit_id) REFERENCES visits(visit_id)
            );

            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INT PRIMARY KEY NOT NULL,
                supplier_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(15) NOT NULL,
                address VARCHAR(255) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS sales (
                sale_id INT PRIMARY KEY,
                sale_date DATE NOT NULL,
                total_sales_amount DECIMAL(10, 2) NOT NULL,
                employee_id INT,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
            );

            CREATE TABLE IF NOT EXISTS orders (
                order_id INT PRIMARY KEY,
                order_date DATE NOT NULL,
                total_amount DECIMAL(10, 2) NOT NULL,
                payment_method VARCHAR(255) NOT NULL,
                payment_date DATE NOT NULL,
                customer_id INT,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            );

            CREATE TABLE IF NOT EXISTS orderdetails (
                orderdetail_id INT PRIMARY KEY,
                quantity INT NOT NULL,
                subtotal DECIMAL(10, 2) NOT NULL,
                order_id INT,
                product_id INT,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            );

            CREATE TABLE IF NOT EXISTS products (
                product_id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                category VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                stock_quantity INT NOT NULL,
                profit_per_unit DECIMAL(10, 2) NOT NULL,
                supplier_id INT,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
            );
            
            '''
            mycursor.execute(query)
        except:
                query = 'USE supermarket'
                mycursor.execute(query)

        # con.commit()
        # con.close()

        messagebox.showinfo('Success', 'Connected to Database')
        connectWindow.destroy()

        addcustomerButton.config(state=NORMAL)

        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)
        # addstudentButton.config(state=NORMAL)

        # searchstudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # showstudentButton.config(state=NORMAL)
        # exportDataButton.config(state=NORMAL)
        # deletestudentButton.config(state=NORMAL)

        show_customer_button.config(state=NORMAL)
        show_product_button.config(state=NORMAL)
        show_order_button.config(state=NORMAL)
        show_orderdetail_button.config(state=NORMAL)
        show_employee_button.config(state=NORMAL)
        show_sale_button.config(state=NORMAL)
        show_promotion_button.config(state=NORMAL)
        show_promotionusage_button.config(state=NORMAL)
        show_inventory_button.config(state=NORMAL)
        show_supplier_button.config(state=NORMAL)
        show_transaction_button.config(state=NORMAL)
        show_storelocation_button.config(state=NORMAL)
        show_visit_button.config(state=NORMAL)
        show_customers__button.config(state=NORMAL)

        updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
        # updatestudentButton.config(state=NORMAL)
    
#################################################################################################

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.title('Connect Database')
    connectWindow.geometry('500x300+500+200')
    connectWindow.resizable(False, False)

    hostnameLabel = Label(connectWindow, text='Hostname', font=('Helvetica', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=10, pady=10)

    hostEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'))
    hostEntry.grid(row=0, column=1, padx=10, pady=10)

    usernameLabel = Label(connectWindow, text='Username', font=('Helvetica', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)

    userEntry = Entry(connectWindow, font=('Username', 15, 'bold'))
    userEntry.grid(row=1, column=1, padx=10, pady=10)

    PasswordLabel = Label(connectWindow, text='Password', font=('Helvetica', 15, 'bold'))
    PasswordLabel.grid(row=2, column=0, padx=10, pady=10)

    PasswordEntry = Entry(connectWindow, font=('Password', 15, 'bold'))
    PasswordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton=ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, column=0, padx=10, pady=10)

# GUI Part
root = ttkthemes.ThemedTk()
root.get_themes()
# root.set_theme('radiance')
root.set_theme('breeze')

root.geometry('1174x680+0+0')
root.resizable(True, True)
root.title('DBMS For Supermarket')

# datetimeLabel = Label(root, text='Hello', font=('Helvetica', 20, 'bold'))
# datetimeLabel.place(x=5, y=5)
# clock()

# s = 'Student Management System'
# sliderLabel = Label(root, font=('Helvetica', 30, 'bold'), relief=RIDGE, width=30)
# sliderLabel.place(x=200, y=0)
# slider() # Start the animation

s = 'Supermarket DBMS'
sliderLabel = Label(root, text=s, font=('Helvetica', 30, 'bold'), width=30, fg='black', anchor='w')
sliderLabel.place(x=5, y=5)

connectButton = ttk.Button(root, text='Connect Database', width=25, command=connect_database)
connectButton.place(x=873, y=0)

exitButton = ttk.Button(root, text='Exit', width=25, command=lambda: exit_ops.handle_exit(root))
exitButton.place(x=873, y=30)

#####################################################
leftFrame = Frame(root, relief=RIDGE, border=2)
leftFrame.place(x=10, y=70, width=1100, height=534)
######################################################

# logo_image = PhotoImage(file='images/student2.png')
# logo_label = Label(leftFrame, image=logo_image)
# logo_label.grid(row=0, column=0, padx=10, pady=10)

addcustomerButton = ttk.Button(leftFrame, text='Add customer', width=25, state=NORMAL, command=add_customer)
addcustomerButton.grid(row=0, column=0, padx=10, pady=0)

addproductButton = ttk.Button(leftFrame, text='Add product', width=25, state=NORMAL, command=add_product)
addproductButton.grid(row=1, column=0, padx=10, pady=0)

addorderButton = ttk.Button(leftFrame, text='Add order', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addorderButton.grid(row=2, column=0, padx=10, pady=0)

addemployeeButton = ttk.Button(leftFrame, text='Add employee', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addemployeeButton.grid(row=3, column=0, padx=10, pady=0)

addorderdetailButton = ttk.Button(leftFrame, text='Add orderdetail', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addorderdetailButton.grid(row=4, column=0, padx=10, pady=0)

addsalesButton = ttk.Button(leftFrame, text='Add Sales', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addsalesButton.grid(row=5, column=0, padx=10, pady=0)

addpromotionButton = ttk.Button(leftFrame, text='Add promotion', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addpromotionButton.grid(row=6, column=0, padx=10, pady=0)

addpromotionusageButton = ttk.Button(leftFrame, text='Add promotionusage', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addpromotionusageButton.grid(row=7, column=0, padx=10, pady=0)

addinventoryButton = ttk.Button(leftFrame, text='Add inventory', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addinventoryButton.grid(row=8, column=0, padx=10, pady=0)

addsupplierButton = ttk.Button(leftFrame, text='Add Supplier', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addsupplierButton.grid(row=9, column=0, padx=10, pady=0)

addtransactionButton = ttk.Button(leftFrame, text='Add transaction', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addtransactionButton.grid(row=10, column=0, padx=10, pady=0)

addstorelocationButton = ttk.Button(leftFrame, text='Add Storelocation', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addstorelocationButton.grid(row=11, column=0, padx=10, pady=0)

addvisitButton = ttk.Button(leftFrame, text='Add visit', width=25, state=NORMAL, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addvisitButton.grid(row=12, column=0, padx=10, pady=0)

show_customer_button = ttk.Button(leftFrame, text='Customers', width=25, state=NORMAL, command=lambda: customer.open_customer_window(root, mycursor))
show_customer_button.grid(row=0, column=1, padx=10, pady=0)

show_product_button = ttk.Button(leftFrame, text='Products', width=25, state=NORMAL, command=lambda: product.open_product_window(root, mycursor))
show_product_button.grid(row=1, column=1, padx=10, pady=0)

show_order_button = ttk.Button(leftFrame, text='Order', width=25, state=NORMAL, command=lambda: order.open_order_window(root, mycursor))
show_order_button.grid(row=2, column=1, padx=10, pady=0)

show_employee_button = ttk.Button(leftFrame, text='Employee', width=25, state=NORMAL, command=lambda: employee.open_employee_window(root, mycursor))
show_employee_button.grid(row=3, column=1, padx=10, pady=0)

show_orderdetail_button = ttk.Button(leftFrame, text='Order Detail', width=25, state=NORMAL, command=lambda: orderdetail.open_orderdetail_window(root, mycursor))
show_orderdetail_button.grid(row=4, column=1, padx=10, pady=0)

show_sale_button = ttk.Button(leftFrame, text='Sales', width=25, state=NORMAL, command=lambda: sale.open_sale_window(root, mycursor))
show_sale_button.grid(row=5, column=1, padx=10, pady=0)

show_promotion_button = ttk.Button(leftFrame, text='Promotion', width=25, state=NORMAL, command=lambda: promotion.open_promotion_window(root, mycursor))
show_promotion_button.grid(row=6, column=1, padx=10, pady=0)

show_promotionusage_button = ttk.Button(leftFrame, text='Promotion Usage', width=25, state=NORMAL, command=lambda: promotionusage.open_promotionusage_window(root, mycursor))
show_promotionusage_button.grid(row=7, column=1, padx=10, pady=0)

show_inventory_button = ttk.Button(leftFrame, text='Inventory', width=25, state=NORMAL, command=lambda: inventory.open_inventory_window(root, mycursor))
show_inventory_button.grid(row=8, column=1, padx=10, pady=0)

show_supplier_button = ttk.Button(leftFrame, text='Supplier', width=25, state=NORMAL, command=lambda: supplier.open_supplier_window(root, mycursor))
show_supplier_button.grid(row=9, column=1, padx=10, pady=0)

show_transaction_button = ttk.Button(leftFrame, text='Transaction', width=25, state=NORMAL, command=lambda: transaction.open_transaction_window(root, mycursor))
show_transaction_button.grid(row=10, column=1, padx=10, pady=0)

show_storelocation_button = ttk.Button(leftFrame, text='Storelocation', width=25, state=NORMAL, command=lambda: storelocation.open_storelocation_window(root, mycursor))
show_storelocation_button.grid(row=11, column=1, padx=10, pady=0)

show_visit_button = ttk.Button(leftFrame, text='Visits', width=25, state=NORMAL, command=lambda: visits.open_visit_window(root, mycursor))
show_visit_button.grid(row=12, column=1, padx=10, pady=0)

#################################################################################################

updatecustomerButton = ttk.Button(leftFrame, text='Update Customer', width=25, state=NORMAL, command=update_customer)
updatecustomerButton.grid(row=0, column=2, padx=10, pady=0)

updateproductButton = ttk.Button(leftFrame, text='Update Product', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updateproductButton.grid(row=1, column=2, padx=10, pady=0)

updateorderButton = ttk.Button(leftFrame, text='Update Order', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updateorderButton.grid(row=2, column=2, padx=10, pady=0)

updateemployeeButton = ttk.Button(leftFrame, text='Update Employee', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updateemployeeButton.grid(row=3, column=2, padx=10, pady=0)

updatestudentButton = ttk.Button(leftFrame, text='Update Order Detail', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatestudentButton.grid(row=4, column=2, padx=10, pady=0)

updatesaleButton = ttk.Button(leftFrame, text='Update Sales', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatesaleButton.grid(row=5, column=2, padx=10, pady=0)

updatepromotionButton = ttk.Button(leftFrame, text='Update Promotion', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatepromotionButton.grid(row=6, column=2, padx=10, pady=0)

updatepromotionuButton = ttk.Button(leftFrame, text='Update Promotion Usage', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatepromotionuButton.grid(row=7, column=2, padx=10, pady=0)

updateinventoryButton = ttk.Button(leftFrame, text='Update Inventory', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updateinventoryButton.grid(row=8, column=2, padx=10, pady=0)

updatesupplierButton = ttk.Button(leftFrame, text='Update Supplier', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatesupplierButton.grid(row=9, column=2, padx=10, pady=0)

updatetransactionButton = ttk.Button(leftFrame, text='Update Transaction', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatetransactionButton.grid(row=10, column=2, padx=10, pady=0)

updatestorelocationButton = ttk.Button(leftFrame, text='Update Store Location', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatestorelocationButton.grid(row=11, column=2, padx=10, pady=0)

updatevisitButton = ttk.Button(leftFrame, text='Update visits', width=25, state=NORMAL, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatevisitButton.grid(row=12, column=2, padx=10, pady=0)



#################################################################################################

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sales_analysis():
    # Query for Sales Analysis
    query = """
    SELECT e.employee_id, SUM(s.total_sales_amount) AS TotalSales
    FROM Sales s
    INNER JOIN Employee e ON s.employee_id = e.employee_id
    WHERE e.position_id = (SELECT position_id FROM Positions WHERE position_name = 'manager')
    GROUP BY e.employee_id
    ORDER BY TotalSales DESC;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['EmployeeID', 'TotalSales'])

    # Visualization (example: bar plot)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='EmployeeID', y='TotalSales', data=df, palette='viridis')
    plt.title('Sales Analysis for Store Managers')
    plt.xlabel('Employee ID')
    plt.ylabel('Total Sales Amount')
    plt.show()

# Call this function when the corresponding button is clicked
salesanalysis_button = ttk.Button(leftFrame, text='Sales Analysis', width=25, state=NORMAL, command=sales_analysis)
salesanalysis_button.grid(row=0, column=3, padx=10, pady=0)
#################################################################################################
def customer_analysis():
    # Query for Customer Analysis
    query = """
    SELECT c.customer_id, SUM(od.subtotal) AS TotalPurchaseAmount
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN orderdetails od ON o.order_id = od.order_id
    GROUP BY c.customer_id
    ORDER BY TotalPurchaseAmount DESC
    LIMIT 50;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['CustomerID', 'TotalPurchaseAmount'])

    # Visualization (example: bar plot)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='CustomerID', y='TotalPurchaseAmount', data=df, palette='magma')
    plt.title('Top 50 Customers by Total Purchase Amount')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Purchase Amount')
    plt.show()

# Call this function when the corresponding button is clicked
customeranalysis_button = ttk.Button(leftFrame, text='Customer Analysis', width=25, state=NORMAL, command=customer_analysis)
customeranalysis_button.grid(row=1, column=3, padx=10, pady=0)
#################################################################################################

def inventory_management():
    # Query for Inventory Management
    query = """
    SELECT p.product_id, p.name AS ProductName, i.stock_quantity, i.restock_threshold
    FROM Products p
    JOIN Inventory i ON p.product_id = i.product_id
    WHERE i.stock_quantity < i.restock_threshold;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['ProductID', 'ProductName', 'StockQuantity', 'RestockThreshold'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
inventorymanagement_button = ttk.Button(leftFrame, text='Inventory Management', width=25, state=NORMAL, command=inventory_management)
inventorymanagement_button.grid(row=2, column=3, padx=10, pady=0)
#################################################################################################

def employee_performance():
    # Query for Employee Performance
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, 
           SUM(s.total_sales_amount) AS TotalSales, 
           COUNT(s.sale_id) AS TotalTransactions, 
           SUM(s.total_sales_amount) / COUNT(s.sale_id) AS AvgSalesPerTransaction
    FROM Sales s
    INNER JOIN Employee e ON s.employee_id = e.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['EmployeeID', 'FirstName', 'LastName', 'TotalSales', 'TotalTransactions', 'AvgSalesPerTransaction'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
employeeperformance_button = ttk.Button(leftFrame, text='Employee Performance', width=25, state=NORMAL, command=employee_performance)
employeeperformance_button.grid(row=3, column=3, padx=10, pady=0)
#################################################################################################

def store_analysis():
    # Query for Store Analysis
    query = """
    SELECT
        sl.store_id,
        sl.store_name,
        COUNT(v.visit_id) AS TotalVisits,
        COUNT(DISTINCT v.customer_id) AS UniqueVisitors,
        COUNT(DISTINCT t.transaction_id) AS TotalTransactions,
        SUM(t.amount) AS TotalSales
    FROM
        store_locations sl
    LEFT JOIN
        visits v ON sl.store_id = v.store_id
    LEFT JOIN
        transactions t ON v.visit_id = t.visit_id
    GROUP BY
        sl.store_id, sl.store_name
    ORDER BY
        sl.store_id;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['StoreID', 'StoreName', 'TotalVisits', 'UniqueVisitors', 'TotalTransactions', 'TotalSales'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
storeanalysis_button = ttk.Button(leftFrame, text='Store Analysis', width=25, state=NORMAL, command=store_analysis)
storeanalysis_button.grid(row=4, column=3, padx=10, pady=0)
#################################################################################################

def financial_analysis():
    # Query for Financial Analysis
    query = """
    SELECT
        DATE_FORMAT(s.sale_date, '%Y-%m') AS Month,
        SUM(s.total_sales_amount) AS TotalSales,
        COUNT(t.transaction_id) AS TotalTransactions,
        SUM(t.amount) AS TotalTransactionAmount
    FROM
        Sales s
    LEFT JOIN
        Transactions t ON s.sale_date = t.date
    GROUP BY
        Month
    ORDER BY
        Month;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['Month', 'TotalSales', 'TotalTransactions', 'TotalTransactionAmount'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
financialanalysis_button = ttk.Button(leftFrame, text='Financial Analysis', width=25, state=NORMAL, command=financial_analysis)
financialanalysis_button.grid(row=5, column=3, padx=10, pady=0)
#################################################################################################

def visitation_analysis():
    # Query for Visitation Analysis
    query = """
    SELECT
        v.date AS VisitDate,
        COUNT(v.visit_id) AS TotalVisits,
        COUNT(t.transaction_id) AS TotalTransactions
    FROM
        Visits v
    LEFT JOIN
        Transactions t ON v.visit_id = t.visit_id
    GROUP BY
        VisitDate
    ORDER BY
        VisitDate;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['VisitDate', 'TotalVisits', 'TotalTransactions'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
visitationanalysis_button = ttk.Button(leftFrame, text='Visitation Analysis', width=25, state=NORMAL, command=visitation_analysis)
visitationanalysis_button.grid(row=6, column=3, padx=10, pady=0)
#################################################################################################

def transaction_analysis():
    # Query for Transaction Analysis
    query = """
    SELECT
        t.transaction_id,
        t.transaction_type,
        t.date AS transaction_date,
        o.order_id,
        o.customer_id,
        o.order_date,
        o.total_amount AS order_total_amount,
        o.payment_method,
        o.payment_date AS payment_date,
        p.product_id,
        p.name AS product_name,
        p.category AS product_category,
        p.price AS product_price
    FROM transactions t
    INNER JOIN orders o ON t.order_id = o.order_id
    INNER JOIN order_details od ON o.order_id = od.order_id
    INNER JOIN products p ON od.product_id = p.product_id;
    """
    # Execute the query
    mycursor.execute(query)
    # Fetch the results
    results = mycursor.fetchall()

    # Convert results to a DataFrame for visualization
    df = pd.DataFrame(results, columns=['TransactionID', 'TransactionType', 'TransactionDate',
                                         'OrderID', 'CustomerID', 'OrderDate', 'OrderTotalAmount',
                                         'PaymentMethod', 'PaymentDate', 'ProductID', 'ProductName',
                                         'ProductCategory', 'ProductPrice'])

    # Visualization (example: table display)
    print(df)

# Call this function when the corresponding button is clicked
transactionanalysis_button = ttk.Button(leftFrame, text='Transaction Analysis', width=25, state=NORMAL, command=transaction_analysis)
transactionanalysis_button.grid(row=7, column=3, padx=10, pady=0)
#####################################################
#####################################################
rightframe = Frame(root, bg='white', relief=RIDGE)
rightframe.place(x=320, y=70, width=0, height=550)
#####################################################

ScrollbarX = Scrollbar(rightframe, orient=HORIZONTAL)
ScrollbarY = Scrollbar(rightframe, orient=VERTICAL)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')

root.mainloop()