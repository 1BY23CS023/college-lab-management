import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db

def equipment_window():
    win = tk.Tk()
    win.title("Equipment Management")

    def add_equipment():
        name = entry.get()
        if name:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO equipment (name) VALUES (%s)", (name,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Added", f"{name} added")
            entry.delete(0, tk.END)
            refresh()

    def remove_equipment():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an equipment to remove.")
            return
        values = tree.item(selected_item, 'values')
        eq_id = values[0]


         
        
        confirm = messagebox.askyesno("Confirm Delete", f"Delete equipment ID {eq_id}?")
        if confirm:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM equipment WHERE equipment_id = %s", (eq_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Equipment deleted.")
            refresh()

    def refresh():
        for i in tree.get_children():
            tree.delete(i)
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM equipment")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    # UI Layout
    tk.Label(win, text="Equipment Name").pack()
    entry = tk.Entry(win)
    entry.pack()

    tk.Button(win, text="Add Equipment", command=add_equipment).pack(pady=5)
    tk.Button(win, text="Remove Selected Equipment", command=remove_equipment).pack(pady=5)

    tree = ttk.Treeview(win, columns=("ID", "Name", "Status"), show='headings')
    for col in ("ID", "Name", "Status"):
        tree.heading(col, text=col)
    tree.pack()
    refresh()


