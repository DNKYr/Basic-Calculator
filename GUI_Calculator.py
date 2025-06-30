import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()

num = tk.StringVar()

root.title('Calculator')
root.geometry('250x350+50+50')

for i in range(4):
    root.columnconfigure(i, weight=1)

for i in range(5):
    root.rowconfigure(i+1, weight=1)

display = ttk.Entry(root, textvariable=num, font= ('Calibri', 15), state=DISABLED)

#Row 1
clear_button = ttk.Button(root, text="C")
percentage_button = ttk.Button(root, text='%')
compare_button = ttk.Button(root, text='<')
division_button = ttk.Button(root, text='/')

#Row 2
seven_button = ttk.Button(root, text='7')
eight_button = ttk.Button(root, text='8')
nine_button = ttk.Button(root, text='9')
multi_button = ttk.Button(root, text='*')

#Row 3
four_button = ttk.Button(root, text='4')
five_button = ttk.Button(root, text='5')
six_button = ttk.Button(root, text='6')
minus_button = ttk.Button(root, text='-')

#Row 4
one_button = ttk.Button(root, text='1')
two_button = ttk.Button(root, text='2')
three_button = ttk.Button(root, text='3')
add_button = ttk.Button(root, text='+')

#Row 5
zero_button = ttk.Button(root, text='0')
dot_button = ttk.Button(root, text='.')
equal_button = ttk.Button(root, text='=')

#Show display
display.grid(row = 0, column=0, columnspan=4, sticky="we")

#show Row 1
clear_button.grid(row = 1, column=0, sticky="nsew")
percentage_button.grid(row = 1, column=1, sticky="nsew")
compare_button.grid(row = 1, column=2, sticky="nsew")
division_button.grid(row = 1, column=3, sticky="nsew")

#show Row 2
seven_button.grid(row=2, column=0, sticky = "nsew")
eight_button.grid(row=2, column=1, sticky = "nsew")
nine_button.grid(row=2, column=2, sticky = "nsew")
multi_button.grid(row=2, column=3, sticky = "nsew")

#show Row 3
four_button.grid(row = 3, column=0, sticky="nsew")
five_button.grid(row = 3, column=1, sticky="nsew")
six_button.grid(row = 3, column=2, sticky="nsew")
minus_button.grid(row = 3, column=3, sticky="nsew")

#show Row 4
one_button.grid(row = 4, column=0, sticky="nsew")
two_button.grid(row = 4, column=1, sticky="nsew")
three_button.grid(row = 4, column=2, sticky="nsew")
add_button.grid(row = 4, column=3, sticky="nsew")

#show Row 5
zero_button.grid(row=5, column=0, columnspan=2, sticky="nsew")
dot_button.grid(row=5, column=2, sticky='nsew')
equal_button.grid(row=5, column=3, sticky='nsew')

root.mainloop()

