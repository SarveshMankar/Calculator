from tkinter import *

root=Tk()

root.title("Calculator ~by Sam Tech😎")

global lst
lst=[]
global flag
flag=0

def calculate(lst):
    b=lst

    for i in b:
        while '/' in b:
            for j in b:
                if j=="/":
                    o=b.index('/')
                    n2=b.pop(o+1)
                    n1=b.pop(o-1)
                    ans=float(n1)/float(n2)
                    extra=[str(ans)]
                    b=b[:o-1]+extra+b[o:]

    for i in b:
        while '*' in b:
            for j in b:
                if j=="*":
                    o=b.index('*')
                    n2=b.pop(o+1)
                    n1=b.pop(o-1)
                    ans=float(n1)*float(n2)
                    extra=[str(ans)]
                    b=b[:o-1]+extra+b[o:]

    for i in b:
        while '+' in b:
            for j in b:
                if j=="+":
                    o=b.index('+')
                    n2=b.pop(o+1)
                    n1=b.pop(o-1)
                    ans=float(n1)+float(n2)
                    extra=[str(ans)]
                    b=b[:o-1]+extra+b[o:]

    while '-' in b:
        while '-' in b:
            for j in b:
                if j=="-":
                    o=b.index('-')
                    n2=b.pop(o+1)
                    n1=b.pop(o-1)
                    ans=float(n1)-float(n2)
                    extra=[str(ans)]
                    b=b[:o-1]+extra+b[o:]

    return float(b[0])

def click(num):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur) + str(num))
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def clear():
    global lst
    lst=[]
    global flag
    flag=0
    e.delete(0,END)
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def add():
    first=e.get()
    e.delete(0,END)
    lst.append(str(first))
    lst.append('+')
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def sub():
    first=e.get()
    e.delete(0,END)
    lst.append(str(first))
    lst.append('-')
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)  

def mul():
    first=e.get()
    e.delete(0,END)
    lst.append(str(first))
    lst.append('*')
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def div():
    first=e.get()
    e.delete(0,END)
    lst.append(str(first))
    lst.append('/')
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def equal():
    second=e.get()
    e.delete(0,END)
    global lst
    lst.append(second)

    try:
        while True:
            lst.remove('')
    except:
        pass
    print(lst)

    if lst[0]=='+' or lst[0]=='-':
        lst[1]=lst[0]+lst[1]
        lst[0]=''

    for i in range(0,len(lst)-2):
        if lst[i]=='*' or lst[i]=='/' or lst[i]=='(':
            if lst[i+1]=='-' or lst[i+1]=='+':
                lst[i+1]=str(lst[i+1])+str(lst[i+2])
                lst[i+2]=''

    try:
        while True:
            lst.remove('')
    except:
        pass
    print(lst)

    op=0
    cl=0
    for i in lst:
        if i=='(':
            op+=1
        elif i==')':
            cl+=1

    if op==cl:
        a='(' in lst
        b=')' in lst
        while a:
            for i in range(len(lst)):
                if lst[i]=='(':
                    o1=i

            for i in range(len(lst)):
                if lst[i]==')':
                    o2=i
                    if o2>o1:
                        break
            
            lst=lst[0:o1]+[calculate(lst[o1+1:o2])]+lst[o2+1:]
            if '(' not in lst:
                a=False

        ans=calculate(lst)
    else:
        print('Syntax Error!')

    e.insert(0,str(ans))
    lst=[]
    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)

def backspace():
    h=e.get()
    h=str(h[:-1])
    e.delete(0,END)
    e.insert(0,str(h))

def brac():
    global flag

    first=e.get()
    e.delete(0,END)
    if first!="":
        lst.append(str(first))

    if lst==[]:
        lst.append('(')
        flag-=1

    elif lst[-1]=='+' or lst[-1]=='-' or lst[-1]=='*' or lst[-1]=='/':
        lst.append('(')
        flag-=1

    elif (lst[-1]!='+' or lst[-1]!='-' or lst[-1]!='*' or lst[-1]!='/') and flag<0:
        lst.append(')')
        flag+=1

    elif (lst[-1]!='+' or lst[-1]!='-' or lst[-1]!='*' or lst[-1]!='/') and flag==0:
        lst.append('*')
        lst.append('(')
        flag-=1

    elif (lst[-1]!='+' or lst[-1]!='-' or lst[-1]!='*' or lst[-1]!='/') and flag<0:
        lst.append(')')
        flag+=1

    e1.configure(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,str(''.join(lst)))
    e1.configure(state=DISABLED)


e=Entry(root,width=56,borderwidth=5,bg="Silver")
e1=Entry(root,width=56,borderwidth=5,bg="Silver")
e1.configure(state=DISABLED)

button1=Button(root,text="1",width=8,padx=10,pady=10,bg="White",command=lambda: click(1))
button2=Button(root,text="2",width=9,padx=10,pady=10,bg="White",command=lambda: click(2))
button3=Button(root,text="3",width=8,padx=10,pady=10,bg="White",command=lambda: click(3))
button4=Button(root,text="4",width=9,padx=10,pady=10,bg="White",command=lambda: click(4))
button5=Button(root,text="5",width=8,padx=10,pady=10,bg="White",command=lambda: click(5))
button6=Button(root,text="6",width=9,padx=10,pady=10,bg="White",command=lambda: click(6))
button7=Button(root,text="7",width=8,padx=10,pady=10,bg="White",command=lambda: click(7))
button8=Button(root,text="8",width=9,padx=10,pady=10,bg="White",command=lambda: click(8))
button9=Button(root,text="9",width=8,padx=10,pady=10,bg="White",command=lambda: click(9))
button0=Button(root,text="0",width=9,padx=10,pady=10,bg="White",command=lambda: click(0))

button_eq=Button(root,text="=",width=21,padx=10,pady=10,bg="White",command= equal)
button_clr=Button(root,text="Clear",width=8,padx=10,pady=10,bg="White",command=clear)
button_exit=Button(root,text="Backspace",width=8,padx=10,pady=10,command=backspace,bg="White")
button_add=Button(root,text="+",width=9,padx=10,pady=10,bg="White",command=add)
button_sub=Button(root,text="-",width=8,padx=10,pady=10,bg="White",command=sub)
button_mul=Button(root,text="*",width=9,padx=10,pady=10,bg="White",command=mul)
button_div=Button(root,text="/",width=8,padx=10,pady=10,bg="White",command=div)
button_dot=Button(root,text=".",width=9,padx=10,pady=10,bg="White",command= lambda:click("."))
button_brac=Button(root,text="( )",width=9,padx=10,pady=10,bg="White",command=brac)

e.grid(row=1,column=0,columnspan=5)
e1.grid(row=0,column=0,columnspan=5)

button_brac.grid(row=2,column=0)
button_eq.grid(row=2,column=1,columnspan=2)
button_clr.grid(row=2,column=3)
button_exit.grid(row=6,column=3)

button_add.grid(row=3,column=0)
button_sub.grid(row=3,column=1)
button_mul.grid(row=3,column=2)
button_div.grid(row=3,column=3)
button_dot.grid(row=6,column=2)

button0.grid(row=4,column=0)
button1.grid(row=4,column=1)
button2.grid(row=4,column=2)
button3.grid(row=4,column=3)
button4.grid(row=5,column=0)
button5.grid(row=5,column=1)
button6.grid(row=5,column=2)
button7.grid(row=5,column=3)
button8.grid(row=6,column=0)
button9.grid(row=6,column=1)

root.mainloop()
