from tkinter import *
from tkinter import ttk


def open_employee_window(root, mycursor):
    employee_window = Toplevel(root)
    employee_window.title('employee Data')
    employee_window.geometry('800x550')

    employee_frame = Frame(employee_window, bg='white', relief=RIDGE)
    employee_frame.pack(fill=BOTH, expand=1)

    employee_scroll_x = Scrollbar(employee_frame, orient=HORIZONTAL)
    employee_scroll_y = Scrollbar(employee_frame, orient=VERTICAL)

    employee_table = ttk.Treeview(employee_frame, columns=(
        'employeeID', 'CustomerID', 'employeeDate', 'TotalAmount', 'PaymentMethod', 'PaymentDate'
    ),
        xscrollcommand=employee_scroll_x.set,
        yscrollcommand=employee_scroll_y.set)

    employee_scroll_x.config(command=employee_table.xview)
    employee_scroll_y.config(command=employee_table.yview)

    employee_scroll_x.pack(side=BOTTOM, fill=X)
    employee_scroll_y.pack(side=RIGHT, fill=Y)

    employee_table.pack(fill=BOTH, expand=1)

    employee_table.heading('employeeID', text='employeeID')
    employee_table.heading('CustomerID', text='CustomerID')
    employee_table.heading('employeeDate', text='employeeDate')
    employee_table.heading('TotalAmount', text='TotalAmount')
    employee_table.heading('PaymentMethod', text='PaymentMethod')
    employee_table.heading('PaymentDate', text='PaymentDate')

    employee_table.column('employeeID', width=20, anchor=CENTER)
    employee_table.column('CustomerID', width=60, anchor=CENTER)
    employee_table.column('employeeDate', width=60, anchor=CENTER)
    employee_table.column('TotalAmount', width=60, anchor=CENTER)
    employee_table.column('PaymentMethod', width=60, anchor=CENTER)
    employee_table.column('PaymentDate', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    employee_table.config(show='headings')

    query='SELECT * FROM employees'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        employee_table.insert('',END,values=data_list)