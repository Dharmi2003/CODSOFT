#Dharmishtha Chandegara
#Contact Book using Tkinter

from tkinter import *
from tkinter import messagebox


# Initialize window
root = Tk()
root.geometry('900x700')
root.config(bg = '#d3f3f5')
root.title("Task 5")
root.resizable(0,0)
contactlist = []

Name = StringVar()
Num = StringVar()
Email = StringVar()
Add = StringVar()


#Create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=10,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


#Get selected value
def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
    
#Add new contact
def AddContact():
    if Name.get()!="" and Num.get()!="" and Email.get()!="" and Add.get()!="":
        contactlist.append([Name.get() ,Num.get(), Email.get(), Add.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error","Please fill the information")


#Edit existing contact
def UpdateDetail():
	if Name.get() and Num.get() and Email.get() and Add.get():
		contactlist[Selected()] = [Name.get(), Num.get(), Email.get(), Add.get()]
    

		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Num.get()) and not(Email.get()) and not(Add.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)

def EntryReset():
	Name.set(''), Num.set(''), Email.set(''), Add.set('')
    

#Delete selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
# func to view contact
def VIEW():
    NAME, PHONE, EMAIL, ADD = contactlist[Selected()]
    Name.set(NAME), Num.set(PHONE), Email.set(EMAIL), Add.set(ADD)
        

#function to exit game window   
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,email,add in contactlist :
        select.insert (END, name)
Select_set()


#Define labels and entry widget 
Label(root, text = 'Store Name: ', font=("Times new roman",25,"bold"), bg = 'LightGray').place(x= 30, y=20)
Entry(root, textvariable = Name, font=("Times new roman",20), width=30).place(x= 300, y=20)

Label(root, text = 'Contact: ', font=("Times new roman",22,"bold"),bg = 'LightGray').place(x= 30, y=70)
Entry(root, textvariable = Num, font=("Times new roman",20), width=30).place(x= 300, y=70)

Label(root, text = 'Email: ', font=("Times new roman",22,"bold"),bg = 'LightGray').place(x= 30, y=120)
Entry(root, textvariable = Email, font=("Times new roman",20), width=30).place(x= 300, y=120)

Label(root, text = 'Address: ', font=("Times new roman",22,"bold"),bg = 'LightGray').place(x= 30, y=170)
Entry(root, textvariable = Add, font=("Times new roman",20), width=30).place(x= 300, y=170)




#Define Buttons
Button(root,text=" ADD", font=("Times new roman", 18, 'bold'), bg='#e8c1c7', command = AddContact, padx=20). place(x= 50, y=300)

Button(root,text="UPDATE", font=("Times new roman", 18, 'bold'), bg='#e8c1c7',command = UpdateDetail, padx=20).place(x= 300, y=300)

Button(root,text="VIEW", font=("Times new roman", 18, 'bold'), bg='#e8c1c7', command = VIEW, padx=20).place(x= 50, y=400)

Button(root,text="DELETE", font=("Times new roman", 18, 'bold'), bg='#e8c1c7',command = Delete_Entry, padx=20).place(x= 300, y=400)

Button(root,text="RESET", font=("Times new roman", 18, 'bold'), bg='#e8c1c7', command = EntryReset,padx=20).place(x= 170, y=500)

Button(root,text="EXIT", font=("Times new roman", 18, 'bold'), bg='tomato', command = EXIT, padx=20).place(x= 180, y=600)

root.mainloop()
  
