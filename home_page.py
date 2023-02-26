from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('1350x710+0+10')
root.title('HOME PAGE')
root['bg']='gray'


bg = PhotoImage(file='file1.png')
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
         
    
    
    tab1_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',15), command=tab1)
    tab1_b.place(x=650, y=30, height=60, width=220,)
    tab2_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',15), command=tab2)
    tab2_b.place(x=878, y=30, height=60, width=220,)
    tab3_b=Button(root, text='ADMIN LOGIN', font=('Times New Roman',15), command=tab3)
    tab3_b.place(x=1110, y=30, height=60, width=210,)
    tab4_b=Button(root, text='HOME', font=('Times New Roman',15), command=tab4)
    tab4_b.place(x=430, y=30, height=60, width=210,)
    
tab()
root.mainloop()
