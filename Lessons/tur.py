from turtle import *

left(30)
speed(0)
i = 0
k = 3000
color("Black", "Green")
begin_fill()
forward(12 * k)
left(120)
forward(12 * k)
right(150)
forward(12 * k)
right(90)
forward(12 * k)
right(90)
forward(12 * k)
end_fill()
up()
canvas = getcanvas()
counter = 0

for i in range(-20 * k, 20 * k, k):
    for j in range(-20 * k, 20 * k, k):
        root = canvas.find_overlapping(i, j, i, j)
        if len(root) == 1 and root[0] == 5:
            counter += 1
print(counter)
done()
