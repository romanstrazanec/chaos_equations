import matplotlib.pyplot as plt

n = 10 # number of iterations
x, y = (1, 1) # initial coordinates
T = -1 # arbitrary constant

xs, ys = [x], [y]
for i in range(1, n+1): # repeat n times
    new_x = x + y*T # calculate new x
    new_y = x - y*T # calculate new y
    x, y = (new_x, new_y) # set x, y to new_x, new_y respectively
    xs.append(x)
    ys.append(y)
    print(f"{i}. iteration [x, y] = [{x}, {y}]")

plt.scatter(xs, ys, c='g')
plt.plot(xs, ys, c='g')
plt.savefig("../images/plot2.png")
plt.show()
