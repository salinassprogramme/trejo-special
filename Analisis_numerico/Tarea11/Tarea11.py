#coding:utf8

import sympy as sp
import numpy as np

x=sp.symbols('x')

def main():
    f=str(input('Introduzca su función: '))
    a=float(input('Introduzca su límite inferior de integración: '))
    b=float(input('Introduzca su límite superior de integración: '))
    metodos=['Simpson 1/3 [S1/3]','Simpson 3/8 [S3/8]','Trapecio simple [TS]', 'Trapecio compuesto [TC]']
    print(metodos)
    m=str(input('Introduzca su método de integración: '))
    if (m=='S1/3'):
        res=simpson13(f,a,b)
    elif(m=='S3/8'):    
        res=simpson38(f,a,b)
    elif(m=='TS'):
        res=trapeciosimple(f,a,b)
    elif(m=='TC'):
        n=int(input('Introduzca el número de iteraciones deseado: '))
        res=trapeciocomp(f,a,b,n)
    print(res)

def simpson13(f,a,b):
    eq=getfunction(f)
    m=(a+b)/2
    return((b-a)/6)*(eq.evalf(subs={x:a})+4*eq.evalf(subs={x:(a+b/2)})+eq.evalf(subs={x:b}))

def simpson38(f,a,b):
    eq=getfunction(f)
    return((3*((b-a)/3)/8)*(eq.evalf(subs={x:a})+3*eq.evalf(subs={x:((2*a+b)/3)})+3*eq.evalf(subs={x:((a+2*b)/3)})+eq.evalf(subs={x:b})))

def trapeciosimple(f,a,b):
    eq=getfunction(f)
    return(((b-a)/2)*(eq.evalf(subs={x:a})+eq.evalf(subs={x:b})))

def trapeciocomp(f,a,b,n):
    eq=getfunction(f)
    sum=0
    for i in range(1,n):
        xi=a+i*((b-a)/n)
        sum=sum+eq.evalf(subs={x:xi})
    c=(eq.evalf(subs={x:a})+eq.evalf(subs={x:b}))/2
    return(((b-a)/n)*(c+sum))

def getfunction(f):
    global x
    return(sp.sympify(f))

if __name__=='__main__':
    main()
