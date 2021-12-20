from tkinter import *
import datetime

def check_it():
    file = open("usom.txt","r")
    content =file.read()
    file.close()
    ip = entry1.get()
    today = datetime.datetime.now()
    if str(ip) in content:
        file = open ("log.txt","a")
        text = str(ip) +  "DAMAGE -- \nDate :" + str(today) + "\n"
        file.write(text)
        file.close()
        
        v.set("IP DAMAGED")
        
    else:
        file = open ("log.txt","a")
        text = str(ip) +  "NOT DAMAGE -- \nDate :" + str(today) + "\n"
        file.write(text)
        file.close()
        
        
        v.set("IP NOT DAMAGED")

top = Tk()

top.title("USOM IP CONTROL")

B = Button(top,text="Check It",command=check_it)
B.place(x=50,y=50)
B.pack()

label1=Label(top,text="Enter the ip address to check : ")
label1.pack()

entry1 = Entry(top)
entry1.place(x=50,y=90)
entry1.pack()

v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()

top.mainloop()