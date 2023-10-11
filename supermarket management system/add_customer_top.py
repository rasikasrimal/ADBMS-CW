from tkinter import *
from tkinter import ttk

def toplevel_date(title, button_text, command):
    global idEntry, mobileEntry, nameEntry, emailEntry, addressEntry, genderEntry, dobEntry, screen
    screen = Toplevel()
    screen.grab_set()
    screen.title('Update Student')
    screen.resizable(False, False)
    idlable = Label(screen, text='ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(screen, text='Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobilelable = Label(screen, text='Mobile', font=('Helvetica', 15, 'bold'))
    mobilelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mobileEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emaillable = Label(screen, text='Email', font=('Helvetica', 15, 'bold'))
    emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    emailEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addresslable = Label(screen, text='Address', font=('Helvetica', 15, 'bold'))
    addresslable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    addressEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderlable = Label(screen, text='Gender', font=('Helvetica', 15, 'bold'))
    genderlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    genderEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    doblable = Label(screen, text='DOB', font=('Helvetica', 15, 'bold'))
    doblable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    dobEntry = Entry(screen, font=('Helvetica', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    student_button = ttk.Button(screen, text=button_text, width=25, command=command)
    student_button.grid(row=9, columnspan=2, padx=10, pady=10)

    if title == 'Update Student':
        indexing=student_table.focus()

        content=student_table.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        mobileEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])