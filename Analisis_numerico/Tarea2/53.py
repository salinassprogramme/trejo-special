import math
import matplotlib.pyplot as plt

def main():
    
    x=[]
    y=[]
    i=0
    while(i<1):
        x.append(i)
        y.append(0.7*i**5-8*i**4+44*i**3-90*i**2+82*i-25)
        i+=0.01

    plt.plot(x,y,label='f(x)=0.7x^5-8x^4+44x^3-90x^2+82x-25')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title('Método gráfico 5.3')
    plt.savefig('53graph.png')

    bis()
    fakepos()
    return(0)

def bis():
    
    xr=1
    xl=0.5
    xu=1
    e=100
    i=0
    temp=1
    flag=False
    error=[]
    iteraciones=[]


    while(e>=10 and flag!=True):

        temp=xr
        xr=(xu+xl)/2

        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1
        if ((0.7*xl**5-8*xl**4+44*xl**3-90*xl**2+82*xl-25)*(0.7*xr**5-8*xr**4+44*xr**3-90*xr**2+82*xr-25) < 0):
            xu=xr
        elif((0.7*xl**5-8*xl**4+44*xl**3-90*xl**2+82*xl-25)*(0.7*xr**5-8*xr**4+44*xr**3-90*xr**2+82*xr-25) > 0):
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
    plt.title('Bisección 5.3')
    plt.savefig('53bis.png')

    print(f'Bisección: {xr}')
    return(0)

def fakepos():
    
    xr=1
    xl=0.5
    xu=1
    i=0
    e=100
    temp=1
    flag=False
    error=[]
    iteraciones=[]

    while(e>=10 and flag!=True):

        temp=xr
        xr=xu-((0.7*xu**5-8*xu**4+44*xu**3-90*xu**2+82*xu-25)*(xl-xu))/((0.7*xl**5-8*xl**4+44*xl**3-90*xl**2+82*xl-25)-(0.7*xu**5-8*xu**4+44*xu**3-90*xu**2+82*xu-25))

        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1

        if ((0.7*xl**5-8*xl**4+44*xl**3-90*xl**2+82*xl-25)*(0.7*xr**5-8*xr**4+44*xr**3-90*xr**2+82*xr-25) < 0):
            xu=xr
        elif((0.7*xl**5-8*xl**4+44*xl**3-90*xl**2+82*xl-25)*(0.7*xr**5-8*xr**4+44*xr**3-90*xr**2+82*xr-25) > 0):
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
    plt.title('Falsa posición 5.3')
    plt.savefig('53fp.png')

    print(f'Posición falsa: {xr}')
    return(0)



if __name__ == '__main__':
    main()
