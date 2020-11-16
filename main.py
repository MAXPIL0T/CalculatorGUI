from tkinter import *
from tkinter import font as tkFont

root = Tk()
root.title("Calculator")
root.wm_iconbitmap('./icon.ico')

helv = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
helv_s = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
helv_b = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)

Output = Entry(root, width=17, font=helv_s)
Output.grid(row=1, column=1, columnspan=3, pady=3, padx=3)

Instructions = Label(root, text="Python GUI\nCalculator\n\nVersion 1.0\n\nThanks for\nusing!\n\nBy Max K.", font=helv_b)
Instructions.grid(row=1, column=4, rowspan=6, padx=10)

def enterVal(value):
    currentVal = Output.get()
    Output.delete(0, END)
    length = len(str(currentVal))
    Output.insert(0, currentVal)
    Output.insert(length, value)

def plusNum():
    global operation
    global val1
    operation = "+"
    val1 = Output.get()
    Output.delete(0, END)

def minusNum():
    global operation
    global val1
    operation = "-"
    val1 = Output.get()
    Output.delete(0, END)

def multNum():
    global operation
    global val1
    operation = "*"
    val1 = Output.get()
    Output.delete(0, END)

def divNum():
    global operation
    global val1
    operation = "/"
    val1 = Output.get()
    Output.delete(0, END)

def equalNum():
    val2 = Output.get()
    Output.delete(0, END)
    if operation == "+":
        result = float(val1) + float(val2)
    elif operation == "-":
        result = float(val1) - float(val2)
    elif operation == "*":
        result = float(val1) * float(val2)
    elif operation == "/":
        try:
            result = float(val1) / float(val2)
        except ZeroDivisionError:
            result = "ZeroDivisionError"
    else:
        result = "Error"
    Output.insert(0, result)

def clearEverything():
    Output.delete(0, END)

Button1 = Button(root, padx=10, pady=5, text="1", font=helv, command=lambda: enterVal(1))
Button2 = Button(root, padx=10, pady=5, text="2", font=helv, command=lambda: enterVal(2))
Button3 = Button(root, padx=10, pady=5, text="3", font=helv, command=lambda: enterVal(3))
Button4 = Button(root, padx=10, pady=5, text="4", font=helv, command=lambda: enterVal(4))
Button5 = Button(root, padx=10, pady=5, text="5", font=helv, command=lambda: enterVal(5))
Button6 = Button(root, padx=10, pady=5, text="6", font=helv, command=lambda: enterVal(6))
Button7 = Button(root, padx=10, pady=5, text="7", font=helv, command=lambda: enterVal(7))
Button8 = Button(root, padx=10, pady=5, text="8", font=helv, command=lambda: enterVal(8))
Button9 = Button(root, padx=10, pady=5, text="9", font=helv, command=lambda: enterVal(9))
Button0 = Button(root, padx=10, pady=5, text="0", font=helv, command=lambda: enterVal(0))
ButtonP = Button(root, padx=10, pady=5, text="+", font=helv, command=plusNum)
ButtonMi = Button(root, padx=10, pady=5, text="-", font=helv, command=minusNum)
ButtonMu = Button(root, padx=10, pady=5, text="*", font=helv, command=multNum)
ButtonD = Button(root, padx=10, pady=5, text="/", font=helv, command=divNum)
ButtonE = Button(root, padx=20, pady=5, text="=", font=helv, command=equalNum)
ButtonCE = Button(root, padx=10, pady=5, text="C", font=helv, command=clearEverything)

Button1.grid(row=2 ,column=1)
Button2.grid(row=2 ,column=2)
Button3.grid(row=2 ,column=3)
Button4.grid(row=3 ,column=1)
Button5.grid(row=3 ,column=2)
Button6.grid(row=3 ,column=3)
Button7.grid(row=4 ,column=1)
Button8.grid(row=4 ,column=2)
Button9.grid(row=4 ,column=3)
Button0.grid(row=5 ,column=1)
ButtonP.grid(row=5 ,column=2)
ButtonMi.grid(row=5 ,column=3)
ButtonMu.grid(row=6 ,column=1)
ButtonD.grid(row=6 ,column=2)
ButtonE.grid(row=7 ,column=1, columnspan=3)
ButtonCE.grid(row=6 ,column=3)

root.mainloop()