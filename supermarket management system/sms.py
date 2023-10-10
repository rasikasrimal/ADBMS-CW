from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

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




count = 0
text = ''

#################################################################################################
# def open_treeview_window():
#     treeview_window = Toplevel(root)
#     treeview_window.title('Customer Data')
#     treeview_window.geometry('800x550')

#     treeview_frame = Frame(treeview_window, bg='white', relief=RIDGE)
#     treeview_frame.pack(fill=BOTH, expand=1)

#     treeview_scroll_x = Scrollbar(treeview_frame, orient=HORIZONTAL)
#     treeview_scroll_y = Scrollbar(treeview_frame, orient=VERTICAL)

#     customer_table = ttk.Treeview(treeview_frame, columns=(
#         'CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address',
#         'RegistrationDate', 'LoyaltyPoints'),
#         xscrollcommand=treeview_scroll_x.set,
#         yscrollcommand=treeview_scroll_y.set)

#     treeview_scroll_x.config(command=customer_table.xview)
#     treeview_scroll_y.config(command=customer_table.yview)

#     treeview_scroll_x.pack(side=BOTTOM, fill=X)
#     treeview_scroll_y.pack(side=RIGHT, fill=Y)

#     customer_table.pack(fill=BOTH, expand=1)

#     customer_table.heading('CustomerID', text='CustomerID')
#     customer_table.heading('FirstName', text='FirstName')
#     customer_table.heading('LastName', text='LastName')
#     customer_table.heading('Email', text='Email')
#     customer_table.heading('Phone', text='Phone')
#     customer_table.heading('Address', text='Address')
#     customer_table.heading('RegistrationDate', text='RegistrationDate')
#     customer_table.heading('LoyaltyPoints', text='LoyaltyPoints')

#     customer_table.column('CustomerID', width=20, anchor=CENTER)
#     customer_table.column('FirstName', width=60, anchor=CENTER)
#     customer_table.column('LastName', width=60, anchor=CENTER)
#     customer_table.column('Email', width=60, anchor=CENTER)
#     customer_table.column('Phone', width=60, anchor=CENTER)
#     customer_table.column('Address', width=60, anchor=CENTER)
#     customer_table.column('RegistrationDate', width=60, anchor=CENTER)
#     customer_table.column('LoyaltyPoints', width=60, anchor=CENTER)

#     style = ttk.Style()
#     style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
#     style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
#     customer_table.config(show='headings')

#################################################################################################

# def open_customer_window():
#     customer_window = Toplevel(root)
#     customer_window.title('Customer Data')
#     customer_window.geometry('800x550')

#     customer_frame = Frame(customer_window, bg='white', relief=RIDGE)
#     customer_frame.pack(fill=BOTH, expand=1)

#     customer_scroll_x = Scrollbar(customer_frame, orient=HORIZONTAL)
#     customer_scroll_y = Scrollbar(customer_frame, orient=VERTICAL)

#     customer_table = ttk.Treeview(customer_frame, columns=(
#         'CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address',
#         'RegistrationDate', 'LoyaltyPoints'),
#         xscrollcommand=customer_scroll_x.set,
#         yscrollcommand=customer_scroll_y.set)

#     customer_scroll_x.config(command=customer_table.xview)
#     customer_scroll_y.config(command=customer_table.yview)

#     customer_scroll_x.pack(side=BOTTOM, fill=X)
#     customer_scroll_y.pack(side=RIGHT, fill=Y)

#     customer_table.pack(fill=BOTH, expand=1)

#     customer_table.heading('CustomerID', text='CustomerID')
#     customer_table.heading('FirstName', text='FirstName')
#     customer_table.heading('LastName', text='LastName')
#     customer_table.heading('Email', text='Email')
#     customer_table.heading('Phone', text='Phone')
#     customer_table.heading('Address', text='Address')
#     customer_table.heading('RegistrationDate', text='RegistrationDate')
#     customer_table.heading('LoyaltyPoints', text='LoyaltyPoints')

#     customer_table.column('CustomerID', width=20, anchor=CENTER)
#     customer_table.column('FirstName', width=60, anchor=CENTER)
#     customer_table.column('LastName', width=60, anchor=CENTER)
#     customer_table.column('Email', width=60, anchor=CENTER)
#     customer_table.column('Phone', width=60, anchor=CENTER)
#     customer_table.column('Address', width=60, anchor=CENTER)
#     customer_table.column('RegistrationDate', width=60, anchor=CENTER)
#     customer_table.column('LoyaltyPoints', width=60, anchor=CENTER)

#     style = ttk.Style()
#     style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
#     style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
#     customer_table.config(show='headings')

#     query='SELECT * FROM customers'
#     mycursor.execute(query)
#     fetched_data=mycursor.fetchall()

#     for data in fetched_data:
#         data_list=list(data)
#         customer_table.insert('',END,values=data_list)

#################################################################################################

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_table.get_children()
    newlist = []
    for index in indexing:
        content=student_table.item(index)
        datalist=content['values']
        newlist.append(datalist)
    
    table=pandas.DataFrame(newlist, columns=['id', 'name', 'mobile', 'email', 'address', 'gender', 'dob', 'added_date', 'added-time'])
    table.to_csv(url, index=False)
    messagebox.showeinfo('Success', 'Data Exported Successfully')


def toplevel_date(title, button_text, command):
    global idEntry, mobileEntry, nameEntry, emailEntry, addressEntry, genderEntry, dobEntry, screen
    screen = Toplevel()
    screen.grab_set()
    screen.title('Update Student')
    screen.resizable(False, False)
    idlable = Label(screen, text='ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(screen, text='Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobilelable = Label(screen, text='Mobile', font=('Helvetica', 15, 'bold'))
    mobilelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mobileEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emaillable = Label(screen, text='Email', font=('Helvetica', 15, 'bold'))
    emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    emailEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addresslable = Label(screen, text='Address', font=('Helvetica', 15, 'bold'))
    addresslable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    addressEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderlable = Label(screen, text='Gender', font=('Helvetica', 15, 'bold'))
    genderlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    genderEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    doblable = Label(screen, text='DOB', font=('Helvetica', 15, 'bold'))
    doblable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    dobEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    student_button = ttk.Button(screen, text=button_text, width=25, command=command)
    student_button.grid(row=9, columnspan=2, padx=10, pady=10)

    if title == 'Update Student':
        indexing=student_table.focus()

        content=student_table.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        mobileEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])


def update_data():
    global currentdate, currenttime
    currentdate = time.strftime('%d:%m:%Y')
    currenttime = time.strftime('%H:%M:%S')

    query = 'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
    mycursor.execute(query, (
        nameEntry.get(),
        mobileEntry.get(),
        emailEntry.get(),
        addressEntry.get(),
        genderEntry.get(),
        dobEntry.get(),
        currentdate,
        currenttime,
        idEntry.get()
    ))
    con.commit()
    messagebox.showinfo('Success', 'Student Updated Successfully', parent=screen)
    screen.destroy()
    show_student()

# def show_student():
#     query='SELECT * FROM student'
#     mycursor.execute(query)
#     fetched_data=mycursor.fetchall()
#     student_table.delete(*student_table.get_children())
#     for data in fetched_data:
#         data_list=list(data)
#         student_table.insert('',END,values=data_list)
#################################################################################################
def show_customer():
    query='SELECT * FROM customers'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    customer_table.delete(*customer_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        customer_table.insert('',END,values=data_list)

def show_product():
    query='SELECT * FROM products'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    product_table.delete(*product_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        product_table.insert('',END,values=data_list)

def show_order():
    query='SELECT * FROM orders'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    order_table.delete(*order_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        order_table.insert('',END,values=data_list)

def show_orderdetail():
    query='SELECT * FROM orderdetails'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    orderdetail_table.delete(*orderdetail_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        orderdetail_table.insert('',END,values=data_list)

def show_employee():
    query='SELECT * FROM orders'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    employee_table.delete(*employee_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        employee_table.insert('',END,values=data_list)

def show_sale():
    query='SELECT * FROM sales'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    sale_table.delete(*sale_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        sale_table.insert('',END,values=data_list)

def show_promotions():
    query='SELECT * FROM promotions'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    promotions_table.delete(*promotions_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        promotions.insert('',END,values=data_list)

def show_promotionusage():
    query='SELECT * FROM promotionusage'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    promotionusage_table.delete(*promotionusage_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        promotionusage_table.insert('',END,values=data_list)

def show_inventory():
    query='SELECT * FROM inventory'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    inventory_table.delete(*inventory_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        inventory_table.insert('',END,values=data_list)

def show_supplier():
    query='SELECT * FROM supplier'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    supplier_table.delete(*supplier_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        supplier_table.insert('',END,values=data_list)

def show_transaction():
    query='SELECT * FROM transaction'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    transaction_table.delete(*transaction_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        transaction_table.insert('',END,values=data_list)

def show_storelocation():
    query='SELECT * FROM storelocation'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    storelocation_table.delete(*storelocation_table.get_children())
    for data in fetched_data:
        data_list=list(data)
        storelocation_table.insert('',END,values=data_list)
#################################################################################################

# def search_data():
#     query = 'SELECT * FROM student WHERE id=%s or Name=%s or Email=%s or mobile=%s or gender=%s or dob=%s' #or address=%s'

#     mycursor.execute(query, (
#         idEntry.get(),
#         nameEntry.get(),
#         emailEntry.get(),
#         mobileEntry.get(), 
#         # addressEntry.get(),
#         genderEntry.get(), 
#         dobEntry.get() 
#         ))
#     student_table.delete(*student_table.get_children())
#     fetched_data = mycursor.fetchall()
#     for data in fetched_data:
#         student_table.insert('', END, values=data)

#################################################################################################

def add_data():
    global currentdate, currenttime
    currentdate = time.strftime('%Y:%m:%d')
    currenttime = time.strftime('%H:%M:%S')

    if (
        idEntry.get() == '' or
        nameEntry.get() == '' or
        mobileEntry.get() == '' or
        emailEntry.get() == '' or
        addressEntry.get() == '' or
        genderEntry.get() == '' or
        dobEntry.get() == ''
    ):
        messagebox.showerror('Error', 'All fields are required', parent=screen)
    else:
        query = 'INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            mycursor.execute(query, (
                idEntry.get(),
                nameEntry.get(),
                mobileEntry.get(),
                emailEntry.get(),
                addressEntry.get(), 
                genderEntry.get(), 
                dobEntry.get(), 
                currentdate,
                currenttime
            ))
            con.commit()
            result = messagebox.askyesnocancel('Success', 'Do you want to clear the form?')
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                mobileEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', 'This ID is already taken', parent=screen)
            return

        query = 'SELECT * FROM student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            data_list = list(data)
            student_table.insert('', END, values=data_list)

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
            query = 'CREATE DATABASE IF NOT EXISTS adbms'
            mycursor.execute(query)
            query = 'USE adbms'
            mycursor.execute(query)
            
            query = ''' 
            -- Create the Customers table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                FirstName VARCHAR(50),
                LastName VARCHAR(50),
                Email VARCHAR(255),
                Phone VARCHAR(15),
                Address VARCHAR(255),
                RegistrationDate DATE,
                LoyaltyPoints INT
            );

            -- Create the Products table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Products (
                ProductID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100),
                Category VARCHAR(50),
                Description TEXT,
                Price DECIMAL(10, 2),
                StockQuantity INT,
                SupplierID INT,
                FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
            );

            -- Create the Orders table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Orders (
                OrderID INT AUTO_INCREMENT PRIMARY KEY,
                CustomerID INT,
                OrderDate DATE,
                TotalAmount DECIMAL(10, 2),
                PaymentMethod VARCHAR(50),
                PaymentDate DATE,
                FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
            );

            -- Create the OrderDetails table if it doesn't exist
            CREATE TABLE IF NOT EXISTS OrderDetails (
                OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
                OrderID INT,
                ProductID INT,
                Quantity INT,
                Subtotal DECIMAL(10, 2),
                FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
            );

            -- Create the Employees table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
                FirstName VARCHAR(50),
                LastName VARCHAR(50),
                Position VARCHAR(50),
                Email VARCHAR(100),
                Phone VARCHAR(15),
                HireDate DATE,
                StoreID INT,
                FOREIGN KEY (StoreID) REFERENCES StoreLocations(StoreID)
            );

            -- Create the Sales table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Sales (
                SaleID INT AUTO_INCREMENT PRIMARY KEY,
                EmployeeID INT,
                SaleDate DATE,
                TotalSalesAmount DECIMAL(10, 2),
                FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
            );

            -- Create the Promotions table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Promotions (
                PromotionID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100),
                Description TEXT,
                StartDate DATE,
                EndDate DATE,
                DiscountPercentage DECIMAL(5, 2)
            );

            -- Create the PromotionUsage table if it doesn't exist
            CREATE TABLE IF NOT EXISTS PromotionUsage (
                UsageID INT AUTO_INCREMENT PRIMARY KEY,
                PromotionID INT,
                OrderID INT,
                FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID),
                FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
            );

            -- Create the Inventory table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Inventory (
                InventoryID INT AUTO_INCREMENT PRIMARY KEY,
                ProductID INT,
                StockQuantity INT,
                RestockThreshold INT,
                FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
            );

            -- Create the StoreLocations table if it doesn't exist
            CREATE TABLE IF NOT EXISTS StoreLocations (
                StoreID INT AUTO_INCREMENT PRIMARY KEY,
                StoreName VARCHAR(100),
                Address VARCHAR(255),
                Phone VARCHAR(15),
                Manager VARCHAR(100),
                OpeningDate DATE
            );

            -- Create the Suppliers table if it doesn't exist
            CREATE TABLE IF NOT EXISTS Suppliers (
                SupplierID INT AUTO_INCREMENT PRIMARY KEY,
                SupplierName VARCHAR(100),
                ContactPerson VARCHAR(100),
                Email VARCHAR(255),
                Phone VARCHAR(15),
                Address VARCHAR(255)
            );
                '''
            mycursor.execute(query)
        except:
                query = 'USE adbms'
                mycursor.execute(query)

        # con.commit()
        # con.close()

        messagebox.showinfo('Success', 'Connected to Database')
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        # searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportDataButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
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

        # OrderDetails
        # Employees
        # Sales
        # Promotions
        # PromotionUsage
        # Inventory
        # Suppliers
        # Transactions
        # StoreLocations

#############################################################

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
root.set_theme('radiance')

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

s = 'DBMS For Supermarket'
sliderLabel = Label(root, text=s, font=('Helvetica', 30, 'bold'), width=30, fg='black', anchor='w')
sliderLabel.place(x=5, y=5)

connectButton = ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=980, y=0)

#####################################################
leftFrame = Frame(root, relief=RIDGE, border=2)
leftFrame.place(x=10, y=70, width=300, height=534)
######################################################

logo_image = PhotoImage(file='images/student2.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=lambda: toplevel_date('Add Student', 'Add Student', add_data))
addstudentButton.grid(row=1, column=0, padx=10, pady=0)

# searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=lambda: toplevel_date('Search Student', 'Search Student', search_data))
# searchstudentButton.grid(row=2, column=0, padx=10, pady=0)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=lambda: delete_ops.delete_student(mycursor, con, student_table))
deletestudentButton.grid(row=3, column=0, padx=10, pady=0)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED, command=lambda: toplevel_date('Update Student', 'Update Student', update_data))
updatestudentButton.grid(row=4, column=0, padx=10, pady=0)

showstudentButton = ttk.Button(leftFrame, text='Show Customer OLD', width=25, state=DISABLED, command=show_customer)
showstudentButton.grid(row=5, column=0, padx=10, pady=0)

exportDataButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, command=lambda: export_ops.export_data(student_table))
exportDataButton.grid(row=6, column=0, padx=10, pady=0)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=lambda: exit_ops.handle_exit(root))
exitButton.grid(row=7, column=0, padx=10, pady=0)

show_customer_button = ttk.Button(leftFrame, text='Show Customers', width=25, state=DISABLED, command=lambda: customer.open_customer_window(root, mycursor))
show_customer_button.grid(row=8, column=0, padx=10, pady=0)

show_product_button = ttk.Button(leftFrame, text='Show Products', width=25, state=DISABLED, command=lambda: product.open_product_window(root, mycursor))
show_product_button.grid(row=9, column=0, padx=10, pady=0)

show_order_button = ttk.Button(leftFrame, text='Show Order', width=25, state=DISABLED, command=lambda: order.open_order_window(root, mycursor))
show_order_button.grid(row=10, column=0, padx=10, pady=0)

#################################################################################################
show_employee_button = ttk.Button(leftFrame, text='Show Employee', width=25, state=DISABLED, command=lambda: employee.open_employee_window(root, mycursor))
show_employee_button.grid(row=11, column=0, padx=10, pady=0)

show_orderdetail_button = ttk.Button(leftFrame, text='Order Detail', width=25, state=DISABLED, command=lambda: orderdetail.open_orderdetail_window(root, mycursor))
show_orderdetail_button.grid(row=12, column=0, padx=10, pady=0)

show_sale_button = ttk.Button(leftFrame, text='Sales', width=25, state=DISABLED, command=lambda: sale.open_sale_window(root, mycursor))
show_sale_button.grid(row=13, column=0, padx=10, pady=0)

show_promotion_button = ttk.Button(leftFrame, text='Promotion', width=25, state=DISABLED, command=lambda: promotion.open_promotion_window(root, mycursor))
show_promotion_button.grid(row=14, column=0, padx=10, pady=0)

show_promotionusage_button = ttk.Button(leftFrame, text='Promotion Usage', width=25, state=DISABLED, command=lambda: promotionusage.open_promotionusage_window(root, mycursor))
show_promotionusage_button.grid(row=15, column=0, padx=10, pady=0)

show_inventory_button = ttk.Button(leftFrame, text='Show Inventory', width=25, state=DISABLED, command=lambda: inventory.open_inventory_window(root, mycursor))
show_inventory_button.grid(row=16, column=0, padx=10, pady=0)

show_supplier_button = ttk.Button(leftFrame, text='Show supplier', width=25, state=DISABLED, command=lambda: supplier.open_supplier_window(root, mycursor))
show_supplier_button.grid(row=17, column=0, padx=10, pady=0)

show_transaction_button = ttk.Button(leftFrame, text='Show transaction', width=25, state=DISABLED, command=lambda: transaction.open_transaction_window(root, mycursor))
show_transaction_button.grid(row=18, column=0, padx=10, pady=0)

show_storelocation_button = ttk.Button(leftFrame, text='Show storelocation', width=25, state=DISABLED, command=lambda: storelocation.open_storelocation_window(root, mycursor))
show_storelocation_button.grid(row=19, column=0, padx=10, pady=0)

#################################################################################################





#####################################################
rightframe = Frame(root, bg='white', relief=RIDGE)
rightframe.place(x=320, y=70, width=800, height=550)
#####################################################

ScrollbarX = Scrollbar(rightframe, orient=HORIZONTAL)
ScrollbarY = Scrollbar(rightframe, orient=VERTICAL)

student_table = ttk.Treeview(rightframe, columns=(
    'ID', 'Name', 'Mobile No', 'Email', 'Address', 
    'Gender','DOB', 'Added Date', 'Added Time' ),
        xscrollcommand=ScrollbarX.set,
        yscrollcommand=ScrollbarY.set)
#################################################################################################
# customer_table = ttk.Treeview(rightframe, columns=(
#     'CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address', 
#     'RegistrationDate','LoyaltyPoints' ),
#         xscrollcommand=ScrollbarX.set,
#         yscrollcommand=ScrollbarY.set)

ScrollbarX.config(command=student_table.xview)
ScrollbarY.config(command=student_table.yview)

ScrollbarX.pack(side=BOTTOM, fill=X)
ScrollbarY.pack(side=RIGHT, fill=Y)

student_table.pack(fill=BOTH, expand=1)

student_table.heading('ID', text='ID')
student_table.heading('Name', text='Name')
student_table.heading('Mobile No', text='Mobile No')
student_table.heading('Email', text='Email')
student_table.heading('Address', text='Address')
student_table.heading('Gender', text='Gender')
student_table.heading('DOB', text='DOB')
student_table.heading('Added Date', text='Added Date')
student_table.heading('Added Time', text='Added Time')

student_table.column('ID', width=20, anchor=CENTER)
student_table.column('Name', width=60, anchor=CENTER)
student_table.column('Mobile No', width=60, anchor=CENTER)
student_table.column('Email', width=60, anchor=CENTER)
student_table.column('Address', width=60, anchor=CENTER)
student_table.column('Gender', width=30, anchor=CENTER)
student_table.column('DOB', width=60, anchor=CENTER)
student_table.column('Added Date', width=60, anchor=CENTER)
student_table.column('Added Time', width=60, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
student_table.config(show='headings')


root.mainloop()