from tkinter import *

root = Tk()

# Apps title
root.title("Calculator")

# Adding color to the whole window
root.configure()

# Adding functionality to the calculator
i = 0


def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


# Adding functionality for operator signs
def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# Adding functionality of factorial button



def factorial():
    whole_string = display.get()
    num = int(whole_string)
    counter = num
    fact = 1
    try:
        while counter > 0:
            fact = fact * counter
            counter -= 1
            clear_all()
            display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")



# Adding functionality for calculation
def calculate():
    try:
        result = eval(str(display.get()))
        clear_all()
        display.insert(0, result)

    except Exception:
        clear_all()
        display.insert(0, "Error")


# Adding function for AC button
def clear_all():
    display.delete(0, END)


# Adding functionality for the <- button
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


# Adding the Entry
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# Adding buttons to the window
Button(root, text="1", width=5, command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2", width=5, command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3", width=5, command=lambda: get_variable(3)).grid(row=2, column=2)

Button(root, text="4", width=5, command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", width=5, command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", width=5, command=lambda: get_variable(6)).grid(row=3, column=2)

Button(root, text="7", width=5, command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8", width=5, command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9", width=5, command=lambda: get_variable(9)).grid(row=4, column=2)

# Adding other buttons
Button(root, text="AC", width=5, command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", width=5, command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="=", width=5, command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", width=5, command=lambda: get_operator("+")).grid(row=2, column=3)
Button(root, text="-", width=5, command=lambda: get_operator("-")).grid(row=3, column=3)
Button(root, text="*", width=5, command=lambda: get_operator("*")).grid(row=4, column=3)
Button(root, text="/", width=5, command=lambda: get_operator("/")).grid(row=5, column=3)

# Adding new operations
Button(root, text="pi", width=5, command=lambda: get_operator("*3.142")).grid(row=2, column=4)
Button(root, text="%", width=5, command=lambda: get_operator("%")).grid(row=3, column=4)
Button(root, text="(", width=5, command=lambda: get_operator("(")).grid(row=4, column=4)
Button(root, text="exp", width=5, command=lambda: get_operator("**")).grid(row=5, column=4)

Button(root, text="<-", width=5, command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!", width=5, command=lambda: factorial()).grid(row=3, column=5)
Button(root, text=")", width=5, command=lambda: get_operator(")")).grid(row=4, column=5)
Button(root, text="^2", width=5, command=lambda: get_operator("**2")).grid(row=5, column=5)

root.mainloop()
