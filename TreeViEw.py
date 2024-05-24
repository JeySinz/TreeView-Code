from tkinter import*
from tkinter import ttk
import sqlite3



root=Tk()
root.title('Tree')
root.geometry('500x500')

frm=Frame(root,width=400,height=400)
frm.place(x=50,y=20)
my_tree=ttk.Treeview(frm)

my_tree['columns']=('Name','Contact','City')

my_tree.column('#0',width=12)
my_tree.column('Name',anchor=W,width=120,minwidth=70)
my_tree.column('Contact',anchor=CENTER,width=120)
my_tree.column('City',anchor=W,width=120)

my_tree.heading('#0',text='',anchor=W)
my_tree.heading('Name',text='Name',anchor=W)
my_tree.heading('Contact',text='Contact',anchor=CENTER)
my_tree.heading('City',text='City',anchor=W)

my_tree.insert(parent='',index='end',iid=0,text='',value=('Bruce Wayne',99225,'Gotham'))
my_tree.pack()

root.mainloop()
