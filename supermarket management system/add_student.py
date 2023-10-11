from tkinter import *
from tkinter import ttk


def add_data():
    if (
        idEntry.get() == '' or
        nameEntry.get() == '' or
        mobileEntry.get() == '' or
        emailEntry.get() == '' or
        addressEntry.get() == '' or
        genderEntry.get() == '' or
        dobEntry.get() == ''
    ):
        messagebox.showerror('Error', 'All fields are required', parent=screen)
    else:
        query = 'INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            mycursor.execute(query, (
                idEntry.get(),
                nameEntry.get(),
                mobileEntry.get(),
                emailEntry.get(),
                addressEntry.get(), 
                genderEntry.get(), 
                dobEntry.get(), 
                currentdate,
                currenttime
            ))
            con.commit()
            result = messagebox.askyesnocancel('Success', 'Do you want to clear the form?')
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                mobileEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', 'This ID is already taken', parent=screen)
            return

        query = 'SELECT * FROM student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            data_list = list(data)
            student_table.insert('', END, values=data_list)