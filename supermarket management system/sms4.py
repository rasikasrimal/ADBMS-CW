import pymysql
from tkinter import *
from tkinter import ttk, messagebox
import ttkthemes

def create_button(left_frame, text, state, command):
    button = ttk.Button(left_frame, text=text, width=25, state=state, command=command)
    button.grid(padx=10, pady=0)
    return button

def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Connected to Database')
            connectWindow.destroy()
            addcustomerButton.config(state=NORMAL)
        except Exception as e:
            messagebox.showerror('Error', f'Error connecting to database: {e}')

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

    connectButton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, column=0, padx=10, pady=10)

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')

root.geometry('1174x680+0+0')
root.resizable(True, True)
root.title('DBMS For Supermarket')

s = 'Supermarket DBMS'
sliderLabel = Label(root, text=s, font=('Helvetica', 30, 'bold'), width=30, fg='black', anchor='w')
sliderLabel.place(x=5, y=5)

connectButton = ttk.Button(root, text='Connect Database', width=25, command=connect_database)
connectButton.place(x=873, y=0)

leftFrame = Frame(root, relief=RIDGE, border=2)
leftFrame.place(x=10, y=70, width=1100, height=534)

addcustomerButton = create_button(leftFrame, 'Add customer', DISABLED, add_customer)
addproductButton = create_button(leftFrame, 'Add Product', NORMAL, add_product)
addorderButton = create_button(leftFrame, 'Add order', DISABLED, add_order)
addemployeeButton = create_button(leftFrame, 'Add employee', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addorderdetailButton = create_button(leftFrame, 'Add orderdetail', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addsalesButton = create_button(leftFrame, 'Add Sales', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addpromotionButton = create_button(leftFrame, 'Add promotion', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addpromotionusageButton = create_button(leftFrame, 'Add promotionusage', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addinventoryButton = create_button(leftFrame, 'Add inventory', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addsupplierButton = create_button(leftFrame, 'Add Supplier', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addtransactionButton = create_button(leftFrame, 'Add transaction', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addstorelocationButton = create_button(leftFrame, 'Add Storelocation', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))
addvisitButton = create_button(leftFrame, 'Add visit', DISABLED, lambda: toplevel_date('Add Student', 'Add Student', add_data))

show_customer_button = create_button(leftFrame, 'Customers', DISABLED, lambda: customer.open_customer_window(root, mycursor))
show_product_button = create_button(leftFrame, 'Products', DISABLED, lambda: product.open_product_window(root, mycursor))
show_order_button = create_button(leftFrame, 'Order', DISABLED, lambda: order.open_order_window(root, mycursor))
show_employee_button = create_button(leftFrame, 'Employee', DISABLED, lambda: employee.open_employee_window(root, mycursor))
show_orderdetail_button = create_button(leftFrame, 'Order Detail', DISABLED, lambda: orderdetail.open_orderdetail_window(root, mycursor))
show_sale_button = create_button(leftFrame, 'Sales', DISABLED, lambda: sale.open_sale_window(root, mycursor))
show_promotion_button = create_button(leftFrame, 'Promotion', DISABLED, lambda: promotion.open_promotion_window(root, mycursor))
show_promotionusage_button = create_button(leftFrame, 'Promotion Usage', DISABLED, lambda: promotionusage.open_promotionusage_window(root, mycursor))
show_inventory_button = create_button(leftFrame, 'Inventory', DISABLED, lambda: inventory.open_inventory_window(root, mycursor))
show_supplier_button = create_button(leftFrame, 'Supplier', DISABLED, lambda: supplier.open_supplier_window(root, mycursor))
show_transaction_button = create_button(leftFrame, 'Transaction', DISABLED, lambda: transaction.open_transaction_window(root, mycursor))
show_storelocation_button = create_button(leftFrame, 'Storelocation', DISABLED, lambda: storelocation.open_storelocation_window(root, mycursor))
show_visit_button = create_button(leftFrame, 'Visits', DISABLED, lambda: visits.open_visit_window(root, mycursor))

root.mainloop()
