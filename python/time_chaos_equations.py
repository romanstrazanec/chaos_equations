import numpy as np
import matplotlib.pyplot as plt


class Equation:
    def __init__(s, t, fx, fy):
        s.t, s.fx, s.fy = t, fx, fy


DPPREG = Equation(np.array([0.01, 0.020694, 0.025791, 0.038996]),
    lambda x, y, t: -x*x+x*t+y,
    lambda x, y, t: x*x-y*y-t*t-x*y+y*t-x+y)


RMCQDI = Equation(np.array([-0.279089, -0.178329]),
    lambda x, y, t: x*x-y*y-t*t-x-t,
    lambda x, y, t: y*y+t*t-x*y-y-t)


LDNMGQ = Equation(np.array([0.107979, 0.108236]),
    lambda x, y, t: -t*t-x*y+t,
    lambda x, y, t: -x*y+x*t+y+t)


RANDOM = Equation(np.array([0, 0.5, 1]),
    lambda x, y, t: x+y*t,
    lambda x, y, t: x-y*t)


def calculate(eq, n):
    xs, ys = [eq.t], [eq.t]
    while len(xs) < n:
        xs.append(eq.fx(xs[-1], ys[-1], eq.t))
        ys.append(eq.fy(xs[-2], ys[-1], eq.t))
    return (xs, ys)


def plot_time_change(x, y, n):
    for i in range(n):
        plt.scatter(x[i], y[i], s=.3)
        plt.plot(x[i], y[i], lw=.3)


def plot_iteration(x, y):
    plt.scatter(x, y, s=.3)
    plt.plot(x, y, lw=.3)


if __name__ == '__main__':
    n = 100 # number of iterations
    x, y = calculate(DPPREG, n)

    plot_time_change(x, y, n)
    plt.axvline(lw=.2, c='k')
    plt.axhline(lw=.2, c='k')
    plt.show()

    plot_iteration(x, y)
    plt.axvline(lw=.2, c='k')
    plt.axhline(lw=.2, c='k')
    plt.show()
    # plt.plot(, lw=.3)
    # plt.show()
