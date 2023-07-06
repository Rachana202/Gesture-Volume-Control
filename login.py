import tkinter as tk
from tkinter import messagebox
import volcontrol as vc

window = tk.Tk()
window.geometry("1000x1300")

window.title("Login Page")

label_username = tk.Label(window, text="Username:")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password:")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your login logic here
    if username == "admin" and password == "password":
        
        messagebox.showinfo("Login", "Login successful!")
        vc.main()
       
    else:
        messagebox.showerror("Login", "Invalid username or password")

button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

window.mainloop()
