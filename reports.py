import tkinter as tk
from tkinter import ttk
from db import connect_db

def show_reports():
    win = tk.Tk()
    win.title("Issued Equipment Report")

    tree = ttk.Treeview(win, columns=("ID", "Equip ID", "Issued To", "Issue Date", "Return Date"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM issued_equipment")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()
