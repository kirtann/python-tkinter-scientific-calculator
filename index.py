# ------------------------- Import library and Banner -------------------------

from tkinter import *
import tkinter.messagebox
import math
from mybanner import bannerTop
import login

print(bannerTop())
print("Calculator ready to use... \nperform your tasks...")

# ------------------------- Functions -------------------------
# Function to add in the entry of text display


def button_click(char):
    global calculator_text_input
    calculator_text_input += str(char)
    text_input_type.set(calculator_text_input)

# Function to clear the whole entry of text display


def button_clear_all():
    global calculator_text_input
    calculator_text_input = ""
    text_input_type.set("")

# Function to delete one by one from the last in the entry of text display


def button_delete():
    global calculator_text_input
    text = calculator_text_input[:-1]
    calculator_text_input = text
    text_input_type.set(text)

# Function to calculate the factorial of a number


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def fact_func():
    global calculator_text_input
    result = str(factorial(int(calculator_text_input)))
    calculator_text_input = result
    text_input_type.set(result)

# Function to calculate trigonometric numbers of an angle


def trig_sin():
    global calculator_text_input
    result = str(math.sin(math.radians(int(calculator_text_input))))
    calculator_text_input = result
    text_input_type.set(result)


def trig_cos():
    global calculator_text_input
    result = str(math.cos(math.radians(int(calculator_text_input))))
    calculator_text_input = result
    text_input_type.set(result)


def trig_tan():
    global calculator_text_input
    result = str(math.tan(math.radians(int(calculator_text_input))))
    calculator_text_input = result
    text_input_type.set(result)


def trig_cot():
    global calculator_text_input
    result = str(1/math.tan(math.radians(int(calculator_text_input))))
    calculator_text_input = result
    text_input_type.set(result)

# Function to find the square tk_calc of a number


def square_root():
    global calculator_text_input
    if int(calculator_text_input) >= 0:
        temporary = str(eval(calculator_text_input+'**(1/2)'))
        calculator_text_input = temporary
    else:
        temporary = "ERROR"
    text_input_type.set(temporary)

# Function to find the third tk_calc of a number


def third_root():
    global calculator_text_input
    if int(calculator_text_input) >= 0:
        temporary = str(eval(calculator_text_input+'**(1/3)'))
        calculator_text_input = temporary
    else:
        temporary = "ERROR"
    text_input_type.set(temporary)

# Function to change the sign of number


def sign_change():
    global calculator_text_input
    if calculator_text_input[0] == '-':
        temporary = calculator_text_input[1:]
    else:
        temporary = '-'+calculator_text_input
    calculator_text_input = temporary
    text_input_type.set(temporary)

# Function to calculate the percentage of a number


def percent():
    global calculator_text_input
    temporary = str(eval(calculator_text_input+'/100'))
    calculator_text_input = temporary
    text_input_type.set(temporary)

# Funtion to find the result of an operation


def button_equal():
    global calculator_text_input
    temp_op = str(eval(calculator_text_input))
    text_input_type.set(temp_op)
    calculator_text_input = temp_op


# ------------------------- Variables -------------------------
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp  # value of exponent in e
p = math.pi  # value of pi in p
E = '*10**'  # value of 10th exponent in E

login.everything()



tk_calc = Tk()  # Tk for creating user interface
tk_calc.configure(bg="#8B8B7D", bd=9)
# tk_calc.resizable(width=False, height=False)
tk_calc.title("Scientific Calculator - By team 17")
photo = PhotoImage(file="iconcalcu.png")
tk_calc.iconphoto(False, photo)
tk_calc.geometry("423x669")
tk_calc.eval('tk::PlaceWindow . center')

calculator_text_input = ""  # the string which will input numbers from input
text_input_type = StringVar()  # type of variable which we will take from user

lblDisplay = Label(text="Scientific Calculator- Team 17",
                   font=('Helvetica', 13, 'bold'),
                   bg='black', fg='white', justify=CENTER).grid(row=0, column=1, columnspan=3)

text_display_field = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input_type,
                           bd=5, insertwidth=6, bg='#FFFFE4', justify='right').grid(row=1, columnspan=5, padx=10, pady=12)

button_params = {'bd': 5, 'fg': '#FFFFE4', 'bg': '#292929',
                 'font': ('sans-serif', 20, 'bold')}  # buttons for function
button_params_main = {'bd': 5, 'fg': '#292929', 'bg': '#FFFFE4', 'font': (
    'sans-serif', 20, 'bold')}  # buttons for main field


# ------------------------- Buttons -------------------------
# --1st row--
# Absolute value of a number
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda: button_click('abs(')).grid(row=2, column=1, sticky="nsew")
# Remainder of a division
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda: button_click('%')).grid(row=2, column=2, sticky="nsew")
# Integer division quotient
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda: button_click('//')).grid(row=2, column=3, sticky="nsew")
# Factorial of a number
factorial_button = Button(tk_calc, button_params, text='x!',
                          command=fact_func).grid(row=2, column=4, sticky="nsew")
# Euler's number e
eulers_num = Button(tk_calc, button_params, text=' e ',
                    command=lambda: button_click(str(math.exp(1)))).grid(row=2, column=0, sticky="nsew")

# --2nd row--
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
              command=trig_sin).grid(row=3, column=1, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
                command=trig_cos).grid(row=3, column=2, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
                 command=trig_tan).grid(row=3, column=3, sticky="nsew")
# Cotangent of an angle in degrees
cotangent = Button(tk_calc, button_params, text='cot',
                   command=trig_cot).grid(row=3, column=4, sticky="nsew")
# Pi(3.14...) number
pi_num = Button(tk_calc, button_params, text=' π ',
                command=lambda: button_click(str(math.pi))).grid(row=3, column=0, sticky="nsew")

# --3rd row--
# Power of 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
                      command=lambda: button_click('**2')).grid(row=4, column=0, sticky="nsew")
# Power of 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
                     command=lambda: button_click('**3')).grid(row=4, column=1, sticky="nsew")
# Power of n
nth_power = Button(tk_calc, button_params, text='x^n',
                   command=lambda: button_click('**')).grid(row=4, column=2, sticky="nsew")
# Inverse number
inv_power = Button(tk_calc, button_params, text='x\u207b\xb9',
                   command=lambda: button_click('**(-1)')).grid(row=4, column=3, sticky="nsew")
# Powers of 10
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda: button_click('10**')).grid(row=4, column=4, sticky="nsew")

# --4th row--
# Square tk_calc of a number
square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=5, column=0, sticky="nsew")
# Third tk_calc of a number
third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=5, column=1, sticky="nsew")
# nth tk_calc of a number
nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda: button_click('**(1/')).grid(row=5, column=2, sticky="nsew")
# Logarithm of a number with base 10
log_base10 = Button(tk_calc, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                    command=lambda: button_click('log(')).grid(row=5, column=3, sticky="nsew")
# Logarithm of a number with base e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lambda: button_click('ln(')).grid(row=5, column=4, sticky="nsew")

# --5th row--
# Add a left parentheses
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda: button_click('(')).grid(row=6, column=0, sticky="nsew")
# Add a right parentheses
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda: button_click(')')).grid(row=6, column=1, sticky="nsew")
# Change the sign of a number
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=6, column=2, sticky="nsew")
# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
                    command=percent).grid(row=6, column=3, sticky="nsew")
# Calculate the e^x
ex = Button(tk_calc, button_params, text='e^x',
            command=lambda: button_click('e(')).grid(row=6, column=4, sticky="nsew")

# --6th row--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda: button_click('7')).grid(row=7, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda: button_click('8')).grid(row=7, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda: button_click('9')).grid(row=7, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='DEL', command=button_delete, bg='#C0C0FF').grid(row=7, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='AC', command=button_clear_all, bg='#C0C0FF').grid(row=7, column=4, sticky="nsew")

# --7th row--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda: button_click('4')).grid(row=8, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda: button_click('5')).grid(row=8, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda: button_click('6')).grid(row=8, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda: button_click('*')).grid(row=8, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda: button_click('/')).grid(row=8, column=4, sticky="nsew")

# --8th row--
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda: button_click('1')).grid(row=9, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda: button_click('2')).grid(row=9, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda: button_click('3')).grid(row=9, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda: button_click('+')).grid(row=9, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda: button_click('-')).grid(row=9, column=4, sticky="nsew")

# --9th row--
button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda: button_click('0')).grid(row=10, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda: button_click('.')).grid(row=10, column=1, sticky="nsew")
exp = Button(tk_calc, button_params_main, text='EXP', font=('sans-serif', 16, 'bold'),
             command=lambda: button_click(E)).grid(row=10, column=2, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=10, columnspan=2, column=3, sticky="nsew")


# ------------------------- to make responsive grid -------------------------
n_rows = 11
n_columns = 5
for i in range(1, n_rows):
    tk_calc.grid_rowconfigure(i,  weight=1)
for i in range(n_columns):
    tk_calc.grid_columnconfigure(i,  weight=1)


# ------------------------- functions for menubar -------------------------
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit > 0:
        tk_calc.destroy()
        return


def aboutus():
    message = '''Calculator 1.1
© 2022 TEAM 17. All rights reserved.\n\n\t-------About Us-------
Hello users meet our members :-
        12115299 (58)-  JAIN KIRTAN SUNIL
        12103695 (34)-  SUDANSHU RAJ TIWARI
        12107018 (17)-  GURKIRAT KAUR SURI
    '''
    tkinter.messagebox.showinfo("About Us", message)


# ------------------------- menubar -------------------------
menubar = Menu(tk_calc)
tk_calc.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Standard Calculator',underline=1)
file_menu.add_command(label='Scientific Calculator',underline=1)
file_menu.add_separator()
file_menu.add_command(label='Exit',underline=0, command=iExit)

about_menu = Menu(menubar, tearoff=False)
about_menu.add_command(label='View Help', underline=0)
about_menu.add_separator()
about_menu.add_command(label='About Us',underline=0, command=aboutus)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="Cut", underline=0)
editmenu.add_command(label="Copy", underline=1)
editmenu.add_separator()
editmenu.add_command(label="Paste", underline=0)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
menubar.add_cascade(
    label='Edit', 
    menu=editmenu,
    underline=0
)
menubar.add_cascade(
    label="About Us",
    menu=about_menu,
    underline=0
)

# ------------------------- mainloop -------------------------
tkinter.messagebox.showinfo("Welcome", "Welcome to our Calculator")
tk_calc.mainloop()
