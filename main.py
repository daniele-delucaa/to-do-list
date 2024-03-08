import tkinter 
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List App")

t_index, colors_index = 0, 0

def add_task():
    global t_index, colors_index
    tasks_colors = ["#fbbc08", "#f9dc71", "#d09404", "#9d8269", "#aac9da"]
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        # clear the entry after inserting a task in the listbox
        entry_task.delete(0, tkinter.END)

        listbox_tasks.itemconfig(t_index,{"bg":tasks_colors[colors_index]})
        t_index += 1
        colors_index += 1
        if colors_index == 5:
            colors_index = 0
    else: 
        tkinter.messagebox.showwarning(title="Warning", message="You must enter a task.")

def delete_tasks():
    global t_index
    tasks_index = listbox_tasks.curselection()
    if len(tasks_index) == 0:
        tkinter.messagebox.showwarning(title="Warning", message="You must select a task.")

    for index in tasks_index[::-1]:
        listbox_tasks.delete(index)
        t_index -= 1

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

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=50, selectmode="multiple", justify="center", font="ubuntu")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# this two instruction make the scrollbar work
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# input
entry_task = tkinter.Entry(root, width=30, font="ubuntu")
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=20, command=add_task, font="ubuntu")
button_add_task.pack(padx=5, pady=5)

button_delete_tasks = tkinter.Button(root, text="Delete task", width=20, command=delete_tasks, font="ubuntu")
button_delete_tasks.pack(padx=5, pady=5)

button_load_tasks = tkinter.Button(root, text="Load tasks", width=20, command=load_tasks, font="ubuntu")
button_load_tasks.pack(padx=5, pady=5)

button_save_tasks = tkinter.Button(root, text="Save tasks", width=20, command=save_tasks, font="ubuntu")
button_save_tasks.pack(padx=5, pady=5)


root.mainloop()