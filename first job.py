#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from random import *
from tkinter import colorchooser
from tkinter import *
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style
from skimage import data
from PIL import ImageTk, Image
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

np.random.seed(42)


# In[5]:



root = Tk()
root.title("First programm))")
root.geometry("1000x540+100+100")
name = StringVar()
img_rows, img_cols = 28, 28
fig, _ = plt.subplots()
print(type(fig))
one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
print(type(one_tick)) 



def sqr(x):
    return x*x
x=np.linspace(0, 10, 50)
y = sqr(x)
# Квадратичная зависимость
y2 = [i**2 for i in x]
plt.xlabel("x") 
plt.ylabel("y") 
graf=plt.plot(x,y,x,y2)
#fig=plt.figure()
lbl=FigureCanvasTkAgg(fig,root)
#lbl.get_tk_widget().grid(row=11,column=2,columnspan=10)
lbl.get_tk_widget().grid(column=0,row=9,columnspan=10)
lbl.draw()


FileName=Entry(root,width=30,textvariable=name)
FileName.grid(row=0, column=1, columnspan=3,pady=10)
FileName.insert(0,'img_1.jpg')
lbl = Label(root, text="       X1      ")  
lbl.grid(column=0, row=5,pady=10)  
txt11 = Entry(root,width=10)  
txt11.grid(column=1, row=5,pady=10)
lbl = Label(root, text="       X2      ")  
lbl.grid(column=2, row=5,pady=10)  
txt12 = Entry(root,width=10)  
txt12.grid(column=3, row=5,pady=10) 
lbl = Label(root, text="       Y1      ")  
lbl.grid(column=0, row=7,pady=10)  
txt21 = Entry(root,width=10)  
txt21.grid(column=1, row=7,pady=10)
lbl = Label(root, text="       Y2      ")  
lbl.grid(column=2, row=7,pady=10)  
txt22 = Entry(root,width=10)  
txt22.grid(column=3, row=7,pady=10)
render=((img_rows, img_cols))




def load():
    name=FileName.get()
    img = Image.open(name)
    render = ImageTk.PhotoImage(img)
    initil = Label(root, image=render)
    initil.image = render
    initil.grid(column=0,row=11)
    #img = img.astype('float32')
    #render = render.reshape(img_rows, img_cols, 1)
    
    
def create():    
    if txt11.get():
        x1=int(txt11.get())
    else:x1=0
    if txt12.get():
        x2=int(txt12.get())
    else:x2=int(x[-1])    
    if txt21.get():
        y1=int(txt21.get())
    else:y1=0    
    if txt22.get():
        y2=int(txt22.get())  
    else:y2=int(y[-1])
        
    countX1=len(x)    
    while(x[countX1-1]>x1):
        countX1=countX1-1  
    countX2=0   
    while(x[countX2]<x2):
        countX2=countX2+1
        if(countX2==len(x)):
            break
        
    countY1=len(y)    
    while(y[countY1-1]>y1):
        countY1=countY1-1  
    countY2=0   
    while(y[countY2]<y2):
        countY2=countY2+1  
        if(countY2==len(y)):
            break
    
    
    
            
    
    
    
    u=np.zeros((countX2-countX1))    
    if(countX1<=countX2):
        for i in range(countX2-countX1):
            temp=int(countX1+i)
            u[i]=x[temp]
            
    v=np.zeros(len(u)) 
    count=0
    for i in range(countX2-countX1):
        if((sqr(u[i])>=y1)&(sqr(u[i])<=y2)):
            count=count+1
    
    a=np.zeros((count))
    if(len(u)!=len(v)):
        for elem in range(len(u)):
            if(u[elem]!=0):
                v[elem]=sqr(u[elem])
       
    #a=u#np.zeros((countY2-countY1))
    temp=0
    v2=np.zeros((count)) 
    for elem in range(countX2-countX1):
        if((sqr(u[elem])>y1)&(sqr(u[elem])<y2)):
            a[temp]=u[elem]
            temp=temp+1
    
    print(a)
    
    for elem in range(len(a)):
        v2[elem]=sqr(a[elem])
        
    
    
    fig.clf()
    plt.xlabel("x") 
    plt.ylabel("y") 
    graf=plt.plot(a,v2)
    #fig=plt.figure(plt)
    lbl=FigureCanvasTkAgg(fig,root)
    #lbl.get_tk_widget().grid(row=11,column=2,columnspan=10)
    lbl.get_tk_widget().grid(column=11,row=9,columnspan=10)
    lbl.draw()
    
    
    
    
    

Button(root,text="exit",command=root.destroy).place(x = 450, y = 450, height = 55)
Button(root,text="download",command=load).place(x = 300, y = 0, height = 25)
Button(root,text="create",command=create).place(x = 300, y = 90, height = 25)
size=250
diapason = 0





"""
canvas = Canvas(root, width=size, height=size)
canvas.grid(column=0,row=9,columnspan=10)
canvas2 = Canvas(root, width=size, height=size)
canvas2.grid(column=11,row=9,columnspan=10)


#canvas.plt(x)
#canvas.create_image(render)
#pilImage = Image.open("example.png")
#image = ImageTk.PhotoImage(image)
#imagesprite = canvas.create_image(400,400,image=image)
while diapason < 2000:
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    u = randint(0, size)
    v = randint(0, size)
    d = randint(0, size/5)
    if(diapason%2==0):
        canvas.create_oval(u, v, u+d, v+d, fill=colors)
    else:
        canvas2.create_oval(u, v, u+d, v+d, fill=colors)
    root.update()
    diapason += 1"""
#app = Example(root).pack()
root.mainloop()  
 
    #if __name__ == '__main__':
     #   main()

#window = Tk()
#colorchooser.askcolor()


# In[ ]:





# In[ ]:





# In[ ]:




