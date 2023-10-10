from tkinter import *
from tkinter import ttk


def open_storelocation_window(root, mycursor):
    storelocation_window = Toplevel(root)
    storelocation_window.title('storelocation Data')
    storelocation_window.geometry('800x550')

    storelocation_frame = Frame(storelocation_window, bg='white', relief=RIDGE)
    storelocation_frame.pack(fill=BOTH, expand=1)

    storelocation_scroll_x = Scrollbar(storelocation_frame, orient=HORIZONTAL)
    storelocation_scroll_y = Scrollbar(storelocation_frame, orient=VERTICAL)

    storelocation_table = ttk.Treeview(storelocation_frame, columns=(
        'StoreID' ,'StoreName'  , 'Address', 'Phone'  ,  'Manager' , 'OpeningDate'
    ),
        xscrollcommand=storelocation_scroll_x.set,
        yscrollcommand=storelocation_scroll_y.set)

    storelocation_scroll_x.config(command=storelocation_table.xview)
    storelocation_scroll_y.config(command=storelocation_table.yview)

    storelocation_scroll_x.pack(side=BOTTOM, fill=X)
    storelocation_scroll_y.pack(side=RIGHT, fill=Y)

    storelocation_table.pack(fill=BOTH, expand=1)

    storelocation_table.heading('StoreID', text='StoreID')
    storelocation_table.heading('StoreName', text='StoreName')
    storelocation_table.heading('Address', text='Address')
    storelocation_table.heading('Phone', text='Phone')
    storelocation_table.heading('Manager', text='Manager')
    storelocation_table.heading('OpeningDate', text='OpeningDate')

    storelocation_table.column('StoreID', width=20, anchor=CENTER)
    storelocation_table.column('StoreName', width=60, anchor=CENTER)
    storelocation_table.column('Address', width=60, anchor=CENTER)
    storelocation_table.column('Phone', width=60, anchor=CENTER)
    storelocation_table.column('Manager', width=60, anchor=CENTER)
    storelocation_table.column('OpeningDate', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    storelocation_table.config(show='headings')

    query='SELECT * FROM storelocations'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        storelocation_table.insert('',END,values=data_list)