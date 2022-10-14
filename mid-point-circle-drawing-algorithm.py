import matplotlib.pyplot as plt
r = int(input())
xc = int(input())
yc = int(input())

x = []
y = []

def plotpoints(xc,yc,x1,y1):
    global x,y
    x.append(xc + x1)
    y.append(yc + y1)

    x.append(xc - x1)
    y.append(yc + y1)

    x.append(xc + x1)
    y.append(yc - y1)

    x.append(xc - x1)
    y.append(yc - y1)

    x.append(xc + y1)
    y.append(yc + x1)

    x.append(xc - y1)
    y.append(yc + x1)

    x.append(xc + y1)
    y.append(yc - x1)

    x.append(xc - y1)
    y.append(yc - x1)


x1 = 0
y1 = r

plotpoints(xc,yc,x1,y1)

pk = 1 - r
while(x1 < y1):
    if(pk < 0):
        x1 +=0.005
        pk = pk + 2*x1 + 1
    else:
        x1 += 0.005
        y1 -= 0.005
        pk = pk + 2*x1 + 1 - 2*y1
    
    plotpoints(xc,yc,x1,y1)


plt.scatter(x,y)
#plt.plot(x,y)
plt.show()
