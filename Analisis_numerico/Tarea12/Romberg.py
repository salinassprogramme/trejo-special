#coding:utf8
import numpy as np
import sympy as sp
import math as mt

x=sp.symbols('x')

def main():
    aproximaciones=[]
    f=str(input('Introduzca su función: '))
    a=float(input('Introduzca su límite inferior de integración: '))
    b=float(input('Introduzca su límite superior de integración: '))
    h=int(input('Introduzca el orden h del método: '))
    
    func=getfunction(f)

    for i in range(2,h+1,2):
        aproximaciones.append(trapeciocomp(func,a,b,i))
    count=2
    res=romberg(aproximaciones,count)
    print(res)

def romberg(l,c):
    
    if (len(l)==1):
        return(l)

    v=[]
    for i in range(0,len(l)-1):
        ap=(4**(c-1)*l[i+1]-l[i])/(4**(c-1)-1)
        v.append(ap)
    c+=1
    return(romberg(v,c))
             

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
