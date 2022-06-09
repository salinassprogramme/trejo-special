#coding:utf8

import math
import numpy
import sympy

x=sympy.symbols('x')

def main():
    func=str(input('Introduzca su función: '))
    x0=float(input('Introduzca su valor inicial: '))
    emax=float(input('Introduzca su factor de tolerancia: '))
    NR(func,emax,x0)


def getfunction(f):
    global x
    return(sympy.sympify(f))


def NR(eq,ed,x0):
    global x
    xr=complex(x0)
    ecuacion=getfunction(eq)
    derivada1=sympy.diff(ecuacion)
    derivada2=sympy.diff(derivada1)
    ea=100
    e=100
    temp=0
    preliminares=[]
    resultados=[]
    error=[]
    iteraciones=[]
    f_NR=x-(((ecuacion)*(derivada1))/((derivada1)**2-((ecuacion)*(derivada2))))
    intentos=0
    
    while(intentos<1000 and round(xr.imag)==0):
        while(ea>ed):
            temp=complex(xr)
            xr=complex(f_NR.evalf(subs={x:temp}))
            if(xr!=0):
                ea=abs((xr-temp)/temp)
            error.append(e)
            iteraciones.append(intentos)
            print(xr)
        if(xr.real in preliminares and xr.real not in resultados):
            resultados.append(xr.real)
        elif(xr.real not in preliminares):
            preliminares.append(xr.real)
        else:
            break
        e=ea
        ea=100
        plt.clf()
        plt.cla()
        plt.plot(iteraciones,error,label='E_s %')
        plt.xlabel('Iteraciones')
        plt.ylabel('Error')
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.title('Falsa posición 5.11')
        plt.savefig(f'{intentos}')
        error=[]
        iteraciones=[]
        if(abs(xr)==0):
            xr=-100*(temp+0.0001)
        elif(abs(xr)==1):
            xr=-100*(temp+0.0001)
        else:
            xr=-100*temp
        intentos+=1
        print(intentos)
    print(resultados)

if __name__ =='__main__':
    main()
