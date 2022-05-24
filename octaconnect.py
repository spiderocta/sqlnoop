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

L = Label(F1, text='Show Databases')
L.place(x=10, y=50)

showAllDataBasesButton = Button(F1, text='All Databases' , cursor='hand2')
showAllDataBasesButton.place(x=105, y=47, width=125)

hieAllDataBasesButton = Button(F1, text='Hide' , cursor='hand2')
hieAllDataBasesButton.place(x= 235, y=47, width=55)


# databases names section 
root.mainloop()

