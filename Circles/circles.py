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
2, nik, Пономарев Никита
...
9, polly, Ефимова Полина
"""

from tkinter import *


# --- Miller Lina Lvovna ---------------------
def mll(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="#ffff77", outline="#ffaa77", width=2)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    nose = canvas.create_polygon(x-5, y+5, x, y-5, x+5, y+5, fill="#ffaa77")
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="blue", outline="blue")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="blue", outline="blue")
    mouth = canvas.create_arc(x-20, y-5, x+20, y+35, start=190, extent=160,
                              fill="#ffaa77", outline="red", width=5, style=ARC)
    #h1 = canvas.create_arc(x+30, y-50, x+60, y-20, start=20, extent=350,
    #                          style=ARC, outline="red", width=5)

    b1 = canvas.create_polygon(x-35, y-35, x-50, y-20, x-60, y-25,
                               x-35, y-35, x-20, y-50, x-40, y-55,
                               fill="green")


# --- Efimova Polina ---------------------
def polly(ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="#e7e784", outline="#e7bc0b", width=5)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22,x-13 , y-8, fill="white",outline="#e7e784")
    eye_right1 = canvas.create_oval(x-24, y-15, x-16, y-8, fill="black",outline="black")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="white", outline="#e7e784")
    eye_left1 = canvas.create_oval(x+16, y-15, x+24, y-8, fill="black",outline="black")
    rot = canvas.create_oval(x-25,y+10, x+25, y+30, fill="#f73110",outline="#f73110")
    rrot = canvas.create_oval(x-25,y+5, x+25, y+25, fill="#e7e784",outline="#e7e784")
    tongue = canvas.create_oval(x-9,y+27, x+9, y+35, fill="#f73110",outline="#f73110")
    palka = canvas.create_line(x,y+28,x,y+34,fill="black",width=1)
    
# --- Ponomarev Nikita---------------------
def nik (ls_circle, k):
    """
     mll - 
    """
    face = ls_circle[k]
    canvas.itemconfig(face, fill="yellow", outline="black", width=2)
    n = (k // 5)
    m = (k % 5)
    x = r + 40 + m * (2 * r + 80)
    y = r + 100 + n * (2 * r + 60)
    eye_right = canvas.create_oval(x-27, y-22, x-13, y-8, fill="blue", outline="blue")
    eye_left = canvas.create_oval(x+13, y-22, x+27, y-8, fill="blue", outline="blue")
    mouth = canvas.create_arc(x-40, y-5, x+40, y+25, start=190, extent=160,
                              fill="black", outline="black", width=5, style=ARC)
    glass_left =canvas.create_oval(x+10, y-25, x+ 30, y-5,outline="black")
    glass_right = canvas.create_oval(x-30, y-25, x-10, y-5, outline="black")
    glass = canvas.create_line(400,135,500,135, fill="black")


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
# --- Miller Lina Lvovna ---------------------    
mll(list_circles, 0)

# --- Efimova Polina ---------------------
polly(list_circles,9)

# --- Ponomarev Nikita ---------------------
nik(list_circles, 2)

# --- ??? ---------------------

canvas.mainloop()


