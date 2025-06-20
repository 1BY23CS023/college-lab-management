from login import show_login
from equipment import equipment_window
from issue_return import issue_return_window
from reports import show_reports
import tkinter as tk

def dashboard():
    win = tk.Tk()
    win.title("Lab Management Dashboard")

    tk.Button(win, text="Manage Equipment", width=25, command=equipment_window).pack(pady=5)
    tk.Button(win, text="Issue/Return Equipment", width=25, command=issue_return_window).pack(pady=5)
    tk.Button(win, text="View Issued Report", width=25, command=show_reports).pack(pady=5)

    win.mainloop()

if __name__ == "__main__":
    show_login(dashboard)
