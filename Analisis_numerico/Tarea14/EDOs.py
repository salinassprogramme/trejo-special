#coding:utf8

import math as mt
import numpy as np
import sympy as sp
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt

x=sp.symbols('x')
y=sp.symbols('y')
t=sp.symbols('t')

def main():

    t = 0
    y = 0
    dt = 0
    ys = [] 
    ts = []

    t=float(input('Introduzca su valor inicial para x: '))
    y=float(input('Introduzca su valor inicial para y: '))
    dt=float(input('Introduzca su salto h: '))
    n=float(input('Introduzca su valor máximo de x: '))
    eq=str(input('Introduzca su ecuación: '))
    func=getfunc(eq)
    eq=str(input('Introduzca su solución analítica: '))

    while t <= n:
        y = runge_kutta(y, t, dt, func)
        t += dt
        ys.append(y)
        ts.append(t)

    func2=getfunc(eq)
    exact = [func2.evalf(subs={x:t}) for t in ts]
    plt.plot(ts, ys, label='runge_kutta')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    error = np.array(exact) - np.array(ys)
    print("max error {:.5f}".format(max(error)))

    while t <= n:
        y = euler(y, t, dt, func)
        t += dt
        ys.append(y)
        ts.append(t)

    func2=getfunc(eq)
    exact = [func2.evalf(subs={x:t}) for t in ts]
    plt.plot(ts, ys, label='Euler')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    error = np.array(exact) - np.array(ys)
    print("max error {:.5f}".format(max(error)))

    while t <= n:
        y = heun(y, t, dt, func)
        t += dt
        ys.append(y)
        ts.append(t)

    func2=getfunc(eq)
    exact = [func2.evalf(subs={x:t}) for t in ts]
    plt.plot(ts, ys, label='Heun')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    error = np.array(exact) - np.array(ys)
    print("max error {:.5f}".format(max(error)))

def runge_kutta(y0, x0, dx, f):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """

    k1 = dx * f.evalf(subs={y:y0,x:x0})
    k2 = dx * f.evalf(subs={y:y0 + 0.5 * k1,x : x0 + 0.5 * dx})
    k3 = dx * f.evalf(subs={y:y0 + 0.5 * k2, x:x0 + 0.5 * dx})
    k4 = dx * f.evalf(subs={y:y0 + k3, x:x0 + dx})
    return (y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

def euler(y0,x0,dx,f):
    k1 = dx * f.evalf(subs={y:y0,x:x0})
    return (y0+k1)

def heun(y0,x0,dx,f):
    y10=y+f.evalf(subs={y:y0,x:x0})*dx
    yi1=y+(f.evalf(subs={y:y0,x:x0}+f(subs={y:y10,x:x+dx})))/2
    return(yi1)

def getfunc(f):
    global x
    global y
    return (sp.sympify(f))





if __name__=='__main__':
    main()
