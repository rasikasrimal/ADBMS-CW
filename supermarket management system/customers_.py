from tkinter import *
from tkinter import ttk


def open_customers__window(root, mycursor):
    customers__window = Toplevel(root)
    customers__window.title('customers_ Data')
    customers__window.geometry('800x550')

    customers__frame = Frame(customers__window, bg='white', relief=RIDGE)
    customers__frame.pack(fill=BOTH, expand=1)

    customers__scroll_x = Scrollbar(customers__frame, orient=HORIZONTAL)
    customers__scroll_y = Scrollbar(customers__frame, orient=VERTICAL)

    customers__table = ttk.Treeview(customers__frame, columns=(
        'Customers_ID', 'Count'
    ),
        xscrollcommand=customers__scroll_x.set,
        yscrollcommand=customers__scroll_y.set)

    customers__scroll_x.config(command=customers__table.xview)
    customers__scroll_y.config(command=customers__table.yview)

    customers__scroll_x.pack(side=BOTTOM, fill=X)
    customers__scroll_y.pack(side=RIGHT, fill=Y)

    customers__table.pack(fill=BOTH, expand=1)


    customers__table.heading('Customers_ID', text='customersID')
    customers__table.heading('Count', text='EmployeeID')

    customers__table.column('Customers_ID', width=20, anchor=CENTER)
    customers__table.column('Count', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    customers__table.config(show='headings')

    query='''
    select v.customer_id, count(*) AS count
    from visits as v
    left join transactions as t
    on v.visit_id = t.visit_id
    where t.transactionid IS NULL
    GROUP BY v.customer_id;
    '''
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        customers__table.insert('',END,values=data_list)