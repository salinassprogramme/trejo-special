import math
import matplotlib.pyplot as plt



def main():
    fakepos()
    return(0)


def fakepos():
    
    xr=1
    xl=0
    xu=2
    e=100
    temp=1
    flag=False
    i=0
    error=[]
    iteraciones=[]
    #30-(math.pi*x**2)*(3*3-x)/3

    while(i<3):

        temp=xr
        xr=xu-((30-(math.pi*xu**2)*(3*3-xu)/3)*(xl-xu))/((30-(math.pi*xl**2)*(3*3-xl)/3)-(30-(math.pi*xu**2)*(3*3-xu)/3))

        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)

        if ((30-(math.pi*xl**2)*(3*3-xl)/3)*(30-(math.pi*xr**2)*(3*3-xr)/3) < 0):
            xu=xr
        elif((30-(math.pi*xl**2)*(3*3-xl)/3)*(30-(math.pi*xr**2)*(3*3-xr)/3) > 0):
            xl=xr
        else:
            flag=True
        i+=1

    
    plt.clf()
    plt.cla()
    plt.plot(iteraciones,error,label='E_s %')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title('Falsa posición 5.17')
    plt.savefig('517fp.png')
    print(f'Falsa posición: {xr}')




if __name__ == '__main__':
    main()
