import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do")

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

add_button = tk.Button(root, text="Add", command=add_task, font=("Helvetica", 12))
add_button.pack(padx=20)

task_list = tk.Listbox(root, selectbackground="lightblue", selectmode=tk.SINGLE, font=("Helvetica", 14))
task_list.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

delete_button = tk.Button(root, text="Delete", command=delete_task, font=("Helvetica", 12))
delete_button.pack(padx=20)

root.mainloop()
