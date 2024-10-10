from tkinter import *
import tkinter.messagebox

# ---------------------------settings-------------------------------------
root = Tk()
root.geometry('600x400')
root.title('Calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ---------------------------variables------------------------------------
num1 = ""
num2 = ""
operator = ""
res_value = StringVar()

# ---------------------------frames---------------------------------------
top_display = Frame(root, width=400, height=50, bg=color)
top_display.pack(side=TOP)

top_buttons = Frame(root, width=400, height=250, bg=color)
top_buttons.pack(side=TOP)


# ---------------------------functions------------------------------------
def btn_click(value):
    global num1, num2, operator
    if operator == "":
        num1 += value
        res_value.set(num1)
    else:
        num2 += value
        res_value.set(num2)


def btn_operator(op):
    global operator
    if num1 != "":
        operator = op
        res_value.set(op)


def calculate():
    global num1, num2, operator, result
    try:
        if operator == "+":
            result = float(num1) + float(num2)
        elif operator == "-":
            result = float(num1) - float(num2)
        elif operator == "*":
            result = float(num1) * float(num2)
        elif operator == "/":
            if float(num2) == 0:
                errormsg('division zero error')
                return
            result = float(num1) / float(num2)
        res_value.set(result)
        num1 = str(result)
        num2 = ""
        operator = ""
    except:
        errormsg('error')


def clear():
    global num1, num2, operator
    num1 = ""
    num2 = ""
    operator = ""
    res_value.set("")


def errormsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'Something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Cannot divide by 0')


# ---------------------------display---------------------------------------
display = Entry(top_display, textvariable=res_value, font=('arial', 20, 'bold'), bd=20, insertwidth=4,
                bg="powder blue", justify='right')
display.pack()

# ---------------------------number buttons--------------------------------
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row = 0
col = 0
for button in buttons:
    if button.isdigit():
        Button(top_buttons, text=button, padx=20, pady=20, font=('arial', 15, 'bold'),
               command=lambda b=button: btn_click(b)).grid(row=row, column=col)
    elif button == 'C':
        Button(top_buttons, text=button, padx=20, pady=20, font=('arial', 15, 'bold'),
               command=clear).grid(row=row, column=col)
    elif button == '=':
        Button(top_buttons, text=button, padx=20, pady=20, font=('arial', 15, 'bold'),
               command=calculate).grid(row=row, column=col)
    else:
        Button(top_buttons, text=button, padx=20, pady=20, font=('arial', 15, 'bold'),
               command=lambda b=button: btn_operator(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
