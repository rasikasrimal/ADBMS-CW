from tkinter import *
from tkinter import ttk


def open_sale_window(root, mycursor):
    sale_window = Toplevel(root)
    sale_window.title('sale Data')
    sale_window.geometry('800x550')

    sale_frame = Frame(sale_window, bg='white', relief=RIDGE)
    sale_frame.pack(fill=BOTH, expand=1)

    sale_scroll_x = Scrollbar(sale_frame, orient=HORIZONTAL)
    sale_scroll_y = Scrollbar(sale_frame, orient=VERTICAL)

    sale_table = ttk.Treeview(sale_frame, columns=(
        'SaleID', 'EmployeeID',  'SaleDate','TotalSalesAmount'
    ),
        xscrollcommand=sale_scroll_x.set,
        yscrollcommand=sale_scroll_y.set)

    sale_scroll_x.config(command=sale_table.xview)
    sale_scroll_y.config(command=sale_table.yview)

    sale_scroll_x.pack(side=BOTTOM, fill=X)
    sale_scroll_y.pack(side=RIGHT, fill=Y)

    sale_table.pack(fill=BOTH, expand=1)


    sale_table.heading('SaleID', text='saleID')
    sale_table.heading('EmployeeID', text='EmployeeID')
    sale_table.heading('SaleDate', text='saleDate')
    sale_table.heading('TotalSalesAmount', text='TotalSalesAmount')

    sale_table.column('SaleID', width=20, anchor=CENTER)
    sale_table.column('EmployeeID', width=60, anchor=CENTER)
    sale_table.column('SaleDate', width=60, anchor=CENTER)
    sale_table.column('TotalSalesAmount', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    sale_table.config(show='headings')

    query='SELECT * FROM sales'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        sale_table.insert('',END,values=data_list)