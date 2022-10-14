import matplotlib.pyplot as plt
import math as m
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))
xinc = dx/steps
yinc = dy/steps

i = 1
x = x1
y = y1

xc = []
yc = []

for i in range(0,steps+1):
    xc.append(round(x))
    yc.append(round(y))

    x += xinc
    y += yinc

plt.plot(xc,yc)
plt.scatter(xc,yc)
plt.show()
