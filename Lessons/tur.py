# from turtle import *
#
# left(30)
# speed(0)
# i = 0
# k = 3000
# color("Black", "Green")
# begin_fill()
# forward(12 * k)
# left(120)
# forward(12 * k)
# right(150)
# forward(12 * k)
# right(90)
# forward(12 * k)
# right(90)
# forward(12 * k)
# end_fill()
# up()
# canvas = getcanvas()
# counter = 0
#
# for i in range(-20 * k, 20 * k, k):
#     for j in range(-20 * k, 20 * k, k):
#         root = canvas.find_overlapping(i, j, i, j)
#         if len(root) == 1 and root[0] == 5:
#             counter += 1
# print(counter)
# done()


from turtle import *
from random import randint
from time import sleep

w = 200
h = 200

t1 = Turtle()
t1.color('blue')
t1.width(5)
t1.shape('turtle')

t2 = Turtle()
t2.color('green')
t2.width(5)
t2.left(120)
t2.shape('turtle')

t3 = Turtle()
t3.color('red')
t3.width(5)
t3.left(-120)
t3.shape('turtle')

def catch1(x, y):
    t1.penup()
    t1.goto(randint(-100,100),randint(-100,100))
    t1.pendown()
    t1.left(randint(0, 180))

def catch2(x, y):
    t2.penup()
    t2.goto(randint(-100,100),randint(-100,100))
    t2.pendown()
    t2.left(randint(0, 180))

def catch3(x, y):
    t3.penup()
    t3.goto(randint(-100,100),randint(-100,100))
    t3.pendown()
    t3.left(randint(0, 180))

def gameFinished(t1, t2, t3):
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    isOutside = t1_outside or t2_outside or t3_outside
    return isOutside

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while gameFinished(t1, t2, t3) != True:
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)

t1.clear()
t2.clear()
t3.clear()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

print("Спасибо за игру, надеюсь вы к нам ещё заглянете!")
feedback = input("Пожалуйста, введите отзыв")
feedback_result = feedback.lower()
length = int(len(feedback_result))
awful = int(feedback_result.find("ужасно"))
bad = int(feedback_result.find("плохо"))
not_good = int(feedback_result.find("не очень"))
negative_count = awful+bad+not_good
if negative_count == -2:
    negative_count = 1
if negative_count == -1:
    negative_count = 0
if negative_count == -3:
    negative_count = 2
print("Длина отзыва:", length)
print("Количество негатива:", negative_count)

exitonclick()