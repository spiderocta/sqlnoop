from tkinter import *
root = Tk()
root.geometry('1010x550+200+30')
root.resizable(False,False)
root.configure(background='white')
root.title('octaconnect  [Database Manager v1.0(SQL)]')
root.iconbitmap('images/icon.ico')


maintTitle = Label(root, text='Database Connector and Manager v1.0 BETA', fg='white', bg='#19282F', font=('tajawal',15))
maintTitle.pack(fill=X)


F1 = Frame(root,bg='white',bd=2,relief=GROOVE)
F1.place(x=5, y=40, width=300, height =190)
  
controlsTitle = Label(F1, text='Database Controls', fg='white', bg='#19282F', font=('tajawal',15))
controlsTitle.pack(fill=X)

# databases controls section

L = Label(F1, text='DB Controls')
L.place(x=10, y=50)

showAllDataBasesButton = Button(F1, text='Show Databases' , cursor='hand2')
showAllDataBasesButton.place(x=105, y=47, width=125)

hieAllDataBasesButton = Button(F1, text='Hide' , cursor='hand2')
hieAllDataBasesButton.place(x= 235, y=47, width=55)


# databases names section

L = Label(F1, text='Database Name : ')
L.place(x=10, y=80)

En1 = Entry(F1)
En1.place(x=110, y=80)

createbutton = Button(F1, text='create Db' , cursor='hand2')
createbutton.place(x=230, y = 78, width=60)

# tables section

L = Label(F1, text='Table Cols: ')
L.place(x=10, y=110)

createTableButton = Button(F1, text='Creat Table' , cursor='hand2')
createTableButton.place(x=100, y=107, width=125)

hideTablesButton = Button(F1, text='Hide' , cursor='hand2')
hideTablesButton.place(x=230, y=107, width=60)

root.mainloop()

