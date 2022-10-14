import matplotlib.pyplot as plt
rx = int(input())
ry = int(input())
xc = int(input())
yc = int(input())

x = []
y = []

x1 = 0
y1 = ry

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


pk = ry*ry - rx*rx*ry + (1/4)*rx*rx
while(2*ry*ry*x1 < 2*rx*rx*y1):
    if(pk < 0):
        x1 += 1
        pk = pk + 2*ry*ry*x1 + ry*ry
        plotpoints(xc,yc,x1,y1)
    else:
        x1 += 1
        y1 -= 1
        pk = pk + 2*ry*ry*x1 -2*rx*rx*y1 + ry*ry
        plotpoints(xc,yc,x1,y1)
    
p2k = ry*ry*(x1+1/2)*(x1+1/2) + rx*rx*(y1-1)*(y1-1) - rx*rx*ry*ry

while(y1>0):
    if(p2k > 0):
        y1 -= 1
        p2k = p2k - 2*rx*rx*y1 + rx*rx
        plotpoints(xc,yc,x1,y1)
    else:
        x1 += 1
        y1 -= 1
        p2k = p2k + 2*ry*ry*x1 - 2*rx*rx*y1 + rx*rx
        plotpoints(xc,yc,x1,y1)


#plt.plot(x,y)
plt.scatter(x,y)
plt.show()
