# delete_operations.py

from tkinter import messagebox

def delete_customer(mycursor, con, customer_table):
    indexing = customer_table.focus()
    content = customer_table.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM customer WHERE id=%s'
    mycursor.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('DELETED', f'User {content_id} is DELETED Successfully')
    query = 'SELECT * FROM customer'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    customer_table.delete(*customer_table.get_children())
    for data in fetched_data:
        data_list = list(data)
        customer_table.insert('', 'end', values=data_list)
