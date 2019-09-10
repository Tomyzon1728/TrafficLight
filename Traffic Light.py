# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:25:31 2019

@author: Ajayi Raymond T
"""

from tkinter import *
root = Tk()
canvas= Canvas(root, bg ='white', height = 600,width =1030)
canvas.pack()
dimx= 490,600,525,-30
rect = canvas.create_rectangle(dimx)
canvas.itemconfigure(rect, fill='grey')
dim0= 415,470,600,-30
rect = canvas.create_rectangle(dim0)
canvas.itemconfigure(rect, fill='black')


dim = 450,15,575,150
dim2= 450,170,575,300
dim3= 450,320,575,450
Oval = canvas.create_oval(dim)
canvas.itemconfigure(Oval, fill='red')
Oval = canvas.create_oval(dim2)
canvas.itemconfigure(Oval, fill='yellow')
Oval = canvas.create_oval(dim3)
canvas.itemconfigure(Oval, fill='green')

root.mainloop()