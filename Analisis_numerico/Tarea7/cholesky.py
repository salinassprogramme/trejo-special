#coding:utf8

import numpy as np

def main():
    uk=int(input('Introduzca el número de incógnitas :'))
    m1=np.zeros((uk,uk+1))
    for i in range(uk):
        for j in range(uk+1):
            if(j==uk):
                m1[i][j]=float(input(f'Introduzca el coeficiente de T.I.: '))
            else:
                m1[i][j]=float(input(f'Introduzca el coeficiente de x{j}: '))
                
    Cholesky(m1,uk)

def Cholesky(m,uk):
    lower=np.zeros((uk,uk+1))
    lowerT=np.zeros((uk,uk+1))
    temp=np.zeros((uk,1))
    for i in range(uk):
        lower[i][uk]=m[i][uk]
        for j in range(uk):
            a=0
            if(i==j):
                for k in range(j):
                    a+=lower[j][k]**2
                lower[j][j]=(m[j][j]-a)**(1/2)
            else:
                for k in range(j):
                    a+=lower[i][k]*lower[j][k]
                if (lower[j][j]>0):
                    lower[i][j]=(m[i][j]-a)/lower[j][j]
    
    for i in range(uk):
        for j in range(uk):
            lowerT[i][j]=lower[j][i]
    
    print(lower)
    temp=Gauss(lower,temp,uk)
    for j in range(uk):
        lowerT[j][uk]=temp[j]
    
    print(lowerT)
    temp=Gauss(lowerT,temp,uk)
    print(temp)

def Gauss(m1,tm,uk):
    i=0
    j=0
    k=0

    for i in range(uk):
        for j in range(i+1, uk):
            ratio = m1[j][i]/m1[i][i]
            for k in range(uk+1):
                m1[j][k] = m1[j][k]-ratio*m1[i][k]

    tm[uk-1] = m1[uk-1][uk]/m1[uk-1][uk-1]

    for i in range(uk-2,-1,-1):
        tm[i] = m1[i][uk]
        for j in range(i+1,uk):
            tm[i] = tm[i] - m1[i][j]*tm[j]
        tm[i] = tm[i]/m1[i][i]

    return (tm)


if __name__=='__main__':
    main()
