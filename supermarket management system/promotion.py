from tkinter import *
from tkinter import ttk


def open_promotion_window(root, mycursor):
    promotion_window = Toplevel(root)
    promotion_window.title('promotion Data')
    promotion_window.geometry('800x550')

    promotion_frame = Frame(promotion_window, bg='white', relief=RIDGE)
    promotion_frame.pack(fill=BOTH, expand=1)

    promotion_scroll_x = Scrollbar(promotion_frame, orient=HORIZONTAL)
    promotion_scroll_y = Scrollbar(promotion_frame, orient=VERTICAL)

    promotion_table = ttk.Treeview(promotion_frame, columns=(
        'PromotionID', 'Name', 'Description', 'StartDate', 'EndDate', 'DiscountPercentage'
    ),
        xscrollcommand=promotion_scroll_x.set,
        yscrollcommand=promotion_scroll_y.set)

    promotion_scroll_x.config(command=promotion_table.xview)
    promotion_scroll_y.config(command=promotion_table.yview)

    promotion_scroll_x.pack(side=BOTTOM, fill=X)
    promotion_scroll_y.pack(side=RIGHT, fill=Y)

    promotion_table.pack(fill=BOTH, expand=1)

    promotion_table.heading('PromotionID', text='promotionID')
    promotion_table.heading('Name', text='Name')
    promotion_table.heading('Description', text='Description')
    promotion_table.heading('StartDate', text='StartDate')
    promotion_table.heading('EndDate', text='EndDate')
    promotion_table.heading('DiscountPercentage', text='DiscountPercentage')

    promotion_table.column('PromotionID', width=20, anchor=CENTER)
    promotion_table.column('Name', width=60, anchor=CENTER)
    promotion_table.column('Description', width=60, anchor=CENTER)
    promotion_table.column('StartDate', width=60, anchor=CENTER)
    promotion_table.column('EndDate', width=60, anchor=CENTER)
    promotion_table.column('DiscountPercentage', width=60, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('Helvetica', 10), foreground='black', background='white', fieldbackground='white')
    style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), foreground='black', background='light green', fieldbackground='grey')
    promotion_table.config(show='headings')

    query='SELECT * FROM promotions'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()

    for data in fetched_data:
        data_list=list(data)
        promotion_table.insert('',END,values=data_list)