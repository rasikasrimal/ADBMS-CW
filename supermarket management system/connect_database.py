from tkinter import *
from tkinter import ttk, messagebox
import pymysql

def connect_database():

    # Function to handle connect button click
    def connect():
        try:
            # Connect to the MySQL server
            con = pymysql.connect(
                host=hostEntry.get(),
                user=userEntry.get(),
                password=PasswordEntry.get(),
                database='supermarket'  # Specify the database name
            )

            mycursor = con.cursor()
            
            # Check if the required tables exist, create them if not
            create_tables_query = '''
                CREATE TABLE IF NOT EXISTS employee (
                    employee_id INT NOT NULL PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    phone VARCHAR(15) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    salary DECIMAL(10,2) NOT NULL,
                    position_id INT,
                    exp_id INT,
                    hire_date DATE NOT NULL
                );

                CREATE TABLE IF NOT EXISTS experience (
                    exp_id INT NOT NULL PRIMARY KEY,
                    exp_level VARCHAR(255) NOT NULL,
                    exp_factor DECIMAL(10,2) NOT NULL
                );

                CREATE TABLE IF NOT EXISTS inventory (
                    inventory_id INT NOT NULL PRIMARY KEY,
                    stock_quantity INT NOT NULL,
                    restock_threshold INT NOT NULL,
                    product_id INT
                );

                -- Add other table creation queries here...

                '''

            mycursor.execute(create_tables_query)

            # Commit changes and close the connection
            con.commit()
            con.close()

            messagebox.showinfo('Success', 'Connected to Database')
            connectWindow.destroy()

            # Enable buttons after successful connection
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            updatestudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            exportDataButton.config(state=NORMAL)
            deletestudentButton.config(state=NORMAL)

        except Exception as e:
            messagebox.showerror('Error', f'Error connecting to the database: {e}')

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.title('Connect Database')
    connectWindow.geometry('500x300+500+200')
    connectWindow.resizable(False, False)

    hostnameLabel = Label(connectWindow, text='Hostname', font=('Helvetica', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=10, pady=10)

    hostEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'))
    hostEntry.grid(row=0, column=1, padx=10, pady=10)

    usernameLabel = Label(connectWindow, text='Username', font=('Helvetica', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)

    userEntry = Entry(connectWindow, font=('Username', 15, 'bold'))
    userEntry.grid(row=1, column=1, padx=10, pady=10)

    PasswordLabel = Label(connectWindow, text='Password', font=('Helvetica', 15, 'bold'))
    PasswordLabel.grid(row=2, column=0, padx=10, pady=10)

    PasswordEntry = Entry(connectWindow, font=('Password', 15, 'bold'))
    PasswordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton=ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, column=0, padx=10, pady=10)

# Add the rest of your GUI code here...

# Create the main Tkinter window
root = Tk()
root.title('Your Application Title')

# Add the rest of your GUI code here...

# Start the Tkinter event loop
root.mainloop()
