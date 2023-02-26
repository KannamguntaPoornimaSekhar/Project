from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk,messagebox
import pymysql
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText 
from email.utils import formataddr

root = Tk()
root.geometry('1050x710+0+10')
root.title('HOME PAGE')
root['bg']='gray'
my_image= ImageTk.PhotoImage(Image.open("s1.png"))
arkaplan = Label(root, image=my_image)
arkaplan.place(x=0,y=0,relwidth=1,relheight=1 )

def tab():
    def tab1():

        root.destroy()
        import home_page

    
    
    def tab7():
        
        root.destroy()

    tab1_b=Button(root, text='HOME', font=('Times New Roman',12), command=tab1)
    tab1_b.place(x=710, y=50, height=30, width=100,)   
     
    tab7_b=Button(root, text='LOGOUT', font=('Times New Roman',12), command=tab7)
    tab7_b.place(x=870, y=50, height=30, width=100,)  
   
    
tab()    
    
    
con = pymysql.connect(host='localhost', user='root', password='admin', database='child')
cur = con.cursor()
cur.execute('SELECT * FROM parent');
myresult = cur.fetchall()



            
def details():
    roott = Tk()
    roott.title("Parent record")
    roott.geometry("300x300")
    selected=tree.focus()
    values=tree.item(selected, 'values')
    


   

    

style = ttk.Style()
style.configure("Treeview",
            foreground="black",
            rowheight=20,
            fieldbackground="white",
            )
style.map('Treeview', background=[('selected', 'lightblue')])

         



        
            


tree = ttk.Treeview(root)

   



tree["columns"]=("id","ChildName","ParentName","phoneNumber","Emailid","Address","AadharNo","photo","FIRcopy")

tree.column("#0", width=0, stretch=NO)
tree.column("id", width=50,minwidth=100,anchor=tk.CENTER)
tree.column("ChildName", width=50, minwidth=100,anchor=tk.CENTER)
tree.column("ParentName", width=50, minwidth=100,anchor=tk.CENTER)             
tree.column("phoneNumber", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("Emailid", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("Address", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("AadharNo", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("photo", width=150, minwidth=150,anchor=tk.CENTER)             
tree.column("FIRcopy", width=150, minwidth=150,anchor=tk.CENTER)

tree.heading("id", text="idparent",anchor=tk.CENTER)
tree.heading("ChildName", text="CHILD NAME",anchor=tk.CENTER)
tree.heading("ParentName", text="PARENT NAME",anchor=tk.CENTER)
tree.heading("phoneNumber", text="PHONE NUMBER",anchor=tk.CENTER)
tree.heading("Emailid", text="EMAIL",anchor=tk.CENTER)
tree.heading("Address", text="ADDRESS",anchor=tk.CENTER)
tree.heading("AadharNo", text="AADHAR NUMBER",anchor=tk.CENTER)
tree.heading("photo", text="PHOTO",anchor=tk.CENTER)
tree.heading("FIRcopy", text="FIRCOPY",anchor=tk.CENTER)


i=0
for ro in myresult:
             tree.insert('',i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
             i=i+1


tree.pack(pady=280)


rollnumLabel = Label(root, text='MATCH RECORD', font=('times new roman', 17, 'bold'), bg='white',
                      fg='black',)
rollnumLabel.place(x=425, y=57, width=200)

def selectRecord():
    selected=tree.focus()
    values=tree.item(selected, 'values')
    messagebox.showinfo(messagebox,values)
   
    def sendEmail():
       
        selected=tree.focus()
        values=tree.item(selected, 'values')
        
        valu = values[2]
        value = values[4]
        host = "smtp.gmail.com"
        mmail = "diwa.2801@gmail.com"        
        hmail = value
        receiver_name = valu
        sender_name= "Missing Child Found"
        msg = MIMEMultipart()
        subject = '''Hello,
               'We found your Child',
               For further Details
               Contant us- 1098
               Email-id: diwa.2801@gmail.com'''
        text = '''Hello,
               'We found your Child',
               For further Details
               Contant us- 1098
               Email-id: diwa.2801@gmail.com'''
        msg = MIMEText(text, 'plain')
        msg['To'] = formataddr((receiver_name, hmail))
        msg['From'] = formataddr((sender_name, mmail))
        msg['Subject'] = 'Hello, my friend ' + receiver_name
        server = smtplib.SMTP(host, 587)
        server.ehlo()
        server.starttls()
        password = "furgqbokcooqfjkf"
        server.login(mmail, password)
        server.sendmail(mmail, [hmail], msg.as_string())
        server.quit()
        print('send')
        messagebox.showinfo('Email Sent'," succesfully Sent")


    b2 = tk.Button(root, text='Send Mail', width=20,command = lambda:sendEmail(), activebackground='#000080', bg='white')
    b2.place(x=780, y=550, width=100, height=40)

   
 


b2 = tk.Button(root, text='select', 
   width=20,command = lambda:selectRecord(), activebackground='#000080', bg='white')
b2.place(x=410, y=550, width=100, height=40)




root.mainloop()
        



