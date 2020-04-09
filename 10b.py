from tkinter import *
import sqlite3
root=Tk()
root.title("Registeration-form")
root.geometry('500x400')

def fetch():
    conn = sqlite3.connect('form.db')
    with conn:
        cursor=conn.cursor()
   
    table_name=str(data1.get())
    sql=("select * from {}".format(table_name))
    cursor.execute(sql)
    result=cursor.fetchall()

    out00=Label(root,text="Name",width=10).grid(row=3,column=0)
    out01=Label(root,text="Uid",width=10).grid(row=3,column=1)
    out03=Label(root,text="Email",width=10).grid(row=3,column=2)
    out04=Label(root,text="Gender",width=10).grid(row=3,column=3)
    out05=Label(root,text="country",width=10).grid(row=3,column=4)
    
    row_count=4
    for row in result:
        out11=Label(root,text=row[0] ,width=10).grid(row=row_count,column=0)
        out12=Label(root,text=row[1] ,width=10).grid(row=row_count,column=1)    
        out13=Label(root,text=row[2] ,width=10).grid(row=row_count,column=2)
        out14=Label(root,text=row[3] ,width=10).grid(row=row_count,column=3)
        out15=Label(root,text=row[4] ,width=10).grid(row=row_count,column=4)

        row_count+=1    
    conn.commit()
    print("Data Displayed ")

data1=StringVar()   
h1=Label(root, text='Database', font=60,height=2,width=10).grid(row=0,column=1,pady=10,columnspan=6)
name=Label(root, text='Table Name:',width=10).grid(row=1,column=2)
e1=Entry(root, textvariable=data1 ,width=10).grid(row=1,column=3)
btn=Button(root, text="Show Data", command=fetch).grid(row=2,column=1,pady=20,columnspan=6)
root.mainloop()
