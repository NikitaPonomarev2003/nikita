"""
Здравствуйте, 10б!

Предлагаю вам принять участие в создании коллективного психологического
портрета нашей группы. Для этого используем известный тест,
связанный с дорисовыванием кружочков.
)))
Перед вам заготовка программы. Нарисованы 15 окружностей. Они пронумерованы,
0..14
Ваша задача, выбрать себе кружок и написать функцию,
которая дорисует что-то на вашем кружочке.

"""

"""
Запишите сюда название функции, автора и номер вашей окружности.

0, mll, Миллер Лина Львовна
1,
2,

"""

from tkinter import *


# --- Miller Lina Lvovna ---------------------

# --- ??? ---------------------    

# --- ??? ---------------------

# --- ??? ---------------------





# --- main ---------------------    

root = Tk()
root.geometry("900x600+0+0")
root.title("Hello, 10b!")

canvas = Canvas(root, width=896, height=596, bg="white") 
canvas.pack()


r = 50
x = r + 40
y = r + 100
list_circles = []
for k in range(3):
    for i in range(5):
        a = canvas.create_oval(x-r, y-r, x+r, y+r, outline="black",
                               fill="white", width=5)
        x += 2 * r + 80
        list_circles.append(a)
    x = r + 40
    y += 2 * r + 60
'''
for k in range(15):
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
'''

# --- ??? ---------------------    

# --- ??? ---------------------

# --- ??? ---------------------



canvas.mainloop()


