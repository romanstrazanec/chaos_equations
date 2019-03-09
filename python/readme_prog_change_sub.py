import matplotlib.pyplot as plt

n = 5
T = [-1, -.5, 0., .5, 1]
x = [1] * len(T)
y = [1] * len(T)

plt.subplot(122)
for i in range(1, n+1):
    for j in range(len(T)):
        x[j], y[j] = (x[j] + y[j]*T[j], x[j] - y[j]*T[j])
    for j in range(len(T)-1):
        plt.arrow(x[j], y[j], x[j+1]-x[j], y[j+1]-y[j], head_width=.35, head_length=.35, alpha=.3, fc='k')
    plt.plot(x, y, alpha=.7, label=f"{i} i")

plt.subplot(121)
for t in T:
    x, y = (1, 1)
    xs, ys = [x], [y]
    for i in range(1, n+1):
        x, y = (x + y*t, x - y*t)
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, '.-', alpha=.5, label=f"T = {t}")


plt.legend()
plt.subplot(122)
plt.legend()
plt.savefig("../images/plot4sub.png")
plt.show()
