from tkinter import *

calc=Tk()
calc.geometry("397x460")
calc.resizable(0,0)
calc.title("Calculator")

#defining funxtions for different actions
def click(t):
    global exp
    exp+=str(t)
    text1.set(exp)
    
def clear_btn():
    global ex
    exp=""
    text1.set(exp)
    
def equal_btn():
    global exp
    ans=str(eval(exp))
    text1.set(ans)
    exp=""


#setting frames and variables
text1=StringVar()
exp=""
colour1="#a3a8ad"
colour2="#c9d0d6"
f1=("Frutiger",11,"bold")
f2=("Futura", 16,"bold")
fg1="#554f57"
frame1=Frame(calc,width=400,height=50)
frame1.pack()
screen1=Entry(frame1,textvariable=text1,width=65,font=f2)
screen1.pack(ipady=10)
frame2=Frame(calc,width=400,height=350,bg="grey")
frame2.pack()

#setting buttons
clear = Button(frame2, text = "C", font=f1 ,fg =fg1, width = 32, height = 4, bd = 0, bg = colour1, cursor = "hand2", command = lambda: clear_btn())
clear.grid(row = 1, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(frame2, text = "/", font=f1, fg =fg1, width = 10, height = 4, bd = 0, bg = colour1, cursor = "hand2", command = lambda: click("/"))
divide.grid(row = 1, column = 3, padx = 1, pady = 1)
seven = Button(frame2, text = "7", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(7))
seven.grid(row = 2, column = 0, padx = 1, pady = 1)
eight = Button(frame2, text = "8", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(8))
eight.grid(row = 2, column = 1, padx = 1, pady = 1)
nine = Button(frame2, text = "9", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(9))
nine.grid(row = 2, column = 2, padx = 1, pady = 1)
multiply = Button(frame2, text = "*", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour1, cursor = "hand2", command = lambda: click("*"))
multiply.grid(row = 2, column = 3, padx = 1, pady = 1)
four = Button(frame2, text = "4", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(4))
four.grid(row = 3, column = 0, padx = 1, pady = 1)
five = Button(frame2, text = "5", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(5))
five.grid(row = 3, column = 1, padx = 1, pady = 1)
six = Button(frame2, text = "6", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(6))
six.grid(row = 3, column = 2, padx = 1, pady = 1)
subtract = Button(frame2, text = "-", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg =colour1, cursor = "hand2", command = lambda: click("-"))
subtract.grid(row = 3, column = 3, padx = 1, pady = 1)
one = Button(frame2, text = "1", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(1))
one.grid(row = 4, column = 0, padx = 1, pady = 1)
two = Button(frame2, text = "2", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(2))
two.grid(row = 4, column = 1, padx = 1, pady = 1)
three = Button(frame2, text = "3", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(3))
three.grid(row = 4, column = 2, padx = 1, pady = 1)
add = Button(frame2, text = "+", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour1, cursor = "hand2", command = lambda: click("+"))
add.grid(row = 4, column = 3, padx = 1, pady = 1)
zero = Button(frame2, text = "0", font=f1, fg = fg1, width = 21, height = 4, bd = 0, bg = colour2, cursor = "hand2", command = lambda: click(0))
zero.grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(frame2, text = ".", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg =colour2, cursor = "hand2", command = lambda: click("."))
point.grid(row = 5, column = 2, padx = 1, pady = 1)
equal = Button(frame2, text = "=", font=f1, fg = fg1, width = 10, height = 4, bd = 0, bg = colour1, cursor = "hand2", command = lambda: equal_btn())
equal.grid(row = 5, column = 3, padx = 1, pady = 1)
 
calc.mainloop()