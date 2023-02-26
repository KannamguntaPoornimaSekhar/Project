from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.messagebox import *
import pymysql

root = Tk()
root.geometry('1050x710+0+10')
root.title('HOME PAGE')
root['bg']='gray'

bg = PhotoImage(file='now3.png')
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

        
    
    tab1_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',14), command=tab1)
    tab1_b.place(x=230, y=30, height=60, width=200,)
    tab2_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',14), command=tab2)
    tab2_b.place(x=460, y=30, height=60, width=200,)
    tab3_b=Button(root, text='ADMIN LOGIN', font=('Times New Roman',14), command=tab3)
    tab3_b.place(x=690, y=30, height=60, width=200,)
    tab4_b=Button(root, text='HOME', font=('Times New Roman',14), command=tab4)
    tab4_b.place(x=50, y=30, height=60, width=160,)
   
    
tab()


titleLabel = Label(root, text='ADMIN LOGIN', font=('Times New Roman', 22, 'bold '))
titleLabel.place(x=430, y=140, height=80)



def signin():
    if mailentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
            cur = con.cursor()
            cur.execute('select * from admin where username=%s and password=%s', (mailentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid adminname or Password')
                
                root.destroy()
                import admin

            else:
                showinfo('Success', 'Welcome')


            con.close()
            root.destroy()
            import admin_home
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)




mailLabel = Label(root, text='Admin Name', font=('arial', 22, 'bold'), bg='#E67E22', fg='black',width=10)
mailLabel.place(x=200, y=272)
mailentry = Entry(root, font=('arial', 22,), bg='white', fg='black')
mailentry.place(x=500, y=272)

passLabel = Label(root, text='Password', font=('arial', 22, 'bold'), bg='#E67E22', fg='black',width=10)
passLabel.place(x=200, y=380)
passentry = Entry(root, text="*",font=('arial', 22,), bg='WHITE', fg='black', show="*")
passentry.place(x=500, y=380)
loginbutton2 = Button(root,text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=430, y=490)



root.mainloop()
