from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
from PIL import ImageTk,Image

root = Tk()
root.geometry('900x600+50+50')
root.title('Login Form')

bg = PhotoImage(file='m89.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


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

        
    
    tab1_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',12), command=tab1)
    tab1_b.place(x=230, y=30, height=40, width=200,)
    tab2_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',12), command=tab2)
    tab2_b.place(x=460, y=30, height=40, width=200,)
    tab3_b=Button(root, text='ADMIN LOGIN', font=('Times New Roman',12), command=tab3)
    tab3_b.place(x=690, y=30, height=40, width=200,)
    tab4_b=Button(root, text='HOME', font=('Times New Roman',12), command=tab4)
    tab4_b.place(x=50, y=30, height=40, width=160,)
   
    
tab()







def signin():
    if mailentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
            cur = con.cursor()
            cur.execute('select * from reg_parent where Emailid=%s and Password=%s', (mailentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid Email or Password')
                con.close()
                root.destroy()
                

            else:
                showinfo('Success', 'Welcome')
                
            con.close()
            root.destroy()
            import third
            
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

titleLabel = Label(root, text='LOGIN', font=('Times New Roman', 22, 'bold '),
                   fg='black', )
titleLabel.place(x=400, y=160)

            

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=180, y=240)

userimage = PhotoImage(file='user.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=10, y=50)
mailLabel = Label(frame, text='Email', font=('arial', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
mailentry.place(x=220, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=220, y=120)
passentry = Entry(frame, font=('arial', 22,), bg='white', fg='black', show="*")
passentry.place(x=220, y=160)


loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=450, y=240)



root.mainloop()


