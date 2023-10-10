from tkinter import *
from tkinter import ttk


def open_supplier_window(root, mycursor):
    supplier_window = Toplevel(root)
    supplier_window.title('supplier Data')
    supplier_window.geometry('800x550')

    supplier_frame = Frame(supplier_window, bg='white', relief=RIDGE)
    supplier_frame.pack(fill=BOTH, expand=1)

    supplier_scroll_x = Scrollbar(supplier_frame, orient=HORIZONTAL)
    supplier_scroll_y = Scrollbar(supplier_frame, orient=VERTICAL)

    supplier_table = ttk.Treeview(supplier_frame, columns=(
        'SupplierID', 'SupplierName' , 'ContactPerson' ,'Email' ,'Phone','Address'
    ),
        xscrollcommand=supplier_scroll_x.set,
        yscrollcommand=supplier_scroll_y.set)

    supplier_scroll_x.config(command=supplier_table.xview)
    supplier_scroll_y.config(command=supplier_table.yview)

    supplier_scroll_x.pack(side=BOTTOM, fill=X)
    supplier_scroll_y.pack(side=RIGHT, fill=Y)

    supplier_table.pack(fill=BOTH, expand=1)

    supplier_table.heading('SupplierID', text='SupplierID')
    supplier_table.heading('SupplierName', text='SupplierName')
    supplier_table.heading('ContactPerson', text='ContactPerson')
    supplier_table.heading('Email', text='Email')
    supplier_table.heading('Phone', text='Phone')
    supplier_table.heading('Address', text='Address')

    supplier_table.column('SupplierID', width=20, anchor=CENTER)
    supplier_table.column('SupplierName', width=60, anchor=CENTER)
    supplier_table.column('ContactPerson', width=60, anchor=CENTER)
    supplier_table.column('Email', width=60, anchor=CENTER)
    supplier_table.column('Phone', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    supplier_table.config(show='headings')

    query='SELECT * FROM suppliers'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        supplier_table.insert('',END,values=data_list)