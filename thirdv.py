from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('1050x710+0+10')
root.title('HOME PAGE')
root['bg']='gray'
my_image= ImageTk.PhotoImage(Image.open("a6.png"))
arkaplan = Label(root, image=my_image)
arkaplan.place(x=0,y=0,relwidth=1,relheight=1 )
def tab():
    def tab1():

        root.destroy()
        import home_page

    def tab2():
        
        root.destroy()
        import reg_parent
    def tab3():
       
        root.destroy()
        import reg_volunty
        
    def tab4():
        root.destroy()
        import admin

    def tab5():
        
        root.destroy()
        import public
    def tab7():
        
        root.destroy()

    tab1_b=Button(root, text='HOME', font=('Times New Roman',12), command=tab1)
    tab1_b.place(x=50, y=30, height=40, width=160,)     
    tab2_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',12), command=tab2)
    tab2_b.place(x=230, y=30, height=40, width=200,)
    tab3_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',12), command=tab3)
    tab3_b.place(x=460, y=30, height=40, width=200,)
    tab4_b=Button(root, text='ADMIN LOGIN', font=('Times New Roman',14), command=tab4)
    tab4_b.place(x=690, y=30, height=40, width=200,)
    tab5_b=Button(root, text='MISSING PERSON DETAILS', font=('Times New Roman',12), command=tab5)
    tab5_b.place(x=650, y=100, height=40, width=250,) 
    

    tab7_b=Button(root, text='LOGOUT', font=('Times New Roman',14), command=tab7)
    tab7_b.place(x=20, y=100, height=50, width=150,)  
   
    
    
    
    
tab()

root.mainloop()
