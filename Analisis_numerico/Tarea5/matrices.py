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
    
    
    l=['Gauss sin pivoteo[G]','Gauss con pivoteo[GP]','Gauss-Jordan[GJ]','Krammer[K]']
    print(l)
    metodo=str(input('Introduzca su método de resolución: '))
    if(metodo=='GP'):
        gausspivote(matriz1,tempmatrix,uk)
    elif(metodo=='G'):
        gauss(matriz1,tempmatrix,uk)
    elif(metodo=='GJ'):
        gaussjordan(matriz1,tempmatrix,uk)
    elif(metodo=='K'):
        krammer(matriz1,tempmatrix,uk)

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
    
    print(tm)
    

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

    print(respuestas)
    return(0)


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

    print(temp2)
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
