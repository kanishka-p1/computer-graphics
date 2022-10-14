import matplotlib.pyplot as plt
print("Enter starting coordinates: ")
x1 = int(input())
y1 = int(input())
print("Enter ending coordinates: ")
x2 = int(input())
y2 = int(input())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

x = []
y = []

x.append(x1)
y.append(y1)
plt.scatter(x,y)

pk = 2*dy - dx
for i in range(x1,x2):
    x1 = x1+1
    if(pk < 0):
        x.append(x1)
        y.append(y1)
        plt.scatter(x,y)
        pk = pk + 2*dy
    else:
        y1 = y1 + 1
        x.append(x1)
        y.append(y1)
        plt.scatter(x,y)
        pk = pk + 2*dy - 2*dx
    
plt.plot(x,y)
plt.show()
