#run using 'python3 linuxcalculator-latest.py' or 'python linuxcalculator-latest.py'

print("   _   _   _   _   _     _   _   _   _   _   _   _   _   _   _  ")
print("  / \\ / \\ / \\ / \\ / \\   / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ ")
print(" ( L | i | n | u | x ) ( C | a | l | c | u | l | a | t | o | r )")
print("  \\_/ \\_/ \\_/ \\_/ \\_/   \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ ")

from tkinter import *
from tkinter import messagebox
version = 1.0
expression = ""
print(version)
def enter(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)
def total():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
if __name__ == "__main__":
    layoutSelect = True
    root = Tk()
    root.configure(background = "light grey")
    root.title("Linux Calculator")
    root.geometry("360x230")
    messagebox.showwarning(title = "WARNING", message = "BETA VERSION!! BUGS CAN OCCOR!")
    equation = StringVar()
    Label(root, text = "Linux Calculator", bg = "light grey").grid(row = 0, column = 0)
    expressionField = Entry(root, textvariable = equation)
    expressionField.grid(row=1, columnspan = 4, ipadx = 70)
    button1 = Button(root, text = " 1 ", fg = "black", bg = "white", command = lambda: enter(1), height = 1, width = 7)
    button1.grid(row = 2, column = 0)
    button2 = Button(root, text = " 2 ", fg = "black", bg = "white", command = lambda: enter(2), height = 1, width = 7)
    button2.grid(row = 2, column = 1)
    button3 = Button(root, text = " 3 ", fg = "black", bg = "white", command = lambda: enter(3), height = 1, width = 7)
    button3.grid(row = 2, column = 2)
    button4 = Button(root, text = " 4 ", fg = "black", bg = "white", command = lambda: enter(4), height = 1, width = 7)
    button4.grid(row = 3, column = 0)
    button5 = Button(root, text = " 5 ", fg = "black", bg = "white", command = lambda: enter(5), height = 1, width = 7)
    button5.grid(row = 3, column = 1)
    button6 = Button(root, text = " 6 ", fg = "black", bg = "white", command = lambda: enter(6), height = 1, width = 7)
    button6.grid(row = 3, column = 2)
    button7 = Button(root, text = " 7 ", fg = "black", bg = "white", command = lambda: enter(7), height = 1, width = 7)
    button7.grid(row = 4, column = 0)
    button8 = Button(root, text = " 8 ", fg = "black", bg = "white", command = lambda: enter(8), height = 1, width = 7)
    button8.grid(row = 4, column = 1)
    button9 = Button(root, text = " 9 ", fg = "black", bg = "white", command = lambda: enter(9), height = 1, width = 7)
    button9.grid(row = 4, column = 2)
    button0 = Button(root, text = " 0 ", fg = "black", bg = "white", command = lambda: enter(0), height = 1, width = 7)
    button0.grid(row = 5, column = 1)
    buttonPlus = Button(root, text = " + ", fg = "black", bg = "white", command = lambda: enter("+"), height = 1, width = 7)
    buttonPlus.grid(row = 2, column = 3)
    buttonMinus = Button(root, text = " - ", fg = "black", bg = "white", command = lambda: enter("-"), height = 1, width = 7)
    buttonMinus.grid(row = 3, column = 3)
    buttonMultiply = Button(root, text = " ÷ ", fg = "black", bg = "white", command = lambda: enter("/"), height = 1, width = 7)
    buttonMultiply.grid(row = 4, column = 3)
    buttonDivide = Button(root, text = " × ", fg = "black", bg = "white", command = lambda: enter("*"), height = 1, width = 7)
    buttonDivide.grid(row = 5, column = 3)
    ButtonEqual = Button(root, text = ' = ', fg = 'black', bg = 'white', command = total, height = 1, width = 7) 
    ButtonEqual.grid(row = 5, column = 2)
    ButtonClear = Button(root, text = 'Clear', fg = 'black', bg = 'white', command = clear, height = 1, width = 7) 
    ButtonClear.grid(columnspan = 4, ipadx = 70)
    ButtonDecimal = Button(root, text='.', fg = 'black', bg = 'white', command = lambda: enter('.'), height = 1, width = 7) 
    ButtonDecimal.grid(row = 5, column = 0)
    root.mainloop()
