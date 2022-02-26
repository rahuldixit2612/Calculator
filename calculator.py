from distutils import command
from random import uniform
import tkinter as tk
from tkinter import *
from webbrowser import get
window = tk.Tk()


window.title("Calculator")
window.rowconfigure(6, weight=1)
window.columnconfigure([0, 1, 2, 3, 4],  weight=1)
#window.geometry("580x580")

frame1 = LabelFrame(window, bg="Grey", fg="white", padx=5, pady=5, )
frame1.grid(sticky="nw")
Tin = tk.Text(frame1, height = 3, width = 47, )
Tin.pack()

Tin.grid(row=0, column=0, sticky="nw")  

frame2 = LabelFrame(window, bg="Grey", fg="white", padx=5, pady=5)
frame2.grid(row=1, column=0, sticky = "nw")

#frame3 = LabelFrame(window, bg="Green", fg="white", padx=5, pady=5)
#frame3.grid(row=2, column=0)

def button_clicked9():
    Tin.insert(INSERT, "9")

def button_clicked8():
    Tin.insert(INSERT, "8")

def button_clicked7():
    Tin.insert(INSERT, "7")

def button_clicked6():
    Tin.insert(INSERT, "6")

def button_clicked5():
    Tin.insert(INSERT, "5")

def button_clicked4():
    Tin.insert(INSERT, "4")

def button_clicked3():
    Tin.insert(INSERT, "3")

def button_clicked2():
    Tin.insert(INSERT, "2")

def button_clicked1():
    Tin.insert(INSERT, "1")

def button_clicked0():
    Tin.insert(INSERT, "0")

def button_clickedplus():
    Tin.insert(INSERT, "+")

def button_clickedminus():
    Tin.insert(INSERT, "-")

def button_clickedmultiply():
    Tin.insert(INSERT, "*")

def button_clickeddivide():
    Tin.insert(INSERT, "/")

def evaluate():
    expression = Tin.get("1.0",END)
    output = eval(expression)
    Tin.delete("1.0","end")
    Tin.insert(INSERT, expression +  "=" + str(output))

def clear_txt():
    Tin.delete("1.0","end")
    #Tout.delete("1.0","end")

btn9 = tk.Button(master=frame2, height= 5, width=12,text="9", command = button_clicked9)
btn9.grid(row=1, column=0, sticky="nsew")

btn8 = tk.Button(master=frame2, height= 5, width=12,text="8",command = button_clicked8)
btn8.grid(row=1, column=1, sticky="nsew")

btn7 = tk.Button(master=frame2,height= 5, width=12, text="7",command = button_clicked7)
btn7.grid(row=1, column=2, sticky="nsew")

btn6 = tk.Button(master=frame2,height= 5, width=12, text="6",command = button_clicked6)
btn6.grid(row=1, column=3, sticky="nsew")

btn5 = tk.Button(master=frame2, height= 5, width=12,text="5",command = button_clicked5)
btn5.grid(row=2, column=0, sticky="nsew")

btn4 = tk.Button(master=frame2, height= 5, width=12,text="4",command = button_clicked4)
btn4.grid(row=2, column=1, sticky="nsew")

btn3 = tk.Button(master=frame2, height= 5, width=12,text="3",command = button_clicked3)
btn3.grid(row=2, column=2, sticky="nsew")

btn2 = tk.Button(master=frame2, height= 5, width=12,text="2",command = button_clicked2)
btn2.grid(row=2, column=3, sticky="nsew")

btn1 = tk.Button(master=frame2, height= 5, width=12,text="1",command = button_clicked1)
btn1.grid(row=3, column=0, sticky="nsew")

btn = tk.Button(master=frame2, height= 5, width=12,text="+",command = button_clickedplus)
btn.grid(row=3, column=1, sticky="nsew")

btn = tk.Button(master=frame2, height= 5, width=12,text="-",command = button_clickedminus)
btn.grid(row=3, column=2, sticky="nsew")

btn = tk.Button(master=frame2,height= 5, width=12, text="*",command = button_clickedmultiply)
btn.grid(row=3, column=3, sticky="nsew")

btn = tk.Button(master=frame2, height= 5, width=12,text="/",command = button_clickeddivide)
btn.grid(row=4, column=0, sticky="nsew")

btn = tk.Button(master=frame2, height= 5, width=12,text="CLEAR", command=clear_txt)
btn.grid(row=4, column=1, sticky="nsew")

btn = tk.Button(master=frame2,height= 5, width=12, text="ENTER", command=evaluate)
btn.grid(row=4, column=2, sticky="nsew")

btn = tk.Button(master=frame2,height= 5, width=12, text="0",command = button_clicked0)
btn.grid(row=4, column=3, sticky="nsew")

#Tout= tk.Text(frame3, height = 3, width = 50)
#Tout.pack()
#Tout.grid(row=5, column=0, sticky="nsew")


window.resizable(False, False) 



window.mainloop()