import os
import django
import tkinter as tk
from tkinter import messagebox

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from inventory.models import Employee

def add_employee():
    name = name_entry.get().strip()
    position = position_entry.get().strip()
    
    if name and position:
        Employee.objects.create(name=name, position=position)
        messagebox.showinfo("Success", f"Successfully added {name} ({position})!")
        name_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please fill in all fields!")

root = tk.Tk()
root.title("Employee Management System - Milestone 2")
root.geometry("350x230")

tk.Label(root, text="Employee Name:").pack(pady=(15, 2))
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=2)

tk.Label(root, text="Position:").pack(pady=(10, 2))
position_entry = tk.Entry(root, width=35)
position_entry.pack(pady=2)

add_btn = tk.Button(root, text="Add Employee", command=add_employee)
add_btn.pack(pady=15)

root.mainloop()