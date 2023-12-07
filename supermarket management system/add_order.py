def add_order():
    # Function to handle add order window submit button click
    def add_order_submit():
        order_date = orderDateEntry.get()
        total_amount = orderTotalAmountEntry.get()
        payment_method = orderPaymentMethodEntry.get()
        payment_date = orderPaymentDateEntry.get()
        customer_id = orderCustomerIdEntry.get()

        # Add order details to the database
        try:
            query = 'INSERT INTO orders (order_date, total_amount, payment_method, payment_date, customer_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
            values = (order_date, total_amount, payment_method, payment_date, customer_id)
            mycursor.execute(query, values)
            con.commit()
            messagebox.showinfo('Success', 'Order added successfully')
            add_order_window.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    add_order_window = Toplevel(root)
    add_order_window.grab_set()
    add_order_window.title('Add Order')
    add_order_window.geometry('500x400+500+200')
    add_order_window.resizable(False, False)

    orderDateLabel = Label(add_order_window, text='Order Date', font=('Helvetica', 15, 'bold'))
    orderDateLabel.grid(row=0, column=0, padx=10, pady=10)

    orderDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderDateEntry.grid(row=0, column=1, padx=10, pady=10)

    orderTotalAmountLabel = Label(add_order_window, text='Total Amount', font=('Helvetica', 15, 'bold'))
    orderTotalAmountLabel.grid(row=1, column=0, padx=10, pady=10)

    orderTotalAmountEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderTotalAmountEntry.grid(row=1, column=1, padx=10, pady=10)

    orderPaymentMethodLabel = Label(add_order_window, text='Payment Method', font=('Helvetica', 15, 'bold'))
    orderPaymentMethodLabel.grid(row=2, column=0, padx=10, pady=10)

    orderPaymentMethodEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentMethodEntry.grid(row=2, column=1, padx=10, pady=10)

    orderPaymentDateLabel = Label(add_order_window, text='Payment Date', font=('Helvetica', 15, 'bold'))
    orderPaymentDateLabel.grid(row=3, column=0, padx=10, pady=10)

    orderPaymentDateEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderPaymentDateEntry.grid(row=3, column=1, padx=10, pady=10)

    orderCustomerIdLabel = Label(add_order_window, text='Customer ID', font=('Helvetica', 15, 'bold'))
    orderCustomerIdLabel.grid(row=4, column=0, padx=10, pady=10)

    orderCustomerIdEntry = Entry(add_order_window, font=('Helvetica', 15, 'bold'))
    orderCustomerIdEntry.grid(row=4, column=1, padx=10, pady=10)

    submitButton = ttk.Button(add_order_window, text='Submit', command=add_order_submit)
    submitButton.grid(row=5, column=0, columnspan=2, pady=10)
