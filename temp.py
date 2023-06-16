import tkinter
from tkinter import *

root=Tk()
root.title("ToDo List")
root.geometry("400x650+400+10")
root.resizable(100,100)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def openTask():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()

def deltask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        
        listbox.delete(ANCHOR)

#icon
img_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,img_icon)


#top bar
barimg=PhotoImage(file="Image/topbar.png")
Label(root,image=barimg).pack()

dockimg=PhotoImage(file="Image/dock.png")
Label(root,image=dockimg,bg="#32405b").place(x=30,y=25)

noteimg=PhotoImage(file="Image/task.png")
Label(root,image=noteimg,bg="#32405b").place(x=30,y=25)

heading=Label(root,text="ALL TASK", font="arial 20 bold",fg="white", bg="#32405b")
heading.place(x=130,y=20)

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD", width=6,font="arial 20",bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=frame=Frame(root,width=700,height=280,bg="#32405b",bd=3)
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial', 12) ,width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTask()


#delete

delicon=PhotoImage(file="Image/delete.png")
Button(root,image=delicon,bd=0,command=deltask).pack(side=BOTTOM,pady=13)



root.mainloop()