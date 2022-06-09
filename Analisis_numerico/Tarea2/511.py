import math
import matplotlib.pyplot as plt


def main():
    
    fakepos()
    return(0)


def fakepos():
    
    xr=1
    xl=2
    xu=5
    i=0
    e=100
    temp=1
    flag=False
    error=[]
    iteraciones=[]

    while (e>=2.5 or flag==True):

        temp=xr
        xr=xu-((xu**(7/2)-80)*(xl-xu))/((xl**(7/2)-80)-(xu**(7/2)-80))
        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1

        if ((xl**(7/2)-80)*(xr**(7/2)-80) < 0):
            xu=xr
        elif((xl**(7/2)-80)*(xr**(7/2)-80) > 0):
            xl=xr
        else:
            flag=True
    
    print(f'Falsa posición: {xr}')
    return(0)



if __name__ == '__main__':
    main()
