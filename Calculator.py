from tkinter import *

root=Tk()

root.title("Calculator ~by Sam Tech")

def click(num):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur) + str(num))

def clear():
    e.delete(0,END)

def add():
    first=e.get()
    global f
    f=float(first)
    global o
    o = "Add"
    e.delete(0,END)

def sub():
    first=e.get()
    global f
    f=float(first)
    global o
    o = "Subtract"
    e.delete(0,END)

def mul():
    first=e.get()
    global f
    f=float(first)
    global o
    o = "Multiply"
    e.delete(0,END)

def div():
    first=e.get()
    global f
    f=float(first)
    global o
    o = "Divide"
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)
    if o=="Add":
        e.insert(0,f+float(second))

    if o=="Subtract":
        e.insert(0,f-float(second))

    if o=="Multiply":
        e.insert(0,f*float(second))

    if o=="Divide":
        e.insert(0,f/float(second))
        
e=Entry(root,width=56,borderwidth=5,bg="Light Green")

button1=Button(root,text="1",width=8,padx=10,pady=10,bg="Orange",command=lambda: click(1))
button2=Button(root,text="2",width=9,padx=10,pady=10,bg="Orange",command=lambda: click(2))
button3=Button(root,text="3",width=8,padx=10,pady=10,bg="Orange",command=lambda: click(3))
button4=Button(root,text="4",width=9,padx=10,pady=10,bg="Orange",command=lambda: click(4))
button5=Button(root,text="5",width=8,padx=10,pady=10,bg="Orange",command=lambda: click(5))
button6=Button(root,text="6",width=9,padx=10,pady=10,bg="Orange",command=lambda: click(6))
button7=Button(root,text="7",width=8,padx=10,pady=10,bg="Orange",command=lambda: click(7))
button8=Button(root,text="8",width=9,padx=10,pady=10,bg="Orange",command=lambda: click(8))
button9=Button(root,text="9",width=8,padx=10,pady=10,bg="Orange",command=lambda: click(9))
button0=Button(root,text="0",width=9,padx=10,pady=10,bg="Orange",command=lambda: click(0))

button_eq=Button(root,text="=",width=21,padx=10,pady=10,bg="Blue",command= equal)
button_clr=Button(root,text="Clear",width=21,padx=10,pady=10,bg="Blue",command=clear)
button_exit=Button(root,text="Exit",width=8,padx=10,pady=10,command=root.destroy,bg="Pink")
button_add=Button(root,text="+",width=9,padx=10,pady=10,bg="Yellow",command=add)
button_sub=Button(root,text="-",width=8,padx=10,pady=10,bg="Yellow",command=sub)
button_mul=Button(root,text="*",width=9,padx=10,pady=10,bg="Yellow",command=mul)
button_div=Button(root,text="/",width=8,padx=10,pady=10,bg="Yellow",command=div)
button_dot=Button(root,text=".",width=9,padx=10,pady=10,bg="Orange",command= lambda:click("."))

e.grid(row=0,column=0,columnspan=5)


button_eq.grid(row=1,column=0,columnspan=2)
button_clr.grid(row=1,column=2,columnspan=2)
button_exit.grid(row=5,column=3)

button_add.grid(row=2,column=0)
button_sub.grid(row=2,column=1)
button_mul.grid(row=2,column=2)
button_div.grid(row=2,column=3)
button_dot.grid(row=5,column=2)

button0.grid(row=3,column=0)
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button7.grid(row=4,column=3)
button8.grid(row=5,column=0)
button9.grid(row=5,column=1)

root.mainloop()
