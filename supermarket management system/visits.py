from tkinter import *
from tkinter import ttk


def open_visit_window(root, mycursor):
    visit_window = Toplevel(root)
    visit_window.title('visit Data')
    visit_window.geometry('800x550')

    visit_frame = Frame(visit_window, bg='white', relief=RIDGE)
    visit_frame.pack(fill=BOTH, expand=1)

    visit_scroll_x = Scrollbar(visit_frame, orient=HORIZONTAL)
    visit_scroll_y = Scrollbar(visit_frame, orient=VERTICAL)

    visit_table = ttk.Treeview(visit_frame, columns=(
        'visit_id', 'customer_id'
    ),
        xscrollcommand=visit_scroll_x.set,
        yscrollcommand=visit_scroll_y.set)

    visit_scroll_x.config(command=visit_table.xview)
    visit_scroll_y.config(command=visit_table.yview)

    visit_scroll_x.pack(side=BOTTOM, fill=X)
    visit_scroll_y.pack(side=RIGHT, fill=Y)

    visit_table.pack(fill=BOTH, expand=1)

    visit_table.heading('visit_id', text='visitID')
    visit_table.heading('customer_id', text='CustomerID')

    visit_table.column('visit_id', width=20, anchor=CENTER)
    visit_table.column('customer_id', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    visit_table.config(show='headings')

    query='SELECT * FROM visits'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        visit_table.insert('',END,values=data_list)