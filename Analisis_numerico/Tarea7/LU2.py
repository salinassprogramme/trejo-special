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
    
    u=np.zeros((uk,uk))
    l=np.zeros((uk,uk))
    lelements=[]
    print('A=')
    print(m1)
    for i in range(uk):
        l[i][i]=1

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
    
    temp2=np.zeros((uk,uk))
    for i in range(uk):
        for j in range(uk):
            temp2=[i][j]=m1[i][j]

    print('L=')
    print(l,"")
    print('U=')
    print(u,"")
    print('L*U=')
    print(np.dot(l,u),"")
    print('L^-1=')
    print(np.linalg.inv(l))
    print('U^-1=')
    print(np.linalg.inv(u))
    print('inv(L)*inv(U)=')
    print(np.dot(np.linalg.inv(l),np.linalg.inv(u)))
    print('A^-1=')
    print(np.linalg.inv(temp2))
    return(0)


if __name__=='__main__':
    main()
