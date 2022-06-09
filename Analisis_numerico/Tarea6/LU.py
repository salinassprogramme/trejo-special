#coding:utf8
import numpy as np

def main():

    uk=int(input('Introduzca el número de incógnitas: '))
    matriz1=np.zeros((uk,uk+1))
    tempmatrix=np.zeros(uk)

    for i in range(0,uk):
        for j in range(0,uk+1):
            if(j==uk):
                matriz1[i][j]=float(input(f'Introduzca el coeficiente del T.I: '))
            else:
                matriz1[i][j]=float(input(f'Introduzca el coeficiente de x{j}: '))
    LU(matriz1,tempmatrix,uk)
    
def LU(m1,tm,uk):
    i=0
    j=0
    k=0
    
    u=np.zeros((uk,uk+1))
    l=np.zeros((uk,uk+1))
    lelements=[]

    for i in range(uk):
        l[i][i]=1

    for i in range(uk):
        l[i][uk]=m1[i][uk]


    for i in range(uk):
        for j in range(i+1, uk):
            ratio = m1[j][i]/m1[i][i]
            lelements.append(ratio)
            for k in range(uk+1):
                m1[j][k] = m1[j][k]-ratio*m1[i][k]

    for i in range(uk):
        for j in range(uk):
            u[i][j]=m1[i][j]

    k=0
    for j in range(uk):
        for i in range(j+1,uk):
            l[i][j]=lelements[k]
            k+=1
    
    lelements=gauss(l,tm,uk)
    
    for i in range(uk):
        u[i][uk]=lelements[i]
    
    print(gauss(u,tm,uk))
    return(0)

def gauss(m1,tm,uk):
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

    return(tm)

if __name__=='__main__':
    main()
