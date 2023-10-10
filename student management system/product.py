from tkinter import *
from tkinter import ttk


def open_product_window(root, mycursor):
    product_window = Toplevel(root)
    product_window.title('Product Data')
    product_window.geometry('800x550')

    product_frame = Frame(product_window, bg='white', relief=RIDGE)
    product_frame.pack(fill=BOTH, expand=1)

    product_scroll_x = Scrollbar(product_frame, orient=HORIZONTAL)
    product_scroll_y = Scrollbar(product_frame, orient=VERTICAL)

    product_table = ttk.Treeview(product_frame, columns=(
        'ProductID', 'Name', 'Category', 'Discription', 'Price', 'StockQuantity', 'SupplierID'),
        xscrollcommand=product_scroll_x.set,
        yscrollcommand=product_scroll_y.set)

    product_scroll_x.config(command=product_table.xview)
    product_scroll_y.config(command=product_table.yview)

    product_scroll_x.pack(side=BOTTOM, fill=X)
    product_scroll_y.pack(side=RIGHT, fill=Y)

    product_table.pack(fill=BOTH, expand=1)

    product_table.heading('ProductID', text='ProductID')
    product_table.heading('Name', text='Name')
    product_table.heading('Category', text='Category')
    product_table.heading('Discription', text='Discription')
    product_table.heading('Price', text='Price')
    product_table.heading('StockQuantity', text='StockQuantity')
    product_table.heading('SupplierID', text='SupplierID')

    product_table.column('ProductID', width=20, anchor=CENTER)
    product_table.column('Name', width=60, anchor=CENTER)
    product_table.column('Category', width=60, anchor=CENTER)
    product_table.column('Discription', width=60, anchor=CENTER)
    product_table.column('Price', width=60, anchor=CENTER)
    product_table.column('StockQuantity', width=60, anchor=CENTER)
    product_table.column('SupplierID', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    product_table.config(show='headings')

    query='SELECT * FROM products'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        product_table.insert('',END,values=data_list)