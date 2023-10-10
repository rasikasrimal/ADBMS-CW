from tkinter import *
from tkinter import ttk


def open_order_window(root, mycursor):
    order_window = Toplevel(root)
    order_window.title('order Data')
    order_window.geometry('800x550')

    order_frame = Frame(order_window, bg='white', relief=RIDGE)
    order_frame.pack(fill=BOTH, expand=1)

    order_scroll_x = Scrollbar(order_frame, orient=HORIZONTAL)
    order_scroll_y = Scrollbar(order_frame, orient=VERTICAL)

    order_table = ttk.Treeview(order_frame, columns=(
        'OrderID', 'CustomerID', 'OrderDate', 'TotalAmount', 'PaymentMethod', 'PaymentDate'
    ),
        xscrollcommand=order_scroll_x.set,
        yscrollcommand=order_scroll_y.set)

    order_scroll_x.config(command=order_table.xview)
    order_scroll_y.config(command=order_table.yview)

    order_scroll_x.pack(side=BOTTOM, fill=X)
    order_scroll_y.pack(side=RIGHT, fill=Y)

    order_table.pack(fill=BOTH, expand=1)

    order_table.heading('OrderID', text='OrderID')
    order_table.heading('CustomerID', text='CustomerID')
    order_table.heading('OrderDate', text='OrderDate')
    order_table.heading('TotalAmount', text='TotalAmount')
    order_table.heading('PaymentMethod', text='PaymentMethod')
    order_table.heading('PaymentDate', text='PaymentDate')

    order_table.column('OrderID', width=20, anchor=CENTER)
    order_table.column('CustomerID', width=60, anchor=CENTER)
    order_table.column('OrderDate', width=60, anchor=CENTER)
    order_table.column('TotalAmount', width=60, anchor=CENTER)
    order_table.column('PaymentMethod', width=60, anchor=CENTER)
    order_table.column('PaymentDate', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    order_table.config(show='headings')

    query='SELECT * FROM orders'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        order_table.insert('',END,values=data_list)