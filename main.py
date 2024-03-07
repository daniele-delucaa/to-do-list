import tkinter 
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List App")

def add_task():
    pass

# GUI
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

# input
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add a task", width=48, command=add_task)
button_add_task.pack()

root.mainloop()