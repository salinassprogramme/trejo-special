#coding:utf8


import math as mt
import  numpy as np 
import sympy as sp 

x=sp.symbols('x')

def main():
    f=str(input('Introduzca su función f(x): '))
    p=float(input('Introduzca la abscisa (x) de su evaluación: '))
    h1=float(input('Introduzca su diferencia h1: '))
    q=str(input('¿Desea utilizar extrapolación de Richardson[s/n}]: ?'))
    func=getfunction(f)
    dx=sp.diff(func,x)
    andx=dx.evalf(subs={x:p})

    print('Diferencia frontal h')
    numdx=difffronth(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)
    print('Diferencia frontal h^2')
    numdx=difffronth2(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)
    print('Diferencia por atrás h')
    numdx=diffbackh(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)
    print('Diferencia por atrás h^2')
    numdx=diffbackh2(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)
    print('Diferencia centrada h^2')
    numdx=diffcenth2(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)
    print('Diferencia centrada h^4')
    numdx=diffcenth4(func,h1,p)
    print(numdx)
    e=abs((numdx-andx)/andx)*100
    print('Error relativo % (contra el algoritmo sympy)')
    print(e)

    if q=='S' or q=='s':
        h2=float(input('Introduzca su h2: '))
        print('Interpolación de Richardson')
        numdx=richardson(func,h1,h2,p)
        print(numdx)
        e=abs((numdx-andx)/andx)*100
        print('Error relativo % (contra el algoritmo sympy)')
        print(e)
    
def difffronth(func,h,p):
    return((func.evalf(subs={x:p+h})-func.evalf(subs={x:p}))/h)

def diffbackh(func,h,p):
    return((func.evalf(subs={x:p})-func.evalf(subs={x:p-h}))/h)

def difffronth2(func,h,p):
    return((-func.evalf(subs={x:p+2*h})+4*func.evalf(subs={x:p+h})-3*func.evalf(subs={x:p}))/(2*h))

def diffbackh2(func,h,p):
    return((func.evalf(subs={x:p-2*h})-4*func.evalf(subs={x:p-h})+3*func.evalf(subs={x:p}))/(2*h))

def diffcenth2(func,h,p):    
    return(func.evalf(subs={x:p+h})-func.evalf(subs={x:p-h}))/(2*h)

def diffcenth4(func,h,p):
    return((-func.evalf(subs={x:p+2*h})+8*func.evalf(subs={x:p+h})-8*func.evalf(subs={x:p-h})+func.evalf(subs={x:p-2*h}))/(12*h))

def richardson(func,h1,h2,p):
    return((4/3)*diffbackh2(func,h2,p)-(1/3)*diffbackh(func,h1,p))

def getfunction(f):
    global x 
    return(sp.sympify(f))

if __name__=='__main__':
    main()
