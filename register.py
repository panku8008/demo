from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

name=StringVar()
UID=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()

def database():
   name1=name.get()
   uid=uid.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()


label_0 = Label(root, text="Registration form",width=20,bg='yellow',font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=70,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="UID",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email",width=20,font=("bold",10))
label_3.place(x=70,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=280)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=280)

label_5 = Label(root, text="country",width=20,font=("bold", 10))
label_5.place(x=70,y=330)
list1 = ['India','Canada','UK','NZ','Germny'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
mainloop()
