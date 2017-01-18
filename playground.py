from Tkinter import *
import tkMessageBox
from datetime import datetime
from threading import *

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
    
def addtolist():
    entrytxt = entry1.get()
    if check4dupe() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0,END)

def addtolist2(event):
    entrytxt = entry1.get()
    if check4dupe() == False:
        listbox1.insert(End, entrytext)
        
    listbox1.insert(END, entrytxt)
    
    entry1.delete(0, END)

def clearlist(event):
    listbox1.delete(0, END)

def check4dupe():
    names = listbox1.get(0, END)
    if entry1.get() in names:
        return True
    else:
        return False
        
def findsize():
    label1.config(text=listbox1.size())

def openfileR():
    clearlist2()
    
    
    
    
    
    



d= datetime.now()
print d
y = d.year
print y
h = d.hour
print h

def generate():
    while(1):
        print "Hello"


thread1 = Thread(target=generate)
#thread1.start()

generate()

root = Tk()
root.title("My first GUI program with Tkinter")

button1 = Button(root, text="Button 1")
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="Go ahead, Master Jouster", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=2, column=2, rowspan=10, sticky=NS)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)
listbox1.bind("<Button-3>", clearlist)

listbox1.insert(END, "Polnareff")
listbox1.insert(END, "Joseph")
listbox1.insert(END, "Jotaro")

findsize()

image = Image.open("ball.jpg")
photo = ImageTk.PhotoImage(image  )

label2 = Label(image=photo)
label2.image = photo
label2.grid(row=12, column=0)


mainloop()