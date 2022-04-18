from email.mime import text
from tkinter import*
from tkinter import font

root=Tk()
root.title("chatbox")
lable=Label(text="My New GUI App!",fg="blue",)
lable.pack(side="top")
def send():
    send="You ->"+e.get()
    t.insert(END,"\n"+send)
    if(e.get()=="Hello"or e.get()=="hello"or e.get()=="Hi"or e.get()=="hi"):
        t.insert(END,"\n"+"Me ->hi")
    elif(e.get()=="How are you?"or e.get()=="how are you?"or e.get()=="HOW ARE YOU?"):
        t.insert(END,"\n"+"Me ->I am fine")
    elif(e.get()=="What are you doing in studies?"or e.get()=="what are you doing in studies?"or e.get()=="what are yuou doing"):
        t.insert(END,"\n"+"Me->I am doing Softer Engineering")
    elif(e.get()=="Now what do you want to do in future"):
        t.insert(END,"\n"+"I want to become a frontend devoloper")
    else:
        t.insert(END,"\n"+"Sorry i didn't get you?")
    e.delete(0,END)
t=Text(root)
t.pack(padx=60,pady=20)
e=Entry(width=150,bg="spring green",fg="black",relief="raised")
send=Button(root,text="send",fg="red",command=send).pack(side="right")

e.pack()
root.mainloop()
    