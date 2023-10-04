import tkinter as tk
from tkinter import ttk

calculation = ""

def add_to_input(symbol):
    global calculation
    calculation = str(calculation)
    calculation += str(symbol)
    input.delete(1.0, "end")
    input.insert(1.0, calculation)
    pass

def calc():
    try:
        global calculation
        calculation = eval(str(calculation))
        input.delete(1.0, "end")
        input.insert(1.0, calculation)
    except:
        clear()

def clear():
    global calculation
    calculation = ""
    input.delete(1.0, "end")
    pass

def reverse():
    global calculation
    calculation = float(calculation) * -1
    input.delete(1.0, "end")
    input.insert(1.0, calculation)

#window
window = tk.Tk()
window.title('Basic calculator')
window.geometry("365x350")
window.configure(bg="#212121")
window.iconbitmap("icon.ico")

#input 
input = tk.Text(window, width=15, height=1, font=("Arial", 25, "bold"), pady= 15, fg="white")
input.grid(row=1, column=0, columnspan=4)
input.configure(bg="#212121")


'''
   c1 c2 c3 c4
    |  |  |  |
r1-[       ][/]
r2-[1][2][3][x]
r3-[4][5][6][-]
r4-[7][8][9][+]
r5-[(][0][,][=]

'''

#number buttons
btn_1 = tk.Button(window, text="1", command=lambda:add_to_input(1), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_1.grid(row=3, column=1)
btn_2 = tk.Button(window, text="2", command=lambda:add_to_input(2), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_2.grid(row=3, column=2)
btn_3 = tk.Button(window, text="3", command=lambda:add_to_input(3), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_3.grid(row=3, column=3)

btn_4 = tk.Button(window, text="4", command=lambda:add_to_input(1), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(window, text="5", command=lambda:add_to_input(2), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(window, text="6", command=lambda:add_to_input(3), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_6.grid(row=4, column=3)

btn_7 = tk.Button(window, text="7", command=lambda:add_to_input(1), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_7.grid(row=5, column=1)
btn_8 = tk.Button(window, text="8", command=lambda:add_to_input(2), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_8.grid(row=5, column=2)
btn_9 = tk.Button(window, text="9", command=lambda:add_to_input(3), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_9.grid(row=5, column=3)

btn_0 = tk.Button(window, text="0", command=lambda:add_to_input(3), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_0.grid(row=6, column=2)

#func buttons
btn_reverse = tk.Button(window, text="+/-", command=reverse, width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_reverse.grid(row=6, column=1)

btn_obra = tk.Button(window, text="(", command=lambda:add_to_input("("), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_obra.grid(row=2, column=1)
btn_obra = tk.Button(window, text=")", command=lambda:add_to_input(")"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_obra.grid(row=2, column=2)
btn_obra = tk.Button(window, text="^2", command=lambda:add_to_input("**2"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_obra.grid(row=2, column=3)

btn_dot = tk.Button(window, text=",", command=lambda:add_to_input("."), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_dot.grid(row=6, column=3)

btn_plus = tk.Button(window, text="+", command=lambda:add_to_input("+"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_plus.grid(row=5, column=4)
btn_minus = tk.Button(window, text="-", command=lambda:add_to_input("-"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_minus.grid(row=4, column=4)
btn_pow = tk.Button(window, text="*", command=lambda:add_to_input("*"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_pow.grid(row=3, column=4)
btn_div = tk.Button(window, text="/", command=lambda:add_to_input("/"), width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_div.grid(row=2, column=4)


btn_enter = tk.Button(window, text="=", command=calc, width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_enter.grid(row=6, column=4)

btn_clear = tk.Button(window, text="C", command=clear, width=5, font=("Arial", 20), background="#2b2b2b", fg="white")
btn_clear.grid(row=1, column=4)

window.mainloop()