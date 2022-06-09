import math
import matplotlib.pyplot as plt


def main():
    
    x=[]
    y=[]
    i=0
    print(bis())


def bis():

    xr=1
    xl=400
    xu=500
    i=0
    e=100
    temp=1
    flag=False
    error=[]
    iteraciones=[]

    
    while(e>=0.5 or flag!=True):

        temp=xr
        xr=(xu+xl)/2

        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1

        if ((((1/(4*3.141592*8.885e-12))*((2e-5)*xl)/(xl**2+0.9**2)**(3/2))-1)*(((1/(4*3.141592*8.885e-12))*((2e-5)*xr)/(xr**2+0.9**2)**(3/2))-1) < 0):
            xu=xr
        elif ((((1/(4*3.141592*8.885e-12))*((2e-5)*xl)/(xl**2+0.9**2)**(3/2))-1)*(((1/(4*3.141592*8.885e-12))*((2e-5)*xr)/(xr**2+0.9**2)**(3/2))-1) > 0):
            xl=xr
        else:
            flag=True

    return(xr)

if __name__=='__main__':
    main()
