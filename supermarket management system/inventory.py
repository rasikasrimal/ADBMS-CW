from tkinter import *
from tkinter import ttk


def open_inventory_window(root, mycursor):
    inventory_window = Toplevel(root)
    inventory_window.title('inventory Data')
    inventory_window.geometry('800x550')

    inventory_frame = Frame(inventory_window, bg='white', relief=RIDGE)
    inventory_frame.pack(fill=BOTH, expand=1)

    inventory_scroll_x = Scrollbar(inventory_frame, orient=HORIZONTAL)
    inventory_scroll_y = Scrollbar(inventory_frame, orient=VERTICAL)

    inventory_table = ttk.Treeview(inventory_frame, columns=(
        'InventoryID', 'ProductID', 'StockQuantity', 'RestockThreshold'
    ),
        xscrollcommand=inventory_scroll_x.set,
        yscrollcommand=inventory_scroll_y.set)

    inventory_scroll_x.config(command=inventory_table.xview)
    inventory_scroll_y.config(command=inventory_table.yview)

    inventory_scroll_x.pack(side=BOTTOM, fill=X)
    inventory_scroll_y.pack(side=RIGHT, fill=Y)

    inventory_table.pack(fill=BOTH, expand=1)

    inventory_table.heading('InventoryID', text='InventoryID')
    inventory_table.heading('ProductID', text='ProductID')
    inventory_table.heading('StockQuantity', text='StockQuantity')
    inventory_table.heading('RestockThreshold', text='RestockThreshold')

    inventory_table.column('InventoryID', width=20, anchor=CENTER)
    inventory_table.column('ProductID', width=60, anchor=CENTER)
    inventory_table.column('StockQuantity', width=60, anchor=CENTER)
    inventory_table.column('RestockThreshold', width=60, anchor=CENTER)
    
    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    inventory_table.config(show='headings')

    query='SELECT * FROM inventory'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        inventory_table.insert('',END,values=data_list)