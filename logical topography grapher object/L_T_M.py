#object oriented ver
from tkinter import *

main_window = Tk()
##main_window.geometry("500x100")
Value_frame = LabelFrame(main_window)
Node_frame = LabelFrame(main_window)
N_frame1 = LabelFrame(Node_frame)
N_frame2 = LabelFrame(Node_frame)
N_frame3 = LabelFrame(Node_frame)
C_frame = LabelFrame(main_window)
##Conn_frame = LabelFrame(main_window)
parents = []
children = []
connections = []
def add():
    current_node = [clicked.get() , name.get()]
    #change into vairiable list
    node_list1.insert(END, current_node)
    node_list2.insert(END, current_node)
def set_parent():
    x = node_list1.get(0,END)
    index= node_list1.curselection()
    parent = [x[i] for i in index]
    parents.append(parent)
    print(parents)
def set_child():
    x = node_list2.get(0,END)
    index= node_list2.curselection()
    child = [x[i] for i in index]
    children.append(child)
    print(children)
    
def connection_button():
    #want format [[PARENT,[CHILD,CHILD...],[PARENT[CHILD,CHILD...]ETC]
    x = [parents, children]
    conn_list.insert(END, x)
    print(x)
options = ["switch", "host", "server"]

clicked = StringVar()
clicked.set("Type")

type_menu = OptionMenu(main_window, clicked, *options)


name = Entry(main_window)

Connec_L = Label(C_frame, text = "Connections")

node_list1 = Listbox(N_frame1)
node_list2 = Listbox(N_frame3,selectmode = 'multiple')
conn_list = Listbox(C_frame, width = 85)

make_conn = Button(N_frame2, text = "make connection", command = connection_button)
set_parent = Button(N_frame2, text = "set host", command = set_parent)
set_child = Button(N_frame2, text = "set child", command = set_child)
add_N = Button(Value_frame, text = "add node", command = add)

type_menu.pack()
node_list1.pack(side = LEFT,padx = 5,anchor = 'w')
set_parent.pack(side = LEFT, padx = 5)
make_conn.pack(side = LEFT, padx = 5)
set_child.pack(side = BOTTOM, padx = 5)
add_N.pack()
node_list2.pack(side = RIGHT,padx = 5, anchor = 'e')
conn_list.pack(side = BOTTOM)
name.pack(anchor = 'n')
Value_frame.pack(anchor = 'n')
##Conn_frame.pack(anchor = 'se')
Node_frame.pack(anchor = 's')
N_frame1.pack(side = LEFT)
N_frame2.pack(side = LEFT)
N_frame3.pack(side = LEFT)
Connec_L.pack(side = TOP)
C_frame.pack()



main_window.mainloop()



    
#what if i have n = 0 and for each instance of n_type n = n + 1
            


