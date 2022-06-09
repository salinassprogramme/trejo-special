#coding:utf8
import numpy as np


def main():
    matriz1=[[-4,1,0,1,0,0,0,0,0,0],[1,-4,1,0,1,0,0,0,0,0],[0,1,-4,0,0,1,0,0,0,100],[1,0,0,-4,1,0,1,0,0,0],[0,1,0,1,-4,1,0,1,0,0],[0,0,1,0,1,-4,0,0,1,100],[0,0,0,1,0,0,-4,1,0,200],[0,0,0,0,1,0,1,-4,1,200],[0,0,0,0,0,1,0,1,-4,300]]
    tempmatrix=[0,0,0,0,0,0,0,0,0]
    uk=9
    
    a=gaussjordan(matriz1,tempmatrix,uk)
    b=krammer(matriz1,tempmatrix,uk)
    
    e=[]
    for i in range(len(a)):
        ea=float((abs((a[i]-b[i])/a[i])))*100
        e.append(ea)
    print('Error relativo aproximado: \n')
    print(e)

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

    print(tm)
    return(0)

def gaussjordan(m1,tm,uk):
    i=0
    j=0
    k=0

    for i in range(uk):
        for j in range(uk):
            if i!=j:
                ratio = m1[j][i]/m1[i][i]
                for k in range(uk+1):
                    m1[j][k] = m1[j][k]-ratio*m1[i][k]

    for i in range(uk):
        tm[i]=m1[i][uk]/m1[i][i]
    
    print('Respuestas GJ: \n')
    print(tm)
    return(tm)

def gausspivote(m1,tm,uk):
    i=0
    j=0
    k=0

    for i in range(uk):
        for j in range(i+1, uk):
            
            if(m1[i][i]==0):
                m1 = pivoteo(m1,uk,i)

            ratio = m1[j][i]/m1[i][i]
            for k in range(uk+1):
                m1[j][k] = m1[j][k]-ratio*m1[i][k]

    tm[uk-1] = m1[uk-1][uk]/m1[uk-1][uk-1]

    for i in range(uk-2,-1,-1):
        tm[i] = m1[i][uk]
        for j in range(i+1,uk):
            tm[i] = tm[i] - m1[i][j]*tm[j]

        tm[i] = tm[i]/m1[i][i]    

    print(tm)
    return(0)

def krammer(m1,tm,uk):
    
    dets=[]
    respuestas=[]

    for k in range(uk+1):
        m2=changecols(m1,uk,k)
        dets.append(np.linalg.det(m2))

    for k in range(uk):
        respuestas.append(dets[k]/dets[uk])

    print('Respuestas determinantes: \n')
    print(respuestas)
    return(respuestas)


def changecols(m,uk,col):
    temp1=np.zeros((uk,uk+1))
    temp2=np.zeros((uk,uk))

    i=0
    index=uk

    while(i!=col):
        i+=1

    if(i!=uk):
        for j in range(uk):
            temp1[j][col]=m[j][index]
            temp1[j][index]=m[j][col]

        for i in range(uk):
            for j in range(uk+1):
                if (j!=col and j!=index):
                    temp1[i][j]=m[i][j]
                    temp1[i][j]=m[i][j]
    
    else:
        temp1=m.copy()
    for i in range(uk):
        for j in range(uk):
            temp2[i][j]=temp1[i][j]

    return(temp2)


def pivoteo(m,uk,row):
    temp=np.zeros((uk,uk+1))

    if(row==uk):
        index=row-1
    else:
        index=row+1

    for j in range(uk+1):   
        temp[row][j]=m[index][j]
        temp[index][j]=m[row][j]

    for i in range(uk):
        if (i!=row and i!=index):
            for j in range(uk+1):
                temp[i][j]=m[i][j]
                temp[i][j]=m[i][j]

    return (temp)

if __name__=='__main__':
    main()
