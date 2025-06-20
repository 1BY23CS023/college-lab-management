from tkinter import *
from tkinter import messagebox
from db import connect_db
import datetime

def issue_return_window():
    win = Tk()
    win.title("Issue / Return Equipment")

    def issue():
        eq_id = entry_id.get()
        user = entry_user.get()
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE equipment SET status='issued' WHERE equipment_id=%s", (eq_id,))
        cur.execute("INSERT INTO issued_equipment (equipment_id, issued_to, issue_date) VALUES (%s, %s, %s)", 
                    (eq_id, user, datetime.date.today()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Equipment Issued")

    def return_eq():
        eq_id = entry_id.get()
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE equipment SET status='available' WHERE equipment_id=%s", (eq_id,))
        cur.execute("UPDATE issued_equipment SET return_date=%s WHERE equipment_id=%s AND return_date IS NULL", 
                    (datetime.date.today(), eq_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Equipment Returned")

    Label(win, text="Equipment ID").pack()
    entry_id = Entry(win)
    entry_id.pack()

    Label(win, text="Issued To").pack()
    entry_user = Entry(win)
    entry_user.pack()

    Button(win, text="Issue", command=issue).pack()
    Button(win, text="Return", command=return_eq).pack()


