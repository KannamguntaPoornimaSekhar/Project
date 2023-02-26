from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
from PIL import ImageTk,Image

root = Tk()
root.geometry('1050x710+0+10')
root.title('Registration Form')

bg = PhotoImage(file='regi.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


def clear():
    entryname.delete(0, END)
    entryemail.delete(0, END)
    entrymobilenumber.delete(0, END)
    entryaddress.delete(0, END)
    entrypincode.delete(0, END)
    entrypassword.delete(0, END)
    check.set(0)

def login_window():
    root.destroy()
    import log_parent

def tab():
    def tab4():

        root.destroy()
        import home_page

    def tab1():
        
        root.destroy()
        import reg_parent
    def tab2():
       
        root.destroy()
        import reg_volunty
        
    def tab3():
        root.destroy()
        import admin

        
    
    tab1_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',15), command=tab1)
    tab1_b.place(x=290, y=30, height=60, width=220,)
    tab2_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',15), command=tab2)
    tab2_b.place(x=520, y=30, height=60, width=220,)
    tab3_b=Button(root, text='ADMIN LOGIN', font=('Times New Roman',15), command=tab3)
    tab3_b.place(x=750, y=30, height=60, width=210,)
    tab4_b=Button(root, text='HOME', font=('Times New Roman',15), command=tab4)
    tab4_b.place(x=100, y=30, height=60, width=210,)
   
    
tab()







def register():
    if entryname.get() == '' or entryemail.get() == '' or entrymobilenumber.get()== '' or  entryaddress.get()=='' or\
            entrypincode.get()=='' or entrypassword.get() == '':
        messagebox.showerror('Error', "All Fields Are Required", parent=root)

    

    elif check.get() == 0:
        messagebox.showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
            cur = con.cursor()
            cur.execute('select * from reg_parent where Name=%s', entryname.get())
            
            row = cur.fetchone()
            if row != None:
                showerror('Error', "User Already Exists", parent=root)
            else:

                cur.execute('insert into reg_parent (name, emailid, mobilenumber, address, pincode, password) values(%s,%s,%s,%s,%s,%s)',(entryname.get(), entryemail.get(), entrymobilenumber.get(), entryaddress.get(),
                     entrypincode.get(), entrypassword.get()))
                con.commit()
                con.close()
                showinfo('Success', "Registration Successful", parent=root)
                clear()
                
                
             


        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)




titleLabel = Label(root, text='REGISTRATION FORM', font=('Times New Roman', 22, 'bold '), bg='blue',
                   fg='white', )
titleLabel.place(x=350, y=100)

nameLabel = Label(root, text='Name', font=('times new roman', 18, 'bold'), bg='blue',
                       fg='white', )
nameLabel.place(x=250, y=160, width=200)
entryname = Entry(root, font=('times new roman', 18), bg='lightgray')
entryname.place(x=550, y=160, width=240)

emailLabel = Label(root, text='Emailid', font=('times new roman', 18, 'bold'), bg='blue',
                     fg='white', )
emailLabel.place(x=250, y=230, width=200)
entryemail = Entry(root, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=550, y=230, width=240)

mobilenumberLabel = Label(root, text='Mobile Number', font=('times new roman', 18, 'bold'), bg='blue', fg='white', )
mobilenumberLabel.place(x=250, y=300, width=200)
entrymobilenumber = Entry(root, font=('times new roman', 18), bg='lightgray')
entrymobilenumber.place(x=550, y=300, width=240)

addressLabel = Label(root, text='Address', font=('times new roman', 18, 'bold'), bg='blue',
                    fg='white', )
addressLabel.place(x=250, y=350, width=200)
entryaddress = Entry(root,font=('times new roman', 18), bg='lightgray',)
entryaddress.place(x=550, y=350, width=240)


pincodeLabel = Label(root, text='pincode', font=('times new roman', 18, 'bold'), bg='blue',
                      fg='white', )
pincodeLabel.place(x=250, y=400, width=200)
entrypincode = Entry(root, font=('times new roman', 18), bg='lightgray')
entrypincode.place(x=550, y=400, width=240)

passwordLabel = Label(root, text='password', font=('times new roman', 18, 'bold'), bg='blue',
                      fg='white', )
passwordLabel.place(x=250, y=450, width=200)
entrypassword = Entry(root, font=('times new roman', 18), bg='lightgray', show="*")
entrypassword.place(x=550, y=450, width=240)

check = IntVar()
checkButton = Checkbutton(root, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=330, y=530)

button = PhotoImage(file='button.png')
registerbutton = Button(root, image=button, bd=0, cursor='hand2', bg='white', activebackground='white'
                        , activeforeground='white', command= register)
registerbutton.place(x=380, y=590)

loginimage = PhotoImage(file='login.png')
loginbutton1 = Button(root, image=loginimage, bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=login_window)
loginbutton1.place(x=680, y=560)


root.mainloop()
