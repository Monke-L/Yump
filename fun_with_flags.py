import tkinter as tk
import tkinter.ttk
from tkinter import *


def change_to_japan():
    C.itemconfigure(rect1, fill='white', state='hidden')
    C.itemconfigure(rect2, fill='white', state='hidden')
    C.itemconfigure(circ1, fill='red', state='normal')
    C.config(bg='white')

def change_to_bang():
    C.itemconfigure(rect1, fill='white', state='hidden')
    C.itemconfigure(rect2, fill='white', state='hidden')
    C.itemconfigure(circ1, fill='red', state='normal')
    C.config(bg='green')

def change_to_sweden():
    C.itemconfigure(circ1, state='hidden')
    C.itemconfigure(rect1, fill='yellow', state='normal')
    C.itemconfigure(rect2, fill='yellow', state='normal')
    C.config(bg='blue')

def change_to_denmark():
    C.itemconfigure(circ1, state='hidden')
    C.itemconfigure(rect1, fill='white', state='normal', )
    C.itemconfigure(rect2, fill='white', state='normal')
    C.config(bg='red')

def change_to_england():
    C.itemconfigure(circ1, state='hidden')
    C.itemconfigure(rect1, fill='red', state='normal')
    C.itemconfigure(rect2, fill='red', state='normal')
    
    C.config(bg='white')

def no_country():
    C.itemconfigure(circ1, fill='green')
    C.config(bg='white')

root = tk.Tk()

C = tk.Canvas(root, bg="white", height=200, width=300)
C.grid(column=3, row=1, rowspan=3)
circ1 = C.create_oval(100, 50, 200, 150,
                            fill="red", 
                            outline = "",
                            state='hidden')

rect1 = C.create_rectangle(00, 90, 310, 110, 
fill = 'yellow', state='hidden',outline="")
rect2 = C.create_rectangle(90, 0, 110, 210,
fill = 'yellow', state='hidden',outline="")
rect3 = C.create_rectangle(00, 90, 310, 110, 
fill = 'yellow', state='hidden',outline="")
rect4 = C.create_rectangle(0, 10, 110, 210,
fill = 'yellow', state='hidden',outline="")

b1 = tk.ttk.Button(root, text='Japan', command=change_to_japan)
b1.grid(column=1, row=1)
b2 = tk.ttk.Button(root, text='Bangladesh', command=change_to_bang)
b2.grid(column=1, row=2)
b3 = tk.ttk.Button(root, text='No country', command=no_country)
b3.grid(column=1, row=3)
b4 = tk.ttk.Button(root, text='Stäng', command=root.destroy)
b4.grid(column=2, row=4, columnspan=2)
b5 = tk.ttk.Button(root, text='Sweden', command=change_to_sweden)
b5.grid(column=2, row=1, sticky=tk.NW)
b6 = tk.ttk.Button(root, text='Denmark', command=change_to_denmark)
b6.grid(column=2, row=2)
b7 = tk.ttk.Button(root, text='England', command=change_to_england)
b7.grid(column=2, row=3)


root.mainloop()
