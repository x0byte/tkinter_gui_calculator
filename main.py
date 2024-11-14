from tkinter import *
from tkinter import ttk, messagebox
import operations

first_operand = None
operator = None
second_operand = None
result = None

def add_digit(digit):
    display_var.set(operations.add_digit(display_var.get(), digit))

def set_operator(op):
    global first_operand, operator
    first_operand, operator = operations.set_operator(display_var.get(), op)
    display_var.set("")

def calculate_result():
    global first_operand, operator
    second_operand = float(display_var.get())
    result = operations.calculate_results(first_operand, operator, second_operand)
    
    add_to_history(first_operand, operator, second_operand, result)
    get_history()
    display_var.set(result)
    first_operand = None
    operator = None

def clear_display():
    display_var.set(operations.clear_display())

def add_to_history(first_operand, operator, second_operand, result):

    operations.add_to_history(first_operand, operator, second_operand, result)


def get_history():

    file_path = "history.txt"
    
    try:
        with open(file_path, "r") as file:
            history_entries = file.readlines()

        history_list.delete(0, END)

        for histroy in history_entries:
            history_list.insert(END, histroy.strip())

    except Exception as e:
        print(f"Error loading file: {e}")

def clear_history():

    if messagebox.askyesno("Confirm Action", "Are you sure you want to delete the history?"):
        with open("history.txt", "w") as file:
            pass

    get_history()


def backspace():

    txt = number_entry.get()
    txt = txt[:-1]

    number_entry.delete(0, END)
    number_entry.insert(0, txt)


root = Tk()
root.title("Calculator")
root.geometry("600x800")
root.minsize(600, 800)
root.maxsize(600, 800)
root.configure(bg="gray10")

#styles
style = ttk.Style()
style.configure("TFrame", background="gray10")


title_frame = ttk.Frame(root, style="TFrame")
title_frame.grid(row=0, column=0, sticky=(W, E))


display_frame = ttk.Frame(root, style="TFrame")
display_frame.grid(row=1, column=0, sticky=(W, E))

button_frame = ttk.Frame(root, style="TFrame")
button_frame.grid(column=0, row=2, sticky=(N, W, E, S), padx=10, pady=10)

history_frame = ttk.Frame(root, style="TFrame")
history_frame.grid(column=0, row=3, sticky=(N, W, E, S), padx=10, pady=10)

#equal button
style.configure("Custom.Equal.TButton", background="orangered3", foreground="white", font=("Helvetica", 18),borderwidth=0, relief="flat", highlightthickness=0)
#digit buttons
style.configure("Custom.Digit.TButton", background="gray1", foreground="white" ,font=("Helvetica", 18),borderwidth=0, relief="flat", highlightthickness=0)

#operation buttons styling
style.configure("Custom.Operation.TButton" , font=("Helvetica", 18), background="forestgreen", foreground="white",borderwidth=0, relief="flat", highlightthickness=0)
style.configure("Custom.History.TButton", background="gray7", foreground="white", font=("Helvetica", 14) ,borderwidth=0, relief="flat", highlightthickness=0)
style.configure("Custom.Back.TButton", background="gray7", foreground="white", font=("Helvetica", 14) ,borderwidth=0, relief="flat", highlightthickness=0)

lbl_title = Label(title_frame, text="Calculator", font=("Helvetica", 25), anchor="center", bg="gray10", fg="white")
lbl_title.grid(row=0, column=0, sticky=(E, W), ipadx=10, ipady=20)

title_frame.columnconfigure(0, weight=1)


#entry widget for the inputs
number_entry = Entry(display_frame, width=42, font=("Helvetica", 18), justify="right",borderwidth=0, relief="flat", background="gray9", foreground="white", highlightthickness=0)
number_entry.grid(row=0, sticky=(W, E), padx=10, pady=10, ipadx=10, ipady=20)

number_entry.focus_set()

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


btnClear = ttk.Button(button_frame, text="Clear", width=10, style="Custom.Back.TButton", command=lambda: clear_display()).grid(column=1, row=5, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btnEqual = ttk.Button(button_frame, text="=", width=10, style="Custom.Equal.TButton", command=lambda: calculate_result()).grid(column=2, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btnDelHistory = ttk.Button(button_frame, text="Clear History", width=10, style="Custom.History.TButton", command=lambda: clear_history()).grid(column=0, row=5, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)

btnPeriod = ttk.Button(button_frame, text=".", width=10, style="Custom.Digit.TButton", command=lambda: add_digit(".")).grid(column=0, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btnBacksapce = ttk.Button(button_frame, text="Del", width=10, style="Custom.Back.TButton", command=lambda: backspace()).grid(column=2, row=5, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)


plus_icon = PhotoImage(file="assets/plus_icon.png")
minus_icon = PhotoImage(file="assets/minus_icon.png")
mul_icon = PhotoImage(file="assets/multiply_icon.png")
div_icon = PhotoImage(file="assets/divide_icon.png")


#operation buttons components
btn_add = ttk.Button(button_frame, image=plus_icon, width=5, style="Custom.Operation.TButton", command=lambda: set_operator("+")).grid(column=3, row=1, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_sub = ttk.Button(button_frame, image=minus_icon, width=5, style="Custom.Operation.TButton", command=lambda: set_operator("-")).grid(column=3, row=2, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_mul = ttk.Button(button_frame, image=mul_icon, width=5, style="Custom.Operation.TButton", command=lambda: set_operator("*")).grid(column=3, row=3, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_div = ttk.Button(button_frame, image=div_icon, width=5, style="Custom.Operation.TButton", command=lambda: set_operator("/")).grid(column=3, row=4, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)
btn_pow = ttk.Button(button_frame, text="^", width=5, style="Custom.Operation.TButton", command=lambda: set_operator("^")).grid(column=3, row=5, sticky=(N, S, E, W), ipady=10, padx=10, pady=10)


history_list = Listbox(history_frame, width=66, height=6, background="grey9", foreground="white",borderwidth=0, relief="flat", highlightthickness=0)
history_list.grid(row=0, sticky=(W, E), padx=10, pady=10, ipadx=10, ipady=20)

get_history()

root.mainloop()