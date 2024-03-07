import tkinter 
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List App")

def add_task():
    task = entry_task.get()
    if task != "":
        # insert the string "task" in the listbox
        listbox_tasks.insert(tkinter.END, task)
        # clear the entry after inserting a task in the listbox
        entry_task.delete(0, tkinter.END)
    else: 
        tkinter.messagebox.showwarning(title="Warning", message="You must enter a task.")

# GUI
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(root)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# input
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

root.mainloop()