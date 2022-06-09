import math




def main():
    #funcion
    #NR(funcion,ed,x0)
    NR(0.01,1)

def NR(ed,x0):
    
    xr=x0
    temp=0
    flag=False
    solutions=0
    ea=100
    preliminares=[]
    resultados=[]
    while(len(resultados)!= numpy.polynomyal.polynomyal.Polynomyal.degree(ecuacion)):
        while(ea>ed and flag!=True):
            temp=xr
            xr=f_NR.evalf(subs={x:temp})
            ea=abs((xr-temp)/xr)
        if(xr in preliminares and xr not in resultados):
            resultados.append(xr)
        else:
            preliminares.append(xr)
        ea=100
        if(xr-temp<0):
            xr=-100*xr
        elif(xr-temp>0):
            xr=-100*xr
    
    print(resultados)

if __name__ == '__main__':
    main()
