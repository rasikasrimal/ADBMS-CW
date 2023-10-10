from tkinter import *
from tkinter import ttk


def open_promotionusage_window(root, mycursor):
    promotionusage_window = Toplevel(root)
    promotionusage_window.title('promotionusage Data')
    promotionusage_window.geometry('800x550')

    promotionusage_frame = Frame(promotionusage_window, bg='white', relief=RIDGE)
    promotionusage_frame.pack(fill=BOTH, expand=1)

    promotionusage_scroll_x = Scrollbar(promotionusage_frame, orient=HORIZONTAL)
    promotionusage_scroll_y = Scrollbar(promotionusage_frame, orient=VERTICAL)

    promotionusage_table = ttk.Treeview(promotionusage_frame, columns=(
        'UsageID', 'PromotionID', 'OrderID'
    ),
        xscrollcommand=promotionusage_scroll_x.set,
        yscrollcommand=promotionusage_scroll_y.set)

    promotionusage_scroll_x.config(command=promotionusage_table.xview)
    promotionusage_scroll_y.config(command=promotionusage_table.yview)

    promotionusage_scroll_x.pack(side=BOTTOM, fill=X)
    promotionusage_scroll_y.pack(side=RIGHT, fill=Y)

    promotionusage_table.pack(fill=BOTH, expand=1)

    promotionusage_table.heading('UsageID', text='UsageID')
    promotionusage_table.heading('PromotionID', text='PromotionID')
    promotionusage_table.heading('OrderID', text='OrderID')


    promotionusage_table.column('UsageID', width=20, anchor=CENTER)
    promotionusage_table.column('PromotionID', width=60, anchor=CENTER)
    promotionusage_table.column('OrderID', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    promotionusage_table.config(show='headings')

    query='select * from promotionusage'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        promotionusage_table.insert('',END,values=data_list)