import tkinter as tk 
from tkinter import *
from tkinter import messagebox

import matplotlib as mpl
from matplotlib import *
import matplotlib.pyplot

import numpy as np
from numpy import *

from PIL import Image, ImageTk
import os
import math

import plyer as ply
from plyer import *
from plyer import notification


#функция вывода графика и оповещение
def graph():
    if not tag_graph.get():
        if not xFirstInput.get() or not xSecondInput.get() or not count.get():
            ply.notification.notify( message='Введите значения во все поля ввода чтобы продолжить.', app_name='График функции', app_icon='icon.ico', title='Ошибка', ) #уведомление о том что не все поля заполнены
        else: 
            x = np.linspace(eval(xFirstInput.get()), eval(xSecondInput.get()), eval(count.get())) #создание списка значений
            y = eval(graphInput.get()) #создание зависимости
            matplotlib.pyplot.plot(x, y, color=graph_colors[current_colors]); #создание графика
            matplotlib.pyplot.title('y=' + graphInput.get()) #вывод подписи
            matplotlib.pyplot.show() #вывод графика
    else:
        if not xFirstInput.get() or not xSecondInput.get() or not count.get():
            ply.notification.notify( message='Введите значения во все поля ввода чтобы продолжить.', app_name='График функции', app_icon='icon.ico', title='Ошибка', ) #уведомление о том что не все поля заполнены
        else: 
            x = np.linspace(eval(xFirstInput.get()), eval(xSecondInput.get()), eval(count.get())) #создание списка значений
            y = eval(graphInput.get()) #создание зависимости
            matplotlib.pyplot.plot(x, y, color=graph_colors[current_colors]); #создание графика
            matplotlib.pyplot.title(str(tag_graph.get())) #вывод подписи
            matplotlib.pyplot.show() #вывод графика

#смена цвета кнопки
count_colors = 7 #количество цветов 
graph_colors = ['red', 'blue', 'orange', 'black', 'yellow', 'green', 'purple'] #цвета в текстовом виде
button_colors = ['#c74040', '#4091c7', '#f08630', '#2b2b2b', '#d4d146', '#32a852', '#7d32a8'] #цвета в HEX
current_colors = 0 #текущий цвет
def color():
    global current_colors
    if current_colors == (count_colors - 1):
        current_colors = 0
        Color.config(background=button_colors[current_colors]) #изменение цвета кнопки
    elif current_colors < count_colors:
        current_colors += 1 #смена цвета 
        Color.config(background=button_colors[current_colors]) #изменение цвета кнопки

#свойства окон
window = tk.Tk() 
window.title('Построение графика функции') 
window.geometry('593x308') 
window.resizable(width=False, height=False) 
window.iconbitmap('icon.ico')
mpl.rcParams['toolbar'] = 'None'

#переменные
graphInput = StringVar()
xSecondInput = StringVar()
xFirstInput = StringVar()
count = StringVar()
tag_graph = StringVar()

#логотип
img = ImageTk.PhotoImage(Image.open("header.gif")) #переменная с картинкой
panel = Label(window, image = img) #элемнт с картинкой
panel.grid(row=0, column=1) #Расположение картинки

#создание элементов
mainLabel = tk.Label(text="Введите график функции:", fg='#153F6B')
E1 = tk.Entry(textvariable=graphInput)
secondLabel = tk.Label(text="Введите начальное значение x:", fg='#153F6B')
E2 = tk.Entry(textvariable=xFirstInput)
thirdLabel = tk.Label(text="Введите конечное значение x:", fg='#153F6B')
E3 = tk.Entry(textvariable=xSecondInput)
fourthLabel = tk.Label(text="Введите кол-во точек для построения:", fg='#153F6B')
E4 = tk.Entry(textvariable=count)
B = tk.Button(window, text ="Построить", command = graph)
ColorLabel = tk.Label(text="Цвет графика:", fg='#153F6B')
Color = tk.Button (window, text ="Нажмите", command = color, background=button_colors[current_colors])
TagLabel = tk.Label(text="Введите подпись к графику:", fg='#153F6B')
Tag = tk.Entry(textvariable=tag_graph)

#расположение
mainLabel.grid(row=1, column=1) 
E1.grid(row=2, column=1)
secondLabel.grid(row=3, column=0)
E2.grid(row=4, column=0)
thirdLabel.grid(row=3, column=1)
E3.grid(row=4, column=1)
fourthLabel.grid(row=3, column=2)
E4.grid(row=4, column=2)
ColorLabel.grid(row=5, column=0)
Color.grid(row=6, column=0, padx=10, pady=10)
TagLabel.grid(row=5, column=1)
Tag.grid(row=6, column=1)
B.grid(row=7, column=1, padx=10, pady=10)

window.mainloop()