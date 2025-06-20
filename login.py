import tkinter as tk
from tkinter import messagebox
from db import connect_db

def show_login(callback):
    def login():
        uname = username.get()
        pwd = password.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (uname, pwd))
        result = cursor.fetchone()
        conn.close()

        if result:
            login_win.destroy()
            callback()
        else:
            messagebox.showerror("Login Failed", "Invalid Credentials")

    login_win = tk.Tk()
    login_win.title("Admin Login")
    tk.Label(login_win, text="Username").pack()
    username = tk.Entry(login_win)
    username.pack()

    tk.Label(login_win, text="Password").pack()
    password = tk.Entry(login_win, show='*')
    password.pack()

    tk.Button(login_win, text="Login", command=login).pack()
    login_win.mainloop()
