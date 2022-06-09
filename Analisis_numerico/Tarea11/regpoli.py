#coding:utf8

import numpy as np
import math as mt
import matplotlib.pyplot as pt
import sympy as sp

x=sp.symbols('x')
e=sp.symbols('e')

def main():

    x=[]
    
    n=int(input('Introduzca el tamaño de su muestra: '))
    intentos=int(input('¿Cuántas regresiones quiere intentar: ?'))
    
    m=0
    
    y=np.zeros((n,1))

    for i in range(n):
        x.append(float(input(f'Introduzca su dato {i+1} para x: ')))
    
    i=0

    for i in range(n):
        y[i][0]=(float(input(f'Introduzca su dato {i+1} para y: ')))

    xmin=float(input('¿Cuál será el valor mínimo para evaluar su función?: '))
    xmax=float(input('¿Cuál será el valor máximo para evaluar su función?: '))

    while(m<intentos):
        regpoli(n,m,x,y,xmin,xmax)
        m+=1
    
    regexp(n,x,y,xmin,xmax)
    reglog(n,x,y,xmin,xmax)


def regpoli(n,m,x,y,xmin,xmax):

    xarr=np.zeros((n,m+1))

    for i in range(0,m+1):
        for j in range(0,len(x)):
            xarr[j][i]=x[j]**i
    
    
    xT=np.transpose(xarr)

    xxT=np.dot(xT,xarr)

    xxTinv=np.linalg.inv(xxT)

    xTy=np.dot(xT,y)

    res=np.dot(xxTinv,xTy)

    respuesta=str('')

    for i in range(0,m+1):
        b=float(res[i])
        if (i==0):
            respuesta=respuesta+(f'{b}*x**{i}')
        else:
            respuesta=respuesta+(f'+{b}*x**{i}')

    print(respuesta)

    file=open("resultados.txt","a")
    file.write(f'{respuesta}\n')
    file.close()
    data=generatedata(xmin,xmax,respuesta)
    pt.clf()
    pt.rcParams.update({'font.size':6})
    pt.plot(data[0],data[1])
    pt.scatter(x,y)
    pt.title(f'{respuesta}')
    pt.savefig(f'{respuesta}.png')
    return(0)

def regexp(n,x,y,xmin,xmax):
    sumx=0
    sumy=0
    sumyp=0
    sumxyp=0
    sumxsqrd=0

    for i in range(0,len(x)):
        sumx+=x[i]
        sumy+=y[i]
        sumyp=sumyp+mt.log(y[i])
        sumxyp=sumxyp+x[i]*mt.log(y[i])
        sumxsqrd=sumxsqrd+x[i]**2

    b=(n*(sumxyp)-(sumx*sumyp))/(n*(sumxsqrd)-(sumx)**2)
    ap=(sumyp/n)-(b*sumx/n)
    a=mt.e**(ap)

    respuesta=str(f'{a}*e**({b}*x)')

    print(respuesta)
    file=open("resultados.txt","a")
    file.write(f'{respuesta}\n')
    file.close()
    data=generatedata(xmin,xmax,respuesta)
    pt.cla()
    pt.clf()
    pt.rcParams.update({'font.size':6})
    pt.plot(data[0],data[1])
    pt.scatter(x,y)
    pt.title(f'{respuesta}')
    pt.savefig(f'{respuesta}.png')
    return(0)


def reglog(n,x,y,xmin,xmax):
    sumy=0
    sumxp=0
    sumxpy=0
    sumxpsqrd=0

    for i in range(0,len(x)):
        sumy=sumy+y[i]
        sumxp=sumxp+mt.log(x[i])
        sumxpy=sumxpy+(mt.log(x[i])*y[i])
        sumxpsqrd=sumxpsqrd+(mt.log(x[i]))**2
    
    b=float((n*(sumxpy)-((sumxp)*(sumy)))/(n*(sumxpsqrd)-(sumxp**2)))
    a=float((sumy/n)-(b*(sumxp/n)))

    respuesta=str(f'{a}+{b}*ln(x)')
    
    print(respuesta)
    file=open("resultados.txt","a")
    file.write(f'{respuesta}\n')
    file.write("################")
    file.close()
    data=generatedata(xmin,xmax,respuesta)
    pt.clf()
    pt.rcParams.update({'font.size':6})
    pt.plot(data[0],data[1])
    pt.scatter(x,y)
    pt.title(f'{respuesta}')
    pt.savefig(f'{respuesta}.png')
    
    return(0)

def generatedata(xl,xu,fx):
    xi=[]
    yi=[]
    data=[]
    function=getfunc(fx)
    i=xl
    while(i<xu):
        xi.append(i)
        fi=function.evalf(subs={x:i,e:mt.e})
        yi.append(fi)
        i+=1

    data.append(xi)
    data.append(yi)
    return(data)

def getfunc(f):
    global x
    return(sp.sympify(f))

if __name__ == '__main__':
    main()
