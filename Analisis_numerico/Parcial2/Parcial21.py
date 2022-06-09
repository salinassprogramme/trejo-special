#coding:utf8

import numpy as np
import math as mt

def main():
    
    d=500
    alfa=[54.8,54.06,53.34]
    beta=[65.59,64.59,63.62]
    arad=[]
    brad=[]
    n=len(alfa)
    x=[]
    y=[]


    for i in range(2):
        for j in range(n):
            if i==0:
                arad.append(degtorad(alfa[j]))
            else:
                brad.append(degtorad(beta[j]))
    
    for i in range(0,n):
        x.append(xcoordinate(d,arad[i],brad[i]))
        y.append(ycoordinate(d,arad[i],brad[i]))
    
    print(x)
    print(y)

    
def xcoordinate(d,a,b):
    return(d*((mt.tan(b))/(mt.tan(b)-mt.tan(a))))

def ycoordinate(d,a,b):
    return(d*((mt.tan(b)*mt.tan(a))/(mt.tan(b)-mt.tan(a))))

def degtorad(ang):
    return(ang*mt.pi/180)

if __name__=='__main__':
    main()
