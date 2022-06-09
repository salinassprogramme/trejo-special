#coding:utf8

import numpy as np


def main():
    A=[[1,6],[3,10],[7,4]]
    B=[[1,3],[0.5,2]]
    C=[[2,-2],[-3,1]]
    
    print(np.dot(A,B))
    print(np.dot(A,C))
    print(np.dot(B,C))
    print(np.dot(C,B))






if __name__=='__main__':
    main()
