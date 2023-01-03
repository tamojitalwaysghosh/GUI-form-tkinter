#importing the library
import tkinter as tk
from tkinter import *  
from tkinter.messagebox import showinfo

#create an instance of tkinter frame
top = Tk()  
top.geometry('1500x1500')
top.resizable(0,0)

top.title("Form")

#define size of window or frame
top.geometry("400x400")  
head = Label(top, text = "IDENTITY FORM",fg="white",bg="blue").place(x = 100,y = 10)  

name = Label(top, text = "Name:").place(x = 30,y = 50)  
email = Label(top, text = "Father's Name:").place(x = 30, y = 90)  
password = Label(top, text = "College:").place(x = 30, y = 130)
phone = Label(top, text = "Phone No.:").place(x = 30, y = 170) 
age = Label(top, text = "Date of Birth:").place(x = 30, y = 210)  
dept = Label(top, text = "Dept.:").place(x = 30, y = 280)
gender = Label(top, text = "Gender:").place(x = 30, y = 250) 
e1 = Entry(top).place(x = 150, y = 50)  
e2 = Entry(top).place(x = 150, y = 90)  
e3 = Entry(top).place(x = 150, y = 130)
e4 = Entry(top).place(x = 150, y = 170) 
e5 = Entry(top).place(x = 150, y = 210)

var2 = IntVar()
var3=StringVar()
var1= IntVar()
var4=IntVar()
var=IntVar()


Radiobutton(top, text="Male",padx = 5, variable=var, value=1).place(x=100,y=250)
Radiobutton(top, text="Female",padx = 20, variable=var, value=2).place(x=200,y=250)

Radiobutton(top, text="CSE", variable=var1,value=1).place(x=100,y=280)
Radiobutton(top, text="IT", variable=var1,value=2).place(x=150,y=280)
Radiobutton(top, text="ECE", variable=var1,value=3).place(x=200,y=280)
Radiobutton(top, text="EE", variable=var1,value=4).place(x=250,y=280)

Checkbutton(top, text="agreed to the terms and conditions", variable=var2).place(x=60,y=330)


def show():
    showinfo(
        title='Result',
        message="Form Submitted"
    )
    
Button(top, text='Submit',width=20,bg='brown',fg='white',command=show).place(x=100,y=350)



top.mainloop()  
