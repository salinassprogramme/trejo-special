#coding:utf8

import numpy as np
import sympy as sp

def main():
    
    n=int(input('Introduzca la extensión de la muestra: '))
    x=np.zeros((1,n))

    for i in range(0,n):
        x[0][i]=float(input(f'Introduzca su valor para x{i+1}: '))

    f=np.zeros((n,n))

    for i in range(0,n):
        f[i][0]=float(input(f'Introduzca su valor para y{i+1}: '))

    print(f)


    for i in range(0,n):
        for j in range(0,n):
            if (j>i or j==0):
                pass
            else:
                if (i==j):
                    f[i][j]=(f[i][j-1]-f[i-1][j-1])/(x[0][i]-x[0][0])
                else:
                    f[i][j]=(f[i][j-1]-f[i-1][j-1])/(x[0][i]-x[0][i-1])
    print(f)
    coeficientes=[]

    for i in range(0,n):
        for j in range(0,n):
            if (i==j):  
                coeficientes.append(f[i][j])

    coeficiente0=float(coeficientes[0])
    resultado=f'{coeficiente0}+'
    print(x)
    for i in range(1,n):
        coeficienten=float(coeficientes[i])
        resultado=resultado+f'+{coeficienten}'
        for j in range(0,i):
            xn=float(x[0][j])
            resultado=resultado+f'*(x-{xn})'
    print(resultado)
    print(sp.sympify(resultado))





if __name__=='__main__':
    main()
