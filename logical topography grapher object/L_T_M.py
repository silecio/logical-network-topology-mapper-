#object oriented ver
from tkinter import *
import yaml
main_window = Tk()
##main_window.geometry("500x100")
Value_frame = LabelFrame(main_window)
Node_frame = LabelFrame(main_window)
N_frame1 = LabelFrame(Node_frame)
N_frame2 = LabelFrame(Node_frame)
N_frame2_5 = LabelFrame(N_frame2)
N_frame3 = LabelFrame(Node_frame)
C_frame = LabelFrame(main_window)

scrollbar_s = Scrollbar(C_frame, orient = HORIZONTAL) 
##Conn_frame = LabelFrame(main_window)
parents = []
children = []
connections = []
M_parents =[]
Names = []
def clear_selec():
    parents.clear()
    children.clear()
def add():
    current_node = (clicked.get() , name.get())
    print(current_node)
    #change into vairiable list
    node_list1.insert(END, current_node)
    node_list2.insert(END, current_node)
def set_parent():
    x = node_list1.get(0,END)
    print(x)
    index= node_list1.curselection()
    print(index)
    parent = [x[i] for i in index]
    print(parent)
    parents.append(parent)
    Names.append(parents[0])
    print(parents)
def set_child():
    x = node_list2.get(0,END)
    index= node_list2.curselection()
    child = [x[i] for i in index]
    children.append(child)

#Working(not finished, needs to store the Yaml data and format yaml correctly) 
def connection_button():
    #want format [[PARENT,[CHILD,CHILD...],[PARENT[CHILD,CHILD...]ETC]
    class parent:
        def __init__(self):
            self.name = parents[0]
            self.cons_l = children[0]
    
    p = parent()
    fin_p = {"temp":{"parent": p.name, "connections": p.cons_l}}
    M_parents.append(fin_p)
    Y_mp = yaml.dump(M_parents)
    print(Y_mp)
    print(M_parents)
    print(Names)
    x = p.name
    y = ' '.join(x[0])

    conn_list1.insert(END,y)
    parents.clear()
    children.clear()
    
options = ["server","host","switch"]

clicked = StringVar()
clicked.set("Type")

type_menu = OptionMenu(main_window, clicked, *options)


name = Entry(main_window)

Connec_L = Label(C_frame, text = "Connections")

node_list1 = Listbox(N_frame1)
node_list2 = Listbox(N_frame3,selectmode = 'multiple')
conn_list1 = Listbox(C_frame)
conn_list2 = Listbox(C_frame)



make_conn = Button(N_frame2_5, text = "make connection", command = connection_button)
set_parent = Button(N_frame2, text = "set host", command = set_parent)
set_child = Button(N_frame2, text = "set child", command = set_child)
add_N = Button(Value_frame, text = "add node", command = add)
clear_all = Button(N_frame2_5, text = "clear selections", command = clear_selec)

type_menu.pack()
node_list1.pack(side = LEFT,padx = 5,anchor = 'w')
set_parent.pack(side = LEFT, padx = 5)
make_conn.pack(side = TOP, padx = 5, pady = 5)
set_child.pack(side = RIGHT, padx = 5)
clear_all.pack(side = BOTTOM,padx = 5, pady = 5)
add_N.pack()
node_list2.pack(side = RIGHT,padx = 5, anchor = 'e')
conn_list1.pack(side = LEFT)
conn_list2.pack(side = RIGHT)
name.pack(anchor = 'n')
Value_frame.pack(anchor = 'n')
##Conn_frame.pack(anchor = 'se')
Node_frame.pack(anchor = 's')
N_frame1.pack(side = LEFT)
N_frame2.pack(side = LEFT)
N_frame2_5.pack(side = LEFT)
N_frame3.pack(side = LEFT)
Connec_L.pack(side = TOP)
C_frame.pack()



main_window.mainloop()



    

            


