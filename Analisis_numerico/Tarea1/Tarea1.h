#ifndef	TAREA1_H 
#define TAREA1_H


#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string>
#include <queue>
#include <stack>

using namespace std;

class Tarea1{
	public:
		static void BinToDec(string & num);
		static long double NumDerivative(long double & num);
		static long double Mepsilon();
		static long double InfSeries();
		static long double RAM();
		static void Polinomio();
	private:
		static long double BinToDecfrac(string & num);
		static long double getnum(long double & num);
		static long double BinToDecint(string & num);
		//static vector <long double> NewtonRaphson(long double & prevres, long double & res, vector <long double> & list, int & intentos);
		static long double NewtonRaphson();
};

#endif
