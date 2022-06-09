#coding:utf8

import matplotlib.pyplot as plt

def main():
    i=0
    x=[]
    y1=[]
    y2=[]
    answer=[]
    answerx=[]
    while(i<500):
        x.append(i)
        y1.append((120+1.1*i)/10)
        y2.append((174+2*i)/17.4)
        ea=abs((y1[i]-y2[i])/y2[i])*100
        if (ea<0.01):
            answer.append(y1[i])
            answerx.append(i)
        else:
            answer.append(0)
            answerx.append(i)
        i+=1

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.scatter(answerx,answer)
    plt.show()

        

if __name__=='__main__':
    main()
