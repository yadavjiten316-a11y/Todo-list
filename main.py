import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                tasks.append(task.strip())
                listbox.insert(tk.END, task.strip())
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks)
save_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

load_tasks()

root.mainloop()
