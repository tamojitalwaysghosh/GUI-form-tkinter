from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo

root = tk.Tk()
root.resizable(0, 0)
root.title("Registration Form")

reg = Frame(root)

Fullname = StringVar()
Email = StringVar()


conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()


def database():
    name = Fullname.get()
    email = Email.get()
    gender = var.get()
    branch = c.get()
    prog = var1.get() + var2.get() 
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student ( Fullname TEXT,Email TEXT,Gender TEXT,Branch TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Student (Fullname,Email,Gender,Branch,Programming) VALUES(?,?,?,?,?)',
                   (name, email, gender, branch, prog))
    conn.commit()
    showinfo(title="Student Record", message="Data inserted sucessfully")


def display():
    cursor.execute('SELECT * FROM Student')
    data = cursor.fetchall()
    print(data)
    output = ''
    v=1
    for x in data:
        output = output +str(v)+".  "+ x[0] + '\t' + x[1] + '\t' + x[2] + '\t' + x[3] + ' \t' + x[4] + '\n\n'
        v = v + 1
    print(output)

    return output


def delete(conn, task):
    sql = 'DELETE FROM Student WHERE Fullname =?'
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()
    showinfo(title="Student Reacord", message="Data deleted sucessfully")


def update(task):
    sql = 'UPDATE Student SET Email=?, Gender=?, Branch=?, Programming=? WHERE Fullname = ?'
    cursor.execute(sql, task)
    conn.commit()
    showinfo(title="Student Reacord", message="Data updated sucessfully")


def main():
    name = Fullname.get()
    email = Email.get()
    gender = var.get()
    branch = c.get()
    prog = var1.get() + var2.get() 
    update(name, email, gender, branch, prog)


def delete_task():
    database = r"Form.db"
    conn = sqlite3.connect(database)
    name = Fullname.get()
    with conn:
        delete_task(conn, name)


def case():
    if len(Fullname.get()):
        database()
    else:
        showinfo(
            title='Error',
            message="Fields need to be completed"
        )

canvas1 = tk.Canvas(root, width=1000, height=500, relief='raised', bg="white")
canvas1.pack()

label1 = tk.Label(root, text='Registration Form')
label1.config(font=("bold", 18), bg="white")
canvas1.create_window(250, 30, window=label1)

label2 = tk.Label(root, text='Fullname :')
label2.config(font=('helvetica', 14), bg="white")
canvas1.create_window(65, 90, window=label2)

entry1 = tk.Entry(root, textvar=Fullname, font=(14), borderwidth=2, width=30)
canvas1.create_window(320, 90, window=entry1)

label3 = tk.Label(root, text='E-mail :')
label3.config(font=('helvetica', 14), bg="white")
canvas1.create_window(65, 140, window=label3)

entry2 = tk.Entry(root, textvar=Email, font=(14), borderwidth=2, width=30)
canvas1.create_window(320, 140, window=entry2)

label4 = tk.Label(root, text='Gender :')
label4.config(font=('helvetica', 14), bg="white")
canvas1.create_window(65, 190, window=label4)

var = StringVar()
rd1 = tk.Radiobutton(root, text="Male", padx=5, variable=var, value="Male")
rd1.config(font=('helvetica', 14), bg="white")
canvas1.create_window(200, 190, window=rd1)

rd2 = tk.Radiobutton(root, text="Female", padx=20, variable=var, value="Female")
rd2.config(font=('helvetica', 14), bg="white")
canvas1.create_window(300, 190, window=rd2)

label5 = tk.Label(root, text='Branch :')
label5.config(font=('helvetica', 14), bg="white")
canvas1.create_window(65, 240, window=label5)

list1 = ['CSE', 'IT', 'ECE', 'EE']
c = StringVar()
droplist = tk.OptionMenu(root, c, *list1)
droplist.config(font=('helvetica', 14), bg="white", width=27)
c.set('Select your branch')
canvas1.create_window(320, 240, window=droplist)

label6 = tk.Label(root, text='Elective :')
label6.config(font=('helvetica', 14), bg="white")
canvas1.create_window(65, 290, window=label6)

var1 = StringVar()
cb1 = tk.Checkbutton(root, text="App Dev", variable=var1)
cb1.config(font=('helvetica', 14), bg="white")
canvas1.create_window(200, 290, window=cb1)

var2 = StringVar()
cb2 = tk.Checkbutton(root, text="Web Dev", variable=var2)
cb2.config(font=('helvetica', 14), bg="white")
canvas1.create_window(320, 290, window=cb2)



button1 = tk.Button(text=' Submit ', command=case, bg='black', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 350, window=button1)

button2 = tk.Button(text=' Display ', command=lambda: (text.delete(1.0, END), text.insert(END, display())), bg='black',
                    fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 350, window=button2)

#button3 = tk.Button(text=' Update ', command=main, bg='black', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 450, window=button3)

#button4 = tk.Button(text=' Delete ', command=delete_task, bg='black', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(300, 450, window=button4)

text = tk.Text(root, height=25, width=50)
text.config(font=('helvetica', 12), bg="white")
canvas1.create_window(750, 270, window=text)

lblDisplay = tk.Label(root, text="Student Data")
lblDisplay.config(font=('Helvetica', 18, 'bold'), fg='black', justify=CENTER, bg="white")
canvas1.create_window(750, 25, window=lblDisplay)


def iExit():
    iExit = tk.messagebox.askyesno("Exit", "Do you want to exit ?")
    if iExit > 0:
        root.destroy()
        return


def Data():
    root.resizable(width=False, height=False)
    root.geometry("1000x500+0+0")


def Form():
    root.resizable(width=False, height=False)
    root.geometry("500x500+0+0")


menubar = Menu(reg)





filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Form", command=Form)
filemenu.add_command(label="Data", command=Data)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)
root.config(menu=menubar)

mainloop()
