#importing the library
import tkinter as tk
from tkinter import *  
from tkinter.messagebox import showinfo

#create an instance of tkinter frame
top = Tk()  

top.title("Form")

#define size of window or frame
top.geometry("400x400")  
head = Label(top, text = "IDENTITY FORM",fg="white",bg="blue").place(x = 100,y = 10)  

name = Label(top, text = "Name:").place(x = 30,y = 50)  
email = Label(top, text = "Father's Name:").place(x = 30, y = 90)  
password = Label(top, text = "College:").place(x = 30, y = 130)
phone = Label(top, text = "Phone No.:").place(x = 30, y = 170) 
age = Label(top, text = "Date of Birth:").place(x = 30, y = 210)  
e1 = Entry(top).place(x = 150, y = 50)  
e2 = Entry(top).place(x = 150, y = 90)  
e3 = Entry(top).place(x = 150, y = 130)
e4 = Entry(top).place(x = 150, y = 170) 
e5 = Entry(top).place(x = 150, y = 210)

def show():
    showinfo(
        title='Result',
        message="Form Submitted"
    )
    

btn = tk.Button(top, text = 'Submit', bd = '5',command = show)
btn.pack(side = "bottom")


top.mainloop()  
