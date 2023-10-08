from tkinter import *
from tkinter import ttk


def open_customer_window(root, mycursor):
    customer_window = Toplevel(root)
    customer_window.title('Customer Data')
    customer_window.geometry('800x550')

    customer_frame = Frame(customer_window, bg='white', relief=RIDGE)
    customer_frame.pack(fill=BOTH, expand=1)

    customer_scroll_x = Scrollbar(customer_frame, orient=HORIZONTAL)
    customer_scroll_y = Scrollbar(customer_frame, orient=VERTICAL)

    customer_table = ttk.Treeview(customer_frame, columns=(
        'CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address',
        'RegistrationDate', 'LoyaltyPoints'),
        xscrollcommand=customer_scroll_x.set,
        yscrollcommand=customer_scroll_y.set)

    customer_scroll_x.config(command=customer_table.xview)
    customer_scroll_y.config(command=customer_table.yview)

    customer_scroll_x.pack(side=BOTTOM, fill=X)
    customer_scroll_y.pack(side=RIGHT, fill=Y)

    customer_table.pack(fill=BOTH, expand=1)

    customer_table.heading('CustomerID', text='CustomerID')
    customer_table.heading('FirstName', text='FirstName')
    customer_table.heading('LastName', text='LastName')
    customer_table.heading('Email', text='Email')
    customer_table.heading('Phone', text='Phone')
    customer_table.heading('Address', text='Address')
    customer_table.heading('RegistrationDate', text='RegistrationDate')
    customer_table.heading('LoyaltyPoints', text='LoyaltyPoints')

    customer_table.column('CustomerID', width=20, anchor=CENTER)
    customer_table.column('FirstName', width=60, anchor=CENTER)
    customer_table.column('LastName', width=60, anchor=CENTER)
    customer_table.column('Email', width=60, anchor=CENTER)
    customer_table.column('Phone', width=60, anchor=CENTER)
    customer_table.column('Address', width=60, anchor=CENTER)
    customer_table.column('RegistrationDate', width=60, anchor=CENTER)
    customer_table.column('LoyaltyPoints', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    customer_table.config(show='headings')

    query='SELECT * FROM customers'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        customer_table.insert('',END,values=data_list)