#Dharmishtha Chandegara
#Random Password Generator usin Tkinter

import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

#Variables
root = Tk()
root.geometry('700x500')
root.resizable(0,0)

var = IntVar()
var1 = IntVar()

root.title("Task 3")


#Create Label and Entry
random_pw = Label(root, text="Password: ", font=("Times new roman",20,"bold"))
random_pw.grid(row=0, column=0)

entry = Entry(root, font=("Times new roman",20))
entry.grid(row=1, column=0)

pw_label = Label(root, text="Length: ", font=("Times new roman",20,"bold"))
pw_label.grid(row=0, column=2)

#entry1 = Entry(root, font=("Times new roman",20))
#entry1.grid(row=6, column=1)


combo = Combobox(root, textvariable=var1, font=("Times new roman",18,"bold"))

combo['value'] = (7,8,9,10,11,12,13,14,15,16,
                  17,18,19,20,21,22,23,24,25,
                  26,27,28,29,30,31,32,"Length")

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(row=1, column=2)

def low():
    entry.delete(0, END)
    
    #Get Length of PW
    length = var1.get()
    
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    pw = " "
    
    if var.get()==1:
        for i in range(0, length):
            pw = pw + random.choice(lower)
        return pw
    
    elif var.get()==0:
        for i in range(0, length):
            pw = pw + random.choice(upper)
        return pw
    
    elif var.get()==2:
        for i in range(0, length):
            pw = pw + random.choice(digits)
        return pw
    
    else:
        messagebox.showerror("Error", "Please Choose an Option.")
        
def create():
    pw1 = low()
    entry.insert(10, pw1)
    
    messagebox.showinfo("Success", "Password Created Successfully!")
    
def copyy():
    random_pw = entry.get()
    pyperclip.copy(random_pw)
    
    messagebox.showinfo("Confirmation", "Password Copied Successfully!")
   
def exit():
    root.destroy()
   

       
#Radio button for deciding choice
radio_low = Radiobutton(root, text="Low", variable=var, value=1) 
radio_low.grid(row=6, column=0,padx=30, pady=30)


radio_mid = Radiobutton(root, text="Medium", variable=var, value=0) 
radio_mid.grid(row=6, column=1)

radio_strong = Radiobutton(root, text="Strong", variable=var, value=2) 
radio_strong.grid(row=6, column=2)


#Creating buttons
copy_btn = Button(root, text="COPY", command=copyy)
copy_btn.grid(row=10, column=0,padx=20, pady=20)

create_btn = Button(root, text="GENERATE", command=create)
create_btn.grid(row=10, column=1)

exit_btn = Button(root, text="EXIT", command=exit)
exit_btn.grid(row=10, column=2)
    
root.mainloop()





