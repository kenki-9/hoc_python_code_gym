
import turtle
import math

# đặt nền màu xanh
screen = turtle.Screen()
screen.bgcolor("gray")

T = turtle.Turtle()
T.color("black")
T.shape("turtle")
T.speed(10)

#vẽ hình hình chữ nhật để vẽ nhà

def veHCN(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
#vẽ hình tam giá để vẽ mái nhà và cây
def veHTG(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()
  
#vẽ hình bình hành để vẽ cạnh nhà
def veHBH(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
#vẽ tia nắng
def ve_tia_nang(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)


T.penup() 
T.goto(-150, -120)
T.pendown()
veHCN(T, 100, 110, "blue")

# vẽ cửa
T.penup()
T.goto(-120, -120)
T.pendown()
veHCN(T, 40, 60, "lightgreen")

# vẽ mái
T.penup()
T.goto(-150, -10)
T.pendown()
veHTG(T, 100, "magenta")

# vẽ cạnh nhà
T.penup()
T.goto(-50, -120)
T.pendown()
veHBH(T, 60, 110, "yellow")

# vẽ cửa sổ
T.penup()
T.goto(-30, -60)
T.pendown()
veHBH(T, 20, 30, "brown")

# 
T.penup()
T.goto(-50, -10)
T.pendown()
T.fillcolor("orange")
T.begin_fill()
T.left(30)
T.forward(60)
T.left(105)
T.forward(100 / math.sqrt(2))
T.left(75)
T.forward(60)
T.left(105)
T.forward(100 / math.sqrt(2))
T.left(45)
T.end_fill()

# vẽ thân cây
T.penup() 
T.goto(100, -130)
T.pendown()
veHCN(T, 20, 40, "brown")

# vẽ ngọn cây
T.penup() 
T.goto(65, -90)
T.pendown()
veHTG(T, 90, "lightgreen")
T.penup() 
T.goto(70, -45)
T.pendown()
veHTG(T, 80, "lightgreen")
T.penup() 
T.goto(75, -5)
T.pendown()
veHTG(T, 70, "lightgreen")

# vẽ mặt trời
T.penup() 
T.goto(55, 110)
T.fillcolor("yellow")
T.pendown()
T.begin_fill()
T.circle(24)
T.end_fill()

# vẽ tia nắng mặt trời
T.penup()
T.goto(55, 134)
T.pendown()
ve_tia_nang(T, 25, 24)
T.right(45)
ve_tia_nang(T, 15, 24)
T.left(45)


T.penup()
T.goto(-100, -150)
T.left(90)

turtle.done()