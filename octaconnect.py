from tkinter import *
root = Tk()
root.geometry('1010x550+200+30')
root.resizable(False,False)
root.configure(background='whitesmoke')
root.title('octaconnect  [Database Manager v1.0(SQL)]')
root.iconbitmap('images/icon.ico')


maintTitle = Label(root, text='Database Connector and Manager v1.0 BETA', fg='white', bg='#19282F', font=('tajawal',15))
maintTitle.pack(fill=X)

#===================== DB Controls Frame ===========================
F1 = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
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



#Columns section

L = Label(F1, text='Add Cols: ')
L.place(x=10, y=140)

addColButton = Button(F1, text='Add Comlumns' , cursor='hand2')
addColButton.place(x=100, y=137, width=125)

hideColssButton = Button(F1, text='Hide' , cursor='hand2')
hideColssButton.place(x=230, y=137, width=60)


#====================== Database Connection Frame =======================

FF1 = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
FF1.place(x=310, y=40, width=300, height =190)
  
controlsTitle = Label(FF1, text='Database Connection', fg='white', bg='#19282F', font=('tajawal',15))
controlsTitle.pack(fill=X)

#==================== Server ============================================

LL1 = Label(FF1, text='server name : ')
LL1.place(x=10, y=50)

Enn1 = Entry(FF1)
Enn1.place(x=100, y=50)

#======= Server Details =========
#===== username =======

LL2 = Label(FF1, text='username : ')
LL2.place(x=10, y=80)

Enn2 = Entry(FF1)
Enn2.place(x=100, y=80)

#===== password =======

LL3 = Label(FF1, text='password : ')
LL3.place(x=10, y=110)

Enn3 = Entry(FF1)
Enn3.place(x=100, y=110)

#====== Connect to server button =======

btn_connect = Button(FF1, text='connect' , cursor='hand2', fg='black', bd=1, relief=SOLID)
btn_connect.place(x=227, y=49, width=65,height=80)

LL4 = Label(FF1, text='Test server connection', fg='blue')
LL4.place(x=10, y=165)

#==== logo ====
# logo by Vectorsmarket15 Isometric from https://www.flaticon.com/

logo = PhotoImage(file='images/logo.png')
logolabel = Label(root, image=logo)
logolabel.place(x=615,y=45, width =390, height=500)


root.mainloop()

