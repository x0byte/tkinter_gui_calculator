from tkinter import *
from tkinter import ttk
import operations

first_operand = None
operator = None

def add_digit(digit):
    display_var.set(operations.add_digit(display_var.get(), digit))

def set_operator(op):
    global first_operand, operator
    first_operand, operator = operations.set_operator(display_var.get(), op)
    display_var.set("")

def calculate_result():
    global first_operand, operator
    result = operations.calculate_results(first_operand, operator, float(display_var.get()))
    display_var.set(result)
    first_operand = None
    operator = None

def clear_display():
    display_var.set(operations.clear_display())


root = Tk()
root.title("Calculator")
root.geometry("600x500")
root.minsize(600, 500)

title_frame = ttk.Frame(root)
title_frame.grid(row=0, column=0, sticky=(W, E))

display_frame = ttk.Frame(root)
display_frame.grid(row=1, column=0, sticky=(W, E))

button_frame = ttk.Frame(root, height=500, width=600)
button_frame.grid(column=0, row=2, sticky=(N, W, E, S), padx=10, pady=10)

#styles
style = ttk.Style()
#equal button
style.configure("Custom.Equal.TButton", background="firebrick1", foreground="black", font=("Helvetica", 18))

#digit buttons
style.configure("Custom.Digit.TButton", font=("Helvetica", 18))

#operation buttons styling
style.configure("Custom.Operation.TButton" , font=("Helvetica", 18), background="seagreen1", foreground="black")

lbl_title = ttk.Label(title_frame, font=("Helvetica", 25), anchor="center", text="Calculator")
lbl_title.grid(row=0, column=0, sticky=(E, W), ipadx=10, ipady=20)

title_frame.columnconfigure(0, weight=1)


#entry widget for the inputs
number_entry = ttk.Entry(display_frame, width=42, font=("Helvetica", 18), justify="right")
number_entry.grid(row=0, sticky=(W, E), padx=10, pady=10, ipadx=10, ipady=20)
display_var = StringVar()
number_entry.config(textvariable=display_var)
display_var.set("")


num1 = ttk.Button(button_frame, text="1", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(1)).grid(column=0, row=1, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num2 = ttk.Button(button_frame, text="2", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(2)).grid(column=1, row=1, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num3 = ttk.Button(button_frame, text="3", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(3)).grid(column=2, row=1, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num4 = ttk.Button(button_frame, text="4", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(4)).grid(column=0, row=2, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num5 = ttk.Button(button_frame, text="5", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(5)).grid(column=1, row=2, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num6 = ttk.Button(button_frame, text="6", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(6)).grid(column=2, row=2, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num7 = ttk.Button(button_frame, text="7", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(7)).grid(column=0, row=3, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num8 = ttk.Button(button_frame, text="8", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(8)).grid(column=1, row=3, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num9 = ttk.Button(button_frame, text="9", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(9)).grid(column=2, row=3, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
num0 = ttk.Button(button_frame, text="0", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(0)).grid(column=1, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)

btnClear = ttk.Button(button_frame, text="Clear", width=10, style="Custom.Digit.TButton", command=lambda: clear_display()).grid(column=0, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btnEqual = ttk.Button(button_frame, text="=", width=10, style="Custom.Equal.TButton", command=lambda: calculate_result()).grid(column=2, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)


#operation buttons components
btn_add = ttk.Button(button_frame, text="+", width=5, style="Custom.Operation.TButton", command=lambda: set_operator("+")).grid(column=3, row=1, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_sub = ttk.Button(button_frame, text="-", width=5, style="Custom.Operation.TButton", command=lambda: set_operator("-")).grid(column=3, row=2, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_mul = ttk.Button(button_frame, text="*", width=5, style="Custom.Operation.TButton", command=lambda: set_operator("*")).grid(column=3, row=3, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_div = ttk.Button(button_frame, text="/", width=5, style="Custom.Operation.TButton", command=lambda: set_operator("/")).grid(column=3, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)

root.mainloop()