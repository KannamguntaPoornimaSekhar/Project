from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import ttk,messagebox

root=tk.Tk()
root.title("volunteer details")
root.geometry('1150x710+0+10')
connect = pymysql.connect(host="localhost",user="root",password="admin",
                             database="child")
bg = PhotoImage(file='logo1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


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



 
conn = connect.cursor()
conn.execute("SELECT * FROM public")

button = PhotoImage(file='pubbutton.png')
titleLabel = Label(root, image=button, bd=0, cursor='hand2', font=('Times New Roman', 22, 'bold '), 
                   fg='BLACK', )
titleLabel.place(x=520, y=120)


    

tree=ttk.Treeview(root)

tree["columns"]=("id","PublicName","Mobilenumber","PublicAddress","PublicAadhaarNo","photo")

tree.column("id", width=50,minwidth=100,anchor=tk.CENTER)          
tree.column("PublicName", width=100, minwidth=150,anchor=tk.CENTER)             
tree.column("Mobilenumber", width=100, minwidth=150,anchor=tk.CENTER)             
tree.column("PublicAddress", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("PublicAadhaarNo", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("photo", width=150, minwidth=150,anchor=tk.CENTER)             


tree.heading("id", text="id",anchor=tk.CENTER)
tree.heading("PublicName", text="PublicName",anchor=tk.CENTER)
tree.heading("Mobilenumber", text="Mobilenumber",anchor=tk.CENTER)
tree.heading("PublicAddress", text="PublicAddress",anchor=tk.CENTER)
tree.heading("PublicAadhaarNo", text="PublicAadhaarNo",anchor=tk.CENTER)
tree.heading("photo", text="photo",anchor=tk.CENTER)



i=0
for ro in conn:
             tree.insert('',i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
             i=i+1

tree.pack(pady=200)

def register():
    root.destroy()
    import image

registerbutton = Button(root, text = 'IMAGE MATCH', bg='white', font=('Arial',13, 'bold'), activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=710, y=73, height=40, width=150)

root.mainloop()
        
             
