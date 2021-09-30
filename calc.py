from functools import partial
from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation,font=("arial",20,"bold"))
    expression_field.grid(row=0,column=0,columnspan=4,sticky="NWSE")
    l1=[1,2,3,'+',4,5,6,'-',7,8,9,'*',0,'clear','=','/','.']
    cnt=0
    for i in range(1,5):
        for j in range(4):
            if l1[cnt]=='=':
                b1=Button(gui,text=l1[cnt], fg='black', bg='cyan',command=equalpress,font=("arial",20,"bold"))
            elif l1[cnt]=='clear':
                b1=Button(gui,text=l1[cnt], fg='black', bg='cyan',command=clear,font=("arial",20,"bold"))
            else:
                f1 = partial(press, l1[cnt])
                b1=Button(gui,text=l1[cnt], fg='black', bg='cyan',command=f1,font=("arial",20,"bold"))

            b1.grid(row=i, column=j,sticky="NWSE")
            cnt+=1
    Decimal= Button(gui, text='.', fg='black', bg='cyan',
	    command=lambda: press('.'),font=("arial",20,"bold"))
    Decimal.grid(row=5, column=0,sticky="NWSE")
    gui.geometry("400x400")        

    for i in range(6):
        gui.rowconfigure(i,weight=1)
    for i in range(4):
        gui.columnconfigure(i,weight=1)
    gui.mainloop()
