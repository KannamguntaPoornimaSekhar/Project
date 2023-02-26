from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import ttk,messagebox


root=tk.Tk()
root.title("parent post")
root.geometry('1350x710+0+10')
connect = pymysql.connect(host="localhost",user="root",password="admin",
                             database="child")
root.resizable(width=1, height=1)


conn = connect.cursor()
conn.execute("SELECT * FROM parent")

bg = PhotoImage(file='now3.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0,)



def tab():
    def tab2():
        
        root.destroy()
        import shparent
        
    def tab3():
       
        root.destroy()
        import publicsh
        
    def tab5():
       
        root.destroy()
        
        
       
      
    tab2_b=Button(root, text='PARENTS POST', font=('Arial',13, 'bold'), command=tab2)
    tab2_b.place(x=380, y=70, height=40, width=150,)

    tab3_b=Button(root, text='PUBLIC POST', font=('Arial',13, 'bold'), command=tab3)
    tab3_b.place(x=550, y=70, height=40, width=150,)
    
    tab5_b=Button(root, text='LOGOUT', font=('Arial',13, 'bold'), command=tab5)
    tab5_b.place(x=20, y=70, height=40, width=150,)


tab()

 

def myclick():
    showinfo('Success', "approve Successful", parent=root)
    

tree = ttk.Treeview(root)




tree["columns"]=("idparent","childname","parentname","phonenumber","email","address","aadharnumber","photo","fircopy")

horizontal_bar = ttk.Scrollbar(root, orient="horizontal")
horizontal_bar.configure(command=tree.xview)
tree.configure(xscrollcommand=horizontal_bar.set)
horizontal_bar.pack(fill=X, side=BOTTOM)

vertical_bar = ttk.Scrollbar(root, orient="vertical")
vertical_bar.configure(command=tree.yview)
tree.configure(yscrollcommand=vertical_bar.set)
vertical_bar.pack(fill=Y, side=RIGHT)


tree.column("idparent", width=50,minwidth=100,anchor=tk.CENTER)
tree.column("childname", width=50, minwidth=100,anchor=tk.CENTER)
tree.column("parentname", width=50, minwidth=100,anchor=tk.CENTER)             
tree.column("phonenumber", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("email", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("address", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("aadharnumber", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("photo", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("fircopy", width=150, minwidth=150,anchor=tk.CENTER)

tree.heading("idparent", text="idparent",anchor=tk.CENTER)
tree.heading("childname", text="childname",anchor=tk.CENTER)
tree.heading("parentname", text="parentname",anchor=tk.CENTER)
tree.heading("phonenumber", text="phonenumber",anchor=tk.CENTER)
tree.heading("email", text="email",anchor=tk.CENTER)
tree.heading("address", text="address",anchor=tk.CENTER)
tree.heading("aadharnumber", text="aadharnumber",anchor=tk.CENTER)
tree.heading("photo", text="photo",anchor=tk.CENTER)
tree.heading("fircopy", text="fircopy",anchor=tk.CENTER)


i=0
for ro in conn:
             tree.insert('',i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
             i=i+1


tree.pack(pady=280)

def Delete():
        
        connect = pymysql.connect(host="localhost",user="root",password="admin",
                             database="child")
        conn = connect.cursor() 
        if not tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn.execute("DELETE FROM parent WHERE id= %d" % selecteditem[0])
            connect.commit()
            conn.close()
            connect.close()




def uploadfile():
    f = open('D:/Kalaiyarasi/child missing/missing file/fir_copy.txt', 'r')
    content = f.read()
    my_text.insert(END, content)
    print('file open')
    f.close()


my_text = Text(root, width=40, height=10, font=("Times New Roman", 12))
my_text.place(x=400, y=450)

    
titleLabel = Label(root, text='PARENTS MISSING POSTS', font=('Times New Roman', 22, 'bold '), bg='#E67E22',
                   fg='BLACK', )
titleLabel.place(x=0, y=140, width=1350, height=80)


registerbutton = Button(root, text = 'REMOVE', font=('Times New Roman', 8, 'bold '), bg='white', command=Delete)
registerbutton.place(x=1255, y=305, height=20, width=50)


filebutton = Button(root, text = 'file', font=('Times New Roman', 10, 'bold '), bg='white', command=uploadfile)
filebutton.place(x=1310, y=305, height=20, width=50)

def register():
    root.destroy()
    import image

registerbutton = Button(root, text = 'IMAGE MATCH', bg='white', font=('Arial',13, 'bold'), activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=710, y=70, height=40, width=150)

tab()

root.mainloop()
        
             
