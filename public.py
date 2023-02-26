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
root.title('PUBLIC POST FORM')

bg = PhotoImage(file='s3.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)


def tab():
    def tab1():

        root.destroy()
        import home_page

   
    def tab3():
       
        root.destroy()
        import reg_volunty
        
    
    def tab5():

        root.destroy()

        
    

    tab3_b=Button(root, text='VOLUNTEERS LOGIN', font=('Times New Roman',10), command=tab3)
    tab3_b.place(x=890, y=10, height=20, width=150,)

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
    entrypublicname.delete(0, END)
    entrypublicmobilenumber.delete(0, END)
    entrypublicaddress.delete(0, END)
    entryadharnumber.delete(0, END)
    check.set(0)

def uploadImg():
    filename = filedialog.askopenfilename(initialdir =  "D:/Kalaiyarasi/child missing", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
    image = Image.open(filename) 
    data = entrypublicname.get()
    print(data)
    save_path = "D:/Kalaiyarasi/child missing/images"
    file_name = f"{data}.png"
    print(file_name)
    complete_name = os.path.join(save_path, file_name)
    image.save(complete_name)
        
              
    resize_image = image.resize((200, 150)) 
            
    show_img = ImageTk.PhotoImage(resize_image) 

    var_photo = Label(img_LabelFrame,image=show_img)

    var_photo.image = show_img
    var_photo.pack()
    img=convertToBinaryData(filename)
    return filename

    



def register():
    if entrypublicname.get() == '' or entrypublicmobilenumber.get()== '' or entrypublicaddress.get() == ''  or entryadharnumber.get() == '':
        messagebox.showerror('Error', "All Fields Are Required", parent=root)

    

    elif check.get() == 0:
        messagebox.showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
            cur = con.cursor()
            cur.execute('select * from public where PublicAadharNo=%s', entrypublicaddress.get())
            
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error', "User Already Exists", parent=root)
            else:

                cur.execute('insert into public (PublicName, Mobilenumber, PublicAddress, PublicAadharNo, photo) values(%s,%s,%s,%s,%s)', (entrypublicname.get(), entrypublicmobilenumber.get(),
                     entrypublicaddress.get(), entryadharnumber.get(), uploadImg()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', "Registration Successful", parent=root)
                clear()
                               


        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)







titleLabel = Label(root, text='CHILD DETAILS', font=('Times New Roman', 22, 'bold '), 
                   fg='black', )
titleLabel.place(x=420, y=60)



publicnameLabel = Label(root, text='Public Name', font=('times new roman', 18, 'bold'), bg='white',
                     fg='black', )
publicnameLabel.place(x=170, y=200, width=200)
entrypublicname = Entry(root, font=('times new roman', 18), bg='lightgray')
entrypublicname.place(x=650, y=200, width=210)

publicmobilenumberLabel = Label(root, text='Public Mobile No', font=('times new roman', 18, 'bold'), bg='white', fg='black', )
publicmobilenumberLabel.place(x=170, y=260, width=200)
entrypublicmobilenumber = Entry(root, font=('times new roman', 18), bg='lightgray')
entrypublicmobilenumber.place(x=650, y=260, width=210)




addressLabel = Label(root, text='Address', font=('times new roman', 18, 'bold'), bg='white',
                    fg='black', )
addressLabel.place(x=170, y=330, width=200)
entrypublicaddress = Entry(root,font=('times new roman', 18), bg='lightgray')
entrypublicaddress.place(x=650, y=330, width=210)


adharnumberLabel = Label(root, text='Public Aadhaar No', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
adharnumberLabel.place(x=170, y=390, width=200)
entryadharnumber = Entry(root, font=('times new roman', 18), bg='lightgray')
entryadharnumber.place(x=650, y=390, width=210)

lbl_Std_photo = Label(root, text="Child Photo: ", font= ("Arial",15,)).place(x=170,y=450 , width=200,)
img_LabelFrame= tk.LabelFrame(root, text="")
img_LabelFrame.place(x=650,y=450, width=200,height=100)


btn_upload_img = Button(text="Upload Image", bg="grey", command= uploadImg).place(x=170, y=500, width= 200 , height=40)





check = IntVar()
checkButton = Checkbutton(root, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=470, y=580)

button = PhotoImage(file='submit3.png')
registerbutton = Button(root, image=button, bd=0, cursor='hand2', bg='white', activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=320, y=620)


root.mainloop()


