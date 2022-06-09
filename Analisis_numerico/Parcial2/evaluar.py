#coding:utf8


import sympy as sp
import math as mt

e=sp.symbols('e')

def main():
    f=str(input('Introduzca su función: '))
    func=sp.sympify(f)
    print(func.evalf(subs={e:mt.e}))

if __name__=='__main__':
    main()
