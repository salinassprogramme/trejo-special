#coding:utf8

def main():
    x=[-2,0,4,6,8,10]
    y=[35,5,-10,2,5,3,20]
    n=len(x)

    sum1=0

    for i in range(1,n):
        sum1+=y[i]
    
    c=(y[len(x)-1]+y[0])/2
    resultado=((x[len(x)-1]-x[0])/n)*(c+sum1)
    print(f'Trapecio compuesto={resultado}')

if __name__=='__main__':
    main()
