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
    
    l=float(input('Introduzca su factor de relajación: '))
    temp1 =np.zeros(uk)
    temp = np.zeros(uk)                        
    resultado=0
    for i in range(0, 25):
        temp1=temp
        temp = seidel(m1, temp,uk)
        temp1=l*temp+(1-l)*temp1
        
    print(temp1)

def seidel(a, tm, uk):

    for j in range(0, uk):        
        d = a[j][uk]                  
          
        for i in range(0, uk):     
            if(j != i):
                d-=a[j][i] * tm[i]
        tm[j] = d / a[j][j]
    return tm    

if __name__=='__main__':
    main()
