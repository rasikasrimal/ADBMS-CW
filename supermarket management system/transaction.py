from tkinter import *
from tkinter import ttk


def open_transaction_window(root, mycursor):
    transaction_window = Toplevel(root)
    transaction_window.title('transaction Data')
    transaction_window.geometry('800x550')

    transaction_frame = Frame(transaction_window, bg='white', relief=RIDGE)
    transaction_frame.pack(fill=BOTH, expand=1)

    transaction_scroll_x = Scrollbar(transaction_frame, orient=HORIZONTAL)
    transaction_scroll_y = Scrollbar(transaction_frame, orient=VERTICAL)

    transaction_table = ttk.Treeview(transaction_frame, columns=(
         'TransactionID' , 'TransactionType' , 'Date'       , 'Amount' , 'Description'              , 'OrderID'
    ),
        xscrollcommand=transaction_scroll_x.set,
        yscrollcommand=transaction_scroll_y.set)

    transaction_scroll_x.config(command=transaction_table.xview)
    transaction_scroll_y.config(command=transaction_table.yview)

    transaction_scroll_x.pack(side=BOTTOM, fill=X)
    transaction_scroll_y.pack(side=RIGHT, fill=Y)

    transaction_table.pack(fill=BOTH, expand=1)

    transaction_table.heading('TransactionID', text='TransactionID')
    transaction_table.heading('TransactionType', text='TransactionType')
    transaction_table.heading('Date', text='Date')
    transaction_table.heading('Amount', text='Amount')
    transaction_table.heading('Description', text='Description')
    transaction_table.heading('OrderID', text='OrderID')

    transaction_table.column('TransactionID', width=20, anchor=CENTER)
    transaction_table.column('TransactionType', width=60, anchor=CENTER)
    transaction_table.column('Date', width=60, anchor=CENTER)
    transaction_table.column('Amount', width=60, anchor=CENTER)
    transaction_table.column('Description', width=60, anchor=CENTER)
    transaction_table.column('OrderID', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    transaction_table.config(show='headings')

    query='SELECT * FROM transactions'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        transaction_table.insert('',END,values=data_list)