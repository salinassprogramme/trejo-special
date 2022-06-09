import math
import matplotlib.pyplot as plt



def main():
    fakepos()
    return(0)

def fakepos():

    xr=1
    xl=40
    xu=80
    e=100
    i=0
    temp=1
    flag=False
    error=[]
    iteraciones=[]
    
    while(e>=0.001 or flag!=True):
       
        temp=xr
        xr=xu-((36-((9.81*xu)/15)*(1-math.e**-(150/xu)))*(xl-xu))/((36-((9.81*xl)/15)*(1-math.e**-(150/xl)))-(36-((9.81*xu)/15)*(1-math.e**-(150/xu))))
        
        e=abs((xr-temp)/(temp))*100
        error.append(e)
        iteraciones.append(i)
        i+=1
        print(e)

        if (((36-((9.81*xl)/15)*(1-math.e**-(150/xl)))*(36-((9.81*xr)/15)*(1-math.e**-(150/xu)))) < 0):
            xu=xr
        elif(((36-((9.81*xl)/15)*(1-math.e**-(150/xl)))*(36-((9.81*xr)/15)*(1-math.e**-(150/xr)))) > 0):
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
    plt.title('Falsa posición 5.13')
    plt.savefig('513fp.png')
    print(f'Falsa posición: {xr}')




if __name__ == '__main__':
    main()
