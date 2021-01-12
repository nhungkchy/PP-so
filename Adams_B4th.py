import numpy as np
import matplotlib.pyplot as plt


def feval(funcName, *args):
    return eval(funcName)(*args)


def RungeKutta4thOrder(func, y0, x_range, h):
    m = len(y0)
    n = int((x_range[-1] - x_range[0]) / h)

    x = x_range[0]
    y = y0

    xsol = np.empty((0))
    xsol = np.append(xsol, x)

    ysol = np.empty((0))
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)

        yp2 = y + k1*(h/2)

        k2 = feval(func, x+h/2, yp2)

        yp3 = y + k2*(h/2)

        k3 = feval(func, x+h/2, yp3)

        yp4 = y + k3*h

        k4 = feval(func, x+h, yp4)

        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])

        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])

    return [xsol, ysol]


def ABM4thOrder(func, yinitial, xspan, h):

    m = len(yinitial)

    dx = int((xspan[-1] - xspan[0]) / h)

    xrk = [xspan[0] + k * h for k in range(dx + 1)]

    trk4 = np.array([xrk[0], xrk[1], xrk[2], xrk[3]])

    [xx, yy] = RungeKutta4thOrder(func, yinitial, trk4, h)

    x = xx
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    y = yy
    yn = yy[0:m]
    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(3, dx):
        x00 = x[i]; x11 = x[i-1]; x22 = x[i-2]; x33 = x[i-3]; xpp = x[i]+h

        y00 = y[m*i:]
        y11 = y[m*(i - 1):m*i]
        y22 = y[m*(i - 2):m*(i-1)]
        y33 = y[m*(i - 3):m*(i-2)]

        y0prime = feval(func, x00, y00)
        y1prime = feval(func, x11, y11)
        y2prime = feval(func, x22, y22)
        y3prime = feval(func, x33, y33)

        ypredictor = y00 + (h/24)*(55*y0prime - 59*y1prime + 37*y2prime - 9*y3prime)
        ypp = feval(func, xpp, ypredictor)

        for j in range(m):
            yn[j] = y00[j] + (h/24)*(9*ypp[j] + 19*y0prime[j] - 5*y1prime[j] + y2prime[j])

        xc = x[i] + h
        xsol = np.append(xsol, xc)

        x = xsol

        ysol = np.append(ysol, yn)

        y = ysol

    return [xsol, ysol]


def myFunc(x, y):
    '''
    Example from Computational Cell Biology, Fall et al
    Exercise #1 of Chapter 9, page 256
    '''
    dy = np.zeros((len(y)))
    a = 1; b = 5; c = 4; r = 1; y0 = 0; epsi = 0.1
    dy[0] = ((a + b*y[0]**2)/(1 + y[0]**2 + r*y[1])) - y[0]
    dy[1] = epsi*(c*y[0] + y0 - y[1])
    return dy


h = 0.1
xspan = np.array([1.0, 100.0])
yinit = np.array([1.0, 1.0])


[ts, ys] = ABM4thOrder('myFunc', yinit, xspan, h)
# print(ys)

node = len(yinit)
ys1 = ys[0::node]
ys2 = ys[1::node]
print(ys1, ys2)


# plt.plot(ts, ys1, 'r')
# plt.plot(ts, ys2, 'b')
# plt.xlim(xspan[0], xspan[1])
# plt.legend(["x(t)", "y(t)"], loc=1)
# plt.xlabel('Time (t)', fontsize=17)
# plt.ylabel('Solutions', fontsize=17)
# plt.tight_layout()
# plt.show()