#coding:utf8

import numpy as np
import sympy 

x=sympy.symbols('x')
y=sympy.symbols('y')
x1=sympy.symbols('x1')
x2=sympy.symbols('x2')

def main():
    func1=str(input('Introduzca su ecuación 1: '))
    func2=str(input('Introduzca su ecuación 2: '))
    e=float(input('Introduzca su tolerancia :'))
    xi=float(input('Introduzca el valor inicial de x/x1: '))
    yi=float(input('Introduzca el valor inicial de y/x2: '))
    print(NRNL(func1,func2,e,xi,yi))

def NRNL(f1,f2,ea,xi,yi):
    
    xr=xi
    yr=yi
    u=getfunction(f1)
    v=getfunction(f2)
    dux=sympy.diff(u,x)
    duy=sympy.diff(u,y)
    dvx=sympy.diff(v,x)
    dvy=sympy.diff(v,y)
    fNRx=x-(u*dvy-v*duy)/(dux*dvy-duy*dvx)
    fNRy=y-(v*dux-u*dvx)/(dux*dvy-duy*dvx)
    e1=100
    e2=100
    respuestas=[]

    while(e1>=ea and e2>=ea):
        temp1=xr
        temp2=yr
        xr=fNRx.evalf(subs={x:temp1,y:temp2})
        yr=fNRy.evalf(subs={x:temp1,y:temp2})
        if(xr!=0):
            e1=abs((xr-temp1)/xr)*100
        if(yr!=0):
            e2=abs((yr-temp2)/yr)*100
        

    respuestas.append(xr)
    respuestas.append(yr)

    return(respuestas)



def getfunction(f):
    global x
    global y 
    return sympy.sympify(f)

if __name__=='__main__':
    main()
