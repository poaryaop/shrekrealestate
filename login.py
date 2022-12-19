from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import sqlite3


def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return


conn = sqlite3.connect("database.db")
c = conn.cursor()


tkWindow = Tk()  
tkWindow.geometry('600x500')  
tkWindow.title('amlakie sherek')

frame = Frame(tkWindow, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("shrek.jpg"))

label = Label(frame, image = img)

usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

label.pack()

tkWindow.mainloop()