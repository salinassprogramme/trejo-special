#coding:utf8
import sympy as sp
x=sp.symbols('x')

def main():
    eq=str(input('Introduzca su expresión: '))
    value=float(input('Introduzca el valor a evaluar: '))
    f=getfunction(eq)
    print(f.evalf(subs={x:value}))
    """
    xr=0.1
    xl=1
    xu=2

    e=100
    flag=False
    
    while(e>=0.001 and flag!=True):
        temp=xr
        xr=(xu+xl)/2

        e=abs((xr-temp)/(temp))*100
        a=f.evalf(subs={x:xr})
        b=f.evalf(subs={x:xl})
        if(a*b<0):
            xu=xr
        elif(a*b>0):
            xl=xr
        else:
            flag=True
    print(xr)

"""
def getfunction(ec):
    global x
    return(sp.sympify(ec))

if __name__=='__main__':
    main()
