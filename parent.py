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
root.title('PARENT POST FORM')

bg = PhotoImage(file='b1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


 
    

def tab():
    def tab1():

        root.destroy()
        import home_page

    def tab2():
        
        root.destroy()
        import reg_parent
    
    def tab5():

        root.destroy()

        
    
    tab2_b=Button(root, text='PARENT LOGIN', font=('Times New Roman',10), command=tab2)
    tab2_b.place(x=890, y=10, height=20, width=150,)

    tab1_b=Button(root, text='HOME', font=('Times New Roman',10), command=tab1)
    tab1_b.place(x=750, y=10, height=20, width=100,)
   
    
    cf1=Canvas(root, bg='white',width=1050, height=80)
    cf1.place(x=1,y=40)
  
    tab5_b=Button(root, text='LOGOUT', font=('Times New Roman',12), command=tab5)
    tab5_b.place(x=20, y=60, height=50, width=72,)
    
     
tab()

   

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binary = file.read()
        
    return binary

def clear():
    entryname.delete(0, END)
    entryrollnum.delete(0, END)
    entryemail.delete(0, END)
    entrydepartment.delete(0, END)
    entryaddress.delete(0, END)
    entrypassword.delete(0, END)
    check.set(0)

var_photo_list = []

def uploadImg():
    filename = filedialog.askopenfilename(initialdir =  "D:/Kalaiyarasi/child missing", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
    img = Image.open(filename)
    data = entryname.get()
    save_path = "D:/Kalaiyarasi/child missing/parent_image"
    file_name = f"{data}.png"
    complete_name = os.path.join(save_path, file_name)
    img.save(complete_name)
        
    resize_image = img.resize((200, 150)) 
            
    show_img = ImageTk.PhotoImage(resize_image) 
    
    var_photo = Label(img_LabelFrame,image=show_img)

    var_photo.image = show_img
   
    var_photo.pack()       
  
    img=convertToBinaryData(filename)
    return filename
   
   

def uploadfile():
    filename1 = filedialog.askopenfilename(initialdir =  "D:/Kalaiyarasi/child missing", title = "Select File", filetype = (("Text files","*.txt*"),("all files","*.*")))  
    show_file = Label(entrypoliceFIRcopy_LabelFrame.configure(text="File Opened:" + filename1))       
    file=convertToBinaryData(filename1)
    return filename1


def register():
    if entryname.get() == '' or entryrollnum.get() == '' or entryemail.get() == '' or entrydepartment.get()== '' or \
            entrypassword.get() == ''  or entryaddress.get() == '':
        messagebox.showerror('Error', "All Fields Are Required", parent=root)

    

    elif check.get() == 0:
        messagebox.showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
            cur = con.cursor()
            cur.execute('select * from parent where ChildName=%s and ParentName=%s', (entryname.get(), entryrollnum.get()))
            
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error', "User Already Exists", parent=root)
            else:

                cur.execute('insert into parent (ChildName, ParentName, phoneNumber, Emailid, Address, AadharNo, photo, FIRcopy) values(%s,%s,%s,%s,%s,%s,%s,%s)', (entryname.get(), entryrollnum.get(), entryemail.get(), entrydepartment.get(),
                     entryaddress.get(), entrypassword.get(), uploadImg(), uploadfile()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', "Registration Successful", parent=root)
                clear()
                
                


        except Exception as e:
            messagebox.showerror('Error', f"Error due to: {e}", parent=root)





titleLabel = Label(root, text='CHILD MISSING DETAILS', font=('Times New Roman', 22, 'bold '), bg='white',
                   fg='black', )
titleLabel.place(x=380, y=60)

nameLabel = Label(root, text='Child Name', font=('times new roman', 18, 'bold'), bg='white',
                       fg='black', )
nameLabel.place(x=70, y=160, width=200)
entryname = Entry(root, font=('times new roman', 18), bg='lightgray')
entryname.place(x=350, y=160, width=230)

rollnumLabel = Label(root, text='Parent Name', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
rollnumLabel.place(x=70, y=200, width=200)
entryrollnum= Entry(root, font=('times new roman', 18), bg='lightgray')
entryrollnum.place(x=350, y=200, width=230)

emailLabel = Label(root, text='phone Number', font=('times new roman', 18, 'bold'), bg='white',
                     fg='black', )
emailLabel.place(x=70, y=250, width=200)
entryemail = Entry(root, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=350, y=250, width=230)

departmentLabel = Label(root, text='Email id', font=('times new roman', 18, 'bold'), bg='white', fg='black', )
departmentLabel.place(x=70, y=300, width=200)
entrydepartment = Entry(root, font=('times new roman', 18), bg='lightgray')
entrydepartment.place(x=350, y=300, width=230)


addressLabel = Label(root, text='Address', font=('times new roman', 18, 'bold'), bg='white',
                    fg='black', )
addressLabel.place(x=70, y=350, width=200)
entryaddress = Entry(root,font=('times new roman', 18), bg='lightgray',)
entryaddress.place(x=350, y=350, width=230)


passwordLabel = Label(root, text='Aadhaar No', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
passwordLabel.place(x=70, y=400, width=200)
entrypassword = Entry(root, font=('times new roman', 18), bg='lightgray')
entrypassword.place(x=350, y=400, width=230)

lbl_Std_photo = Label(root, text="Missing Photo: ", font= ("Arial",15,)).place(x=70,y=450 , width=200,)
img_LabelFrame= tk.LabelFrame(root, text="")
img_LabelFrame.place(x=350,y=450, width=200,height=100)


btn_upload_img = Button(text="Upload Image", bg="gray", command= uploadImg).place(x=70, y=500, width= 200 , height=40)


policeFIRcopyLabel = Label(root, text='POLICE FIR COPY', font=('times new roman', 16, 'bold')).place(x=670,y=200, width=200,)
entrypoliceFIRcopy_LabelFrame= tk.LabelFrame(root, text="")
entrypoliceFIRcopy_LabelFrame.place(x=670,y=270,width=200, height=100)

btn_upload_file = Button(text="Upload FIR COPY", bg = "gray", command= uploadfile).place(x=720, y=400, height=40)



check = IntVar() 
checkButton = Checkbutton(root, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=390, y=560)

button = PhotoImage(file='submit3.png')
registerbutton = Button(root, image=button, bd=0, cursor='hand2', bg='white', activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=320, y=620)




root.mainloop()


