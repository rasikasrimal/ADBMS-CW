from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import ttkthemes
from datetime import datetime

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
        addproductButton.config(state=NORMAL)
        addorderButton.config(state=NORMAL)
        addemployeeButton.config(state=NORMAL)
        addorderdetailButton.config(state=NORMAL)
        addsalesButton.config(state=NORMAL)
        addpromotionButton.config(state=NORMAL)
        addpromotionusageButton.config(state=NORMAL)
        addinventoryButton.config(state=NORMAL)
        addsupplierButton.config(state=NORMAL)
        addtransactionButton.config(state=NORMAL)
        addstorelocationButton.config(state=NORMAL)
        addvisitButton.config(state=NORMAL)

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

    userEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'))
    userEntry.grid(row=1, column=1, padx=10, pady=10)

    passwordLabel = Label(connectWindow, text='Password', font=('Helvetica', 15, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=10, pady=10)

    PasswordEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'), show='*')
    PasswordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, column=0, columnspan=2, pady=10)
# Function to handle add customer button click
def add_customer():
    # Function to handle add customer window submit button click
    def add_customer_submit():
        first_name = firstNameEntry.get()
        last_name = lastNameEntry.get()
        email = emailEntry.get()
        phone = phoneEntry.get()
        address = addressEntry.get()

        # Add customer details to the database
        try:
            query = 'INSERT INTO customers (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)'
            values = (first_name, last_name, email, phone, address)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Customer added successfully')
            add_customer_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_customer_window = Toplevel(root)
    add_customer_window.grab_set()
    add_customer_window.title('Add Customer')
    add_customer_window.geometry('500x400+500+200')
    add_customer_window.resizable(False, False)

    firstNameLabel = Label(add_customer_window, text='First Name', font=('Helvetica', 15, 'bold'))
    firstNameLabel.grid(row=0, column=0, padx=10, pady=10)

    firstNameEntry = Entry(add_customer_window, font=('Helvetica', 15, 'bold'))
    firstNameEntry.grid(row=0, column=1, padx=10, pady=10)

    lastNameLabel = Label(add_customer_window, text='Last Name', font=('Helvetica', 15, 'bold'))
    lastNameLabel.grid(row=1, column=0, padx=10, pady=10)

    lastNameEntry = Entry(add_customer_window, font=('Helvetica', 15, 'bold'))
    lastNameEntry.grid(row=1, column=1, padx=10, pady=10)

    emailLabel = Label(add_customer_window, text='Email', font=('Helvetica', 15, 'bold'))
    emailLabel.grid(row=2, column=0, padx=10, pady=10)

    emailEntry = Entry(add_customer_window, font=('Helvetica', 15, 'bold'))
    emailEntry.grid(row=2, column=1, padx=10, pady=10)

    phoneLabel = Label(add_customer_window, text='Phone', font=('Helvetica', 15, 'bold'))
    phoneLabel.grid(row=3, column=0, padx=10, pady=10)

    phoneEntry = Entry(add_customer_window, font=('Helvetica', 15, 'bold'))
    phoneEntry.grid(row=3, column=1, padx=10, pady=10)

    addressLabel = Label(add_customer_window, text='Address', font=('Helvetica', 15, 'bold'))
    addressLabel.grid(row=4, column=0, padx=10, pady=10)

    addressEntry = Entry(add_customer_window, font=('Helvetica', 15, 'bold'))
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_customer_window, text='Submit', command=add_customer_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = nameEntry.get()
        category = categoryEntry.get()
        price = priceEntry.get()
        stock_quantity = stockQuantityEntry.get()
        profit_per_unit = profitPerUnitEntry.get()
        supplier_id = supplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    nameLabel = Label(add_product_window, text='Name', font=('Helvetica', 15, 'bold'))
    nameLabel.grid(row=0, column=0, padx=10, pady=10)

    nameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    nameEntry.grid(row=0, column=1, padx=10, pady=10)

    categoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    categoryLabel.grid(row=1, column=0, padx=10, pady=10)

    categoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    categoryEntry.grid(row=1, column=1, padx=10, pady=10)

    priceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    priceLabel.grid(row=2, column=0, padx=10, pady=10)

    priceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    priceEntry.grid(row=2, column=1, padx=10, pady=10)

    stockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    stockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    stockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    stockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    profitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    profitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    profitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    profitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    supplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    supplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    supplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    supplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = totalAmountEntry.get()
        payment_method = paymentMethodEntry.get()
        payment_date = paymentDateEntry.get()
        customer_id = customerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    totalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    totalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    totalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    totalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    paymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    paymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    paymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    paymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    paymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    paymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    paymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    paymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    customerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    customerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    customerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    customerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Product Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Product Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        product_name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (product_name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
# Function to handle connect database button click
def connect_database():
    global con, mycursor
    try:
        con = pymysql.connect(
            host=databaseHostEntry.get(),
            user=databaseUserEntry.get(),
            password=databasePasswordEntry.get(),
            database=databaseNameEntry.get()
        )
        mycursor = con.cursor()
        messagebox.showinfo('Success', 'Connected to the database successfully')
        connect_database_window.destroy()
    except Exception as e:
        messagebox.showerror('Error', f'Error connecting to the database: {str(e)}')

# Function to handle connect database window submit button click
def connect_database_submit():
    connect_database()

# Function to handle add order button click
def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
# Function to handle add product button click
def add_product():
    # Function to handle add product window submit button click
    def add_product_submit():
        name = productNameEntry.get()
        category = productCategoryEntry.get()
        price = productPriceEntry.get()
        stock_quantity = productStockQuantityEntry.get()
        profit_per_unit = productProfitPerUnitEntry.get()
        supplier_id = productSupplierIdEntry.get()

        # Add product details to the database
        try:
            query = 'INSERT INTO products (name, category, price, stock_quantity, profit_per_unit, supplier_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s)'
            values = (name, category, price, stock_quantity, profit_per_unit, supplier_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Product added successfully')
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_product_window = Toplevel(root)
    add_product_window.grab_set()
    add_product_window.title('Add Product')
    add_product_window.geometry('500x400+500+200')
    add_product_window.resizable(False, False)

    productNameLabel = Label(add_product_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    productNameLabel.grid(row=0, column=0, padx=10, pady=10)

    productNameEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productNameEntry.grid(row=0, column=1, padx=10, pady=10)

    productCategoryLabel = Label(add_product_window, text='Category', font=('Helvetica', 15, 'bold'))
    productCategoryLabel.grid(row=1, column=0, padx=10, pady=10)

    productCategoryEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productCategoryEntry.grid(row=1, column=1, padx=10, pady=10)

    productPriceLabel = Label(add_product_window, text='Price', font=('Helvetica', 15, 'bold'))
    productPriceLabel.grid(row=2, column=0, padx=10, pady=10)

    productPriceEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productPriceEntry.grid(row=2, column=1, padx=10, pady=10)

    productStockQuantityLabel = Label(add_product_window, text='Stock Quantity', font=('Helvetica', 15, 'bold'))
    productStockQuantityLabel.grid(row=3, column=0, padx=10, pady=10)

    productStockQuantityEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productStockQuantityEntry.grid(row=3, column=1, padx=10, pady=10)

    productProfitPerUnitLabel = Label(add_product_window, text='Profit Per Unit', font=('Helvetica', 15, 'bold'))
    productProfitPerUnitLabel.grid(row=4, column=0, padx=10, pady=10)

    productProfitPerUnitEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productProfitPerUnitEntry.grid(row=4, column=1, padx=10, pady=10)

    productSupplierIdLabel = Label(add_product_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    productSupplierIdLabel.grid(row=5, column=0, padx=10, pady=10)

    productSupplierIdEntry = Entry(add_product_window, font=('Helvetica', 15, 'bold'))
    productSupplierIdEntry.grid(row=5, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_product_window, text='Submit', command=add_product_submit)
    submitButton.grid(row=6, column=0, columnspan=2, pady=10)
