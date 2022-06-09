import math
import matplotlib.pyplot as plt


def main():
    
    x=[]
    y=[]
    i=0
    while(i<=2):
        x.append(i)
        y.append(5-math.sqrt(2*9.81*i)*math.tanh((math.sqrt(2*9.81*i)/2*4)*2.5))
        i+=0.01

    plt.clf()
    plt.cla()
    plt.plot(x,y,label='f(m)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title('Método gráfico 5.15')
    plt.savefig('515graph.png')
    bis()
    fakepos()
    return(0)


def bis():

    xr=1
    xl=0
    xu=2
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

        if ((5-math.sqrt(2*9.81*xl)*math.tanh((math.sqrt(2*9.81*xl)/2*4)*2.5))*(5-math.sqrt(2*9.81*xr)*math.tanh((math.sqrt(2*9.81*xr)/2*4)*2.5)) < 0):
            xu=xr
        elif((5-math.sqrt(2*9.81*xl)*math.tanh((math.sqrt(2*9.81*xl)/2*4)*2.5))*5-math.sqrt(2*9.81*xr)*math.tanh((math.sqrt(2*9.81*xr)/2*4)*2.5) > 0):
            xl=xr
        else:
            flag=True

            flag=True
    plt.clf()
    plt.cla()
    plt.plot(iteraciones,error,label='E_s %')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title('Bisección 5.15')
    plt.savefig('515bis.png')
    print(f'Bisección: {xr}')
    return(0)

def fakepos():

    xr=1
    xl=0
    xu=2
    i=0
    e=100
    temp=1
    flag=False
    error=[]
    iteraciones=[]

    while(e>=0.5 or flag!=True):

        temp=xr
        xr=xu-((5-math.sqrt(2*9.81*xu)*math.tanh((math.sqrt(2*9.81*xu)/2*4)*2.5))*(xl-xu))/((5-math.sqrt(2*9.81*xl)*math.tanh((math.sqrt(2*9.81*xl)/2*4)*2.5))-(5-math.sqrt(2*9.81*xu)*math.tanh((math.sqrt(2*9.81*xu)/2*4)*2.5)))
       
        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1

        if ((5-math.sqrt(2*9.81*xl)*math.tanh((math.sqrt(2*9.81*xl)/2*4)*2.5))*(5-math.sqrt(2*9.81*xr)*math.tanh((math.sqrt(2*9.81*xr)/2*4)*2.5)) < 0):
            xu=xr
        elif((5-math.sqrt(2*9.81*xl)*math.tanh((math.sqrt(2*9.81*xl)/2*4)*2.5))*5-math.sqrt(2*9.81*xr)*math.tanh((math.sqrt(2*9.81*xr)/2*4)*2.5) > 0):
            xl=xr
        else:
            flag=True


    plt.clf()
    plt.cla()
    plt.plot(iteraciones,error,label='E_s %')
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title('Falsa posición 5.15')
    plt.savefig('515fp.png')
    print(f'Falsa posición: {xr}')
                                     


if __name__ == '__main__':
    main()

