import math
import numpy
import pandas
import sympy

x=sympy.symbols('x')
xi=sympy.symbols('xi')
xl=sympy.symbols('xl')
xu=sympy.symbols('xu')

def main():
    l=['Newton-Raphson[NR]','Punto fijo[PF]','Secante[Sec]']
    func=str(input('Introduzca su función: '))
    print(l)
    metodo=str(input('Seleccione el método para encontrar una raíz: ')
            )
    x0=float(input('Ahora introduzca su valor inicial: '))
    emax=float(input('Finalmente, introduzca el factor de tolerancia: '))
    if(metodo=="NR"):
        print(NR(func,x0,emax))
    elif(metodo=="PF"):
        print(PF(func,x0,emax))
    elif(metodo=="Sec"):
        print(Sec(func,x0,emax))

def getfunction(f):
    global x
    global xi
    global xl
    global xu
    return(sympy.sympify(f))

def NR(eq,x0,emax):
    global x
    ecuacion=getfunction(eq)
    derivada= sympy.diff(ecuacion)
    f_NR=x-(ecuacion/derivada)
    e=100
    xr=x0
    while(e>emax):
        temp=xr
        xr=f_NR.evalf(subs={x:temp})
        if(xr!=0):
            e=abs((xr-temp)/xr)*100
    return(xr)
    
def PF(eq,x0,emax):
    global x
    ecuacion=getfunction(eq)
    xr=x0
    e=100
    while(e>emax):
        temp=xr
        xr= ecuacion.evalf(subs={x:temp})
        if(xr!=0):
            e=abs((xr-temp)/xr)*100
    return(xr)

def Sec(eq,x0,emax):
    global x
    global xi
    global xl
    global xu
    ecuacion=getfunction(eq)
    a=eq.replace("x","xl")
    ecuacion2=getfunction(a)
    f_Sec=x-((ecuacion*(xl-x))/(a-ecuacion))
    temp1=x0
    temp2=1
    temp3=0
    xr=x0
    e=100
    while(e>emax):
        xr=f_Sec.evalf(subs={x:temp1,xl:temp2})
        temp3=ecuacion.evalf(subs={x:xr})
        if(xr!=0):
            e=abs((xr-temp1)/(temp1))*100
        if(ecuacion.evalf(subs={x:temp1})*temp3 < 0):
                temp1=temp1
                temp2=temp3
        elif(ecuacion.evalf(subs={x:temp2})*temp3 < 0):
            temp1=temp3
            temp2=temp2
        elif(temp3==0):
            return(xr)
        else:
            return(None)
    return(xr)




if __name__ =='__main__':
    main()
