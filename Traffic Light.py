# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:25:31 2019

@author: Ajayi Raymond T
"""

from tkinter import *
root = Tk()
root.title('TrafficLight')
root.wm_iconbitmap('TL.ico')
canvas= Canvas(root, bg ='white', height = 600,width =1030)
canvas.pack(side= 'top')
dim_black_casing= 415,470,600,-30
dim_bar= 490,600,525,-30
dimr = 450,15,575,150
dimy= 450,170,575,300
dimg= 450,320,575,450
rect = canvas.create_rectangle(dim_bar)
canvas.itemconfigure(rect, fill='#656565')
rect = canvas.create_rectangle(dim_black_casing)
canvas.itemconfigure(rect, fill='#343434')

Oval = canvas.create_oval(dimr)
canvas.itemconfigure(Oval, fill='grey')
Oval = canvas.create_oval(dimy)
canvas.itemconfigure(Oval, fill='grey')
Oval = canvas.create_oval(dimg)
canvas.itemconfigure(Oval, fill='grey')
#def redLight():
    #starttraffic()
stop_var = False 
    
def go_but():
    global stop_var
    stop_var = False
    redLight()
    
def redLight():
    global stop_var
    if stop_var:
        return
    Oval1 = canvas.create_oval(dimr)
    canvas.itemconfigure(Oval1, fill='red')
    Oval2 = canvas.create_oval(dimy)
    canvas.itemconfigure(Oval2, fill='grey')
    Oval3 = canvas.create_oval(dimg)
    canvas.itemconfigure(Oval3, fill='grey')
    canvas.after(10000,yellowLight)

    
    
def yellowLight():
    global stop_var
    if stop_var:
        return
    Oval4 = canvas.create_oval(dimr)
    canvas.itemconfigure(Oval4, fill='grey')
    Ovalyellow = canvas.create_oval(dimy)
    canvas.itemconfigure(Ovalyellow, fill='yellow')
    Oval5 = canvas.create_oval(dimg)
    canvas.itemconfigure(Oval5, fill='grey')
    canvas.after(5000,greenLight)
    
def greenLight():
    global stop_var
    if stop_var:
        return
    Oval6 = canvas.create_oval(dimr)
    canvas.itemconfigure(Oval6, fill='grey')
    Oval7 = canvas.create_oval(dimy)
    canvas.itemconfigure(Oval7, fill='grey')
    Ovalgreen = canvas.create_oval(dimg)
    canvas.itemconfigure(Ovalgreen, fill='green')
    canvas.after(8000,redLight)
def stop():
    global stop_var
    Oval6 = canvas.create_oval(dimr)
    canvas.itemconfigure(Oval6, fill='grey')
    Oval7 = canvas.create_oval(dimy)
    canvas.itemconfigure(Oval7, fill='grey')
    Ovalgreen = canvas.create_oval(dimg)
    canvas.itemconfigure(Ovalgreen, fill='grey')
    stop_var = True
        
goButton = Button(root,height = 2,text=" GO ",padx= 16, bd = 2, fg='green', font =('courier',10, 'bold'),bg = '#00ffff',command=go_but)
goButton.pack(side= 'top')
stopButton = Button(root,height = 2,text="STOP",padx= 16, bd = 2, fg='red', font =('courier',10, 'bold'),bg = '#00ffff',command=stop)
stopButton.pack(side= 'top')

root.mainloop()