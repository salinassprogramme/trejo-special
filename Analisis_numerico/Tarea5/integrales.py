#coding:utf8
import math


def main():
    l1=float(input('Introduzca su límite inferior de integración: '))
    l2=float(input('Introduzca su límite superior de integración: '))
    integral(l1,l2)

def integral(l,u):
    T=3595.15
    n=100000000
    h=6.62607015e-34
    c=299792458
    K=1.380649e-23
    dx=(u-l)/n
    suma=0
    for i in range(0,n):   
        xi=((l+i*dx)+(l+i*dx+1))/2
        suma+=(8*math.pi*h*xi**3)/((math.e**((h*xi/K*T))-1)*c**3)
    print(suma)






if __name__=='__main__':
    main()
