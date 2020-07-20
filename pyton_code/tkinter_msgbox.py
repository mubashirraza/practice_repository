from tkinter import *
#import tkinter.messagebox

root = Tk()
"""
tkinter.messagebox.showinfo("Title ","this is awesome")

response = tkinter.messagebox.askquestion("question1","do you like cofee")

if response == "yes":
    print("here is a coffe for you")
else:
    print("thats your choice")
"""

canvas = Canvas(root,width=200,height=100)
canvas.pack()
newline= canvas.create_line(0,0,50,100)
otherline= canvas.create_line(0,0,100,100,fill="red")
