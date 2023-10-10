from tkinter import *
from tkinter import ttk


def open_customer_window(root, mycursor):
    orderdetail_window = Toplevel(root)
    orderdetail_window.title('orderdetail Data')
    orderdetail_window.geometry('800x550')

    orderdetail_frame = Frame(orderdetail_window, bg='white', relief=RIDGE)
    orderdetail_frame.pack(fill=BOTH, expand=1)

    orderdetail_scroll_x = Scrollbar(orderdetail_frame, orient=HORIZONTAL)
    orderdetail_scroll_y = Scrollbar(orderdetail_frame, orient=VERTICAL)

    orderdetail_table = ttk.Treeview(orderdetail_frame, columns=(
        'CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address',
        'RegistrationDate', 'LoyaltyPoints'),
        xscrollcommand=orderdetail_scroll_x.set,
        yscrollcommand=orderdetail_scroll_y.set)

    orderdetail_scroll_x.config(command=orderdetail_table.xview)
    orderdetail_scroll_y.config(command=orderdetail_table.yview)

    orderdetail_scroll_x.pack(side=BOTTOM, fill=X)
    orderdetail_scroll_y.pack(side=RIGHT, fill=Y)

    orderdetail_table.pack(fill=BOTH, expand=1)

    orderdetail_table.heading('CustomerID', text='CustomerID')
    orderdetail_table.heading('FirstName', text='FirstName')
    orderdetail_table.heading('LastName', text='LastName')
    orderdetail_table.heading('Email', text='Email')
    orderdetail_table.heading('Phone', text='Phone')
    orderdetail_table.heading('Address', text='Address')
    orderdetail_table.heading('RegistrationDate', text='RegistrationDate')
    orderdetail_table.heading('LoyaltyPoints', text='LoyaltyPoints')

    orderdetail_table.column('CustomerID', width=20, anchor=CENTER)
    orderdetail_table.column('FirstName', width=60, anchor=CENTER)
    orderdetail_table.column('LastName', width=60, anchor=CENTER)
    orderdetail_table.column('Email', width=60, anchor=CENTER)
    orderdetail_table.column('Phone', width=60, anchor=CENTER)
    orderdetail_table.column('Address', width=60, anchor=CENTER)
    orderdetail_table.column('RegistrationDate', width=60, anchor=CENTER)
    orderdetail_table.column('LoyaltyPoints', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    orderdetail_table.config(show='headings')

    query='SELECT * FROM corderdetail'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        orderdetail_table.insert('',END,values=data_list)