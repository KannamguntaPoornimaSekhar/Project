from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk,messagebox
import pymysql
import os

root = Tk()
root.geometry('1050x710+0+10')
root.title('ADMIN HOME PAGE')
root['bg']='gray'
my_image= ImageTk.PhotoImage(Image.open("regi.png"))
arkaplan = Label(root, image=my_image)
arkaplan.place(x=0,y=0,relwidth=1,relheight=1 )

def clear():
    entryname.delete(0, END)
    entryrollnum.delete(0, END)
    entryemail.delete(0, END)
    entrydepartment.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryaddress.delete(0, END)
    check.set(0)



def tab():
    def tab2():
        
        root.destroy()
        import shparent
        
    def tab3():
       
        root.destroy()
        import publicsh
        
    def tab5():
       
        root.destroy()
        import home_page
        

        
      
    tab2_b=Button(root, text='PARENTS POST', font=('Arial',13, 'bold'), command=tab2)
    tab2_b.place(x=380, y=70, height=40, width=150,)

    tab3_b=Button(root, text='PUBLIC POST', font=('Arial',13, 'bold'), command=tab3)
    tab3_b.place(x=550, y=70, height=40, width=150,)
    
    tab5_b=Button(root, text='HOME', font=('Arial',13, 'bold'), command=tab5)
    tab5_b.place(x=220, y=70, height=40, width=150,)



tab()

def register():
    root.destroy()
    import image

def register1():
    root.destroy()
    import found_data_try

registerbutton = Button(root, text = 'IMAGE MATCH', bg='white', font=('Arial',13, 'bold'), activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=720, y=70, height=40, width=150)

registerbutton = Button(root, text = 'CHILD DETAILS', bg='white', font=('Arial',13, 'bold'), activebackground='white'
                        , activeforeground='white', command=register1)
registerbutton.place(x=880, y=70, height=40, width=150)


root.mainloop()
