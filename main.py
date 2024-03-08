import tkinter 
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List App")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        # clear the entry after inserting a task in the listbox
        entry_task.delete(0, tkinter.END)
    else: 
        tkinter.messagebox.showwarning(title="Warning", message="You must enter a task.")

def delete_tasks():
    tasks_index = listbox_tasks.curselection()
    if len(tasks_index) == 0:
        tkinter.messagebox.showwarning(title="Warning", message="You must select a task.")

    for index in tasks_index[::-1]:
        listbox_tasks.delete(index)

def load_tasks():
    try:
        # load tasks from "tasks.txt" and insert them
        tasks = pickle.load(open("tasks.txt", "rb"))
        # this line delete the tasks from listbox, without it, if we load another time
        # the tasks it will reload the same tasks for many times as many we click load
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning", message="Cannot find tasks.txt")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    if len(tasks) == 0:
        tkinter.messagebox.showwarning(title="Warning", message="There are no tasks in the list.")
    else :
        # save tasks in a file named "tasks.txt"
        pickle.dump(tasks, open("tasks.txt", "wb"))

# GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, selectmode="multiple")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# this two instruction make the scrollbar work
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# input
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_tasks = tkinter.Button(root, text="Delete task", width=48, command=delete_tasks)
button_delete_tasks.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()


root.mainloop()