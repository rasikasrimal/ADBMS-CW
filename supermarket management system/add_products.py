from tkinter import messagebox, ttk, END

def add_product():
    def add_product_data():
        if (
            idEntry.get() == '' or 
            nameEntry.get() == '' or 
            categoryEntry.get() == '' or 
            priceEntry.get() == '' or 
            quantityEntry.get() == '' or 
            profit_per_unitEntry.get() == '' or 
            supplier_idEntry.get() == ''
        ):
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            try:
                # Check if the selected supplier_id exists in the suppliers table
                supplier_id = int(supplier_idEntry.get())
                query = "SELECT supplier_id FROM suppliers WHERE supplier_id = %s;"
                mycursor.execute(query, (supplier_id,))
                if not mycursor.fetchone():
                    messagebox.showerror('Error', 'Invalid supplier_id', parent=add_window)
                    return

                # Insert into products table
                query = '''
                INSERT INTO products (
                    product_id, name, category, 
                    price, stock_quantity, profit_per_unit, supplier_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s);
                '''
                values = (
                    idEntry.get(),
                    nameEntry.get(),
                    categoryEntry.get(),
                    priceEntry.get(),
                    quantityEntry.get(),
                    profit_per_unitEntry.get(),
                    supplier_id
                )
                mycursor.execute(query, values)
                con.commit()

                result = messagebox.askyesno('Confirm', 'Do you want to clear the form?')
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    categoryEntry.delete(0, END)
                    priceEntry.delete(0, END)
                    quantityEntry.delete(0, END)
                    profit_per_unitEntry.delete(0, END)
                    supplier_idEntry.set('')  # Clear the supplier_id dropdown

            except ValueError:
                messagebox.showerror('Error', 'Invalid input for supplier_id', parent=add_window)

    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(False, False)

    idlable = Label(add_window, text='Product ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(add_window, text='Product Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    categorylable = Label(add_window, text='Category', font=('Helvetica', 15, 'bold'))
    categorylable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    categoryEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    categoryEntry.grid(row=2, column=1, padx=10, pady=10)

    pricelable = Label(add_window, text='Price', font=('Helvetica', 15, 'bold'))
    pricelable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    priceEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    priceEntry.grid(row=3, column=1, padx=10, pady=10)

    quantitylable = Label(add_window, text='Quantity', font=('Helvetica', 15, 'bold'))
    quantitylable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    quantityEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    quantityEntry.grid(row=4, column=1, padx=10, pady=10)

    profit_per_unitlable = Label(add_window, text='Profit per Unit', font=('Helvetica', 15, 'bold'))
    profit_per_unitlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    profit_per_unitEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), width=24)
    profit_per_unitEntry.grid(row=5, column=1, padx=10, pady=10)

    supplier_idlable = Label(add_window, text='Supplier ID', font=('Helvetica', 15, 'bold'))
    supplier_idlable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    supplier_idEntry = ttk.Combobox(add_window, font=('Helvetica', 15, 'bold'), state='readonly', width=22)
    supplier_idEntry.grid(row=6, column=1, padx=10, pady=10)

    # Populate the supplier_id dropdown
    mycursor.execute("SELECT supplier_id FROM suppliers;")
    suppliers = mycursor.fetchall()
    supplier_ids = [str(s[0]) for s in suppliers]
    supplier_idEntry['values'] = supplier_ids

    add_button = Button(add_window, text='Add Product', font=('Helvetica', 15, 'bold'), command=add_product_data)
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

    add_window.mainloop()