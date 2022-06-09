#coding:utf8
import numpy as np
import sympy as sp
import math as mt

x=sp.symbols('x')
w2=[1,1]
w3=[0.55555,0.88888,0.55555]
w4=[0.3478548451,0.6521451549,0.3478548451,0.6521451549]
w5=[0.2369268851,0.4786286705,0.2369268851,0.4786286705,0.5688]
x2=[0.5773502692,-0.5773502692]
x3=[0.7745966692,0,-0.7745966692]
x4=[0.8611363113,0.3399810536,-0.3399810536,-0.8611363113]
x5=[0.9061798459,0.5384693101,0,-0.5384693101,-0.9061798459]

def main():
    f=str(input('Introduzca su función: '))
    a=float(input('Introduzca su límite inferior de integración: '))
    b=float(input('Introduzca su límite superior de integración: '))
    func=getfunction(f)
    n=int(input('Introduzca el número de iteraciones deseada: '))
    if n<=5 and n>1:
        gauss(func,a,b,n)

def gauss(func,a,b,n):
    global w2
    global w3
    global w4
    global w5
    global x2
    global x3
    global x4
    global x5
    w=[]
    z=[]
    k=(b-a)/(2)
    sum1=0
    
    if(n==2):
        w=w2
        z=x2
    elif(n==3):
        w=w3
        z=x3
    elif(n==4):
        w=w4
        z=x4
    elif(n==5):
        w=w5
        z=x5

    for i in range(0,len(w)):
        xi=((b-a)/(2))*z[i]+((a+b)/(2))
        sum1=w[i]*func.evalf(subs={x:xi})

    res=sum1*k
    print(res)


def getfunction(f):
    global x
    return(sp.sympify(f))
    
if __name__=='__main__':
    main()
