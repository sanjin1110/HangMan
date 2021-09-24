from tkinter import *
root=Tk()
root.title("LOG-IN")
root.minsize(600,500)
root.maxsize(600,600)
root.configure(bg="antique white")
root.iconbitmap('icon.ico')

lab0=Label(root,text='Sign Up',font=20,bg='antique white')
lab0.grid(row=0,column=1,padx=10,pady=10)
lab1=Label(root,text='Username:',bg='thistle3')
lab1.grid(row=2,column=1,padx=10,pady=10)
lab2=Label(root,text='User-mail:',bg='thistle3')
lab2.grid(row=3,column=1,padx=10,pady=10)
lab3=Label(root,text='Password:',bg='thistle3')
lab3.grid(row=4,column=1,padx=10,pady=10)
lab5=Label(root,text='Phone No.:',bg='thistle3')
lab5.grid(row=5,column=1,padx=10,pady=10)
lab7=Label(root,text='Gender',bg='thistle3')
lab7.grid(row=6,column=1,padx=10,pady=10)

ent1=Entry(root,text='hello',fg='black',width=30)
ent1.grid(row=2,column=2)
ent2=Entry(root,width=30)
ent2.grid(row=3,column=2)
ent3=Entry(root,width=30)
ent3.grid(row=4,column=2)
ent4=Entry(root,width=30)
ent4.grid(row=5,column=2)

but1=Button(root,text='LOGIN',bg='white', fg='green2')
but1.grid(row=9,column=2,columnspan = 5)

r1=Checkbutton(root,text='I accept Terms Of Use & Privacy Policy')
r1.grid(row=7,column=2,columnspan = 2)

var = IntVar()
r2=Radiobutton(root,text='male',value=1,variable = var)
r2.grid(row=6,column=2)
r3=Radiobutton(root,text='female',value=2,variable = var)
r3.grid(row=6,column=3)


root.mainloop()