import matplotlib.pyplot as plt

n = 5
x = [1, 1]
y = [1, 1]
T = [-1, 1.5]

for i in range(1, n+1):
    for j in range(len(T)):
        x[j], y[j] = (x[j] + y[j]*T[j], x[j] - y[j]*T[j])
    for j in range(len(T)-1):
        plt.arrow(x[j], y[j], x[j+1]-x[j], y[j+1]-y[j], head_width=1, head_length=1, alpha=.3, fc='k')
    plt.plot(x, y, alpha=.7, label=f"{i} i")


for t, c in zip(T, ['g', 'b']):
    x, y = (1, 1)
    xs, ys = [x], [y]
    for i in range(1, n+1):
        x, y = (x + y*t, x - y*t)
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, '.-', c=c, alpha=.5, label=f"T = {t}")


plt.legend()
plt.savefig("../images/plot3.png")
plt.show()
