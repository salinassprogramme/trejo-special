#include "Tarea1.h"


int main(){

	cout << "" << endl;
	cout << "Problema 3.1" << endl;

	string a = "101101";
	Tarea1 :: BinToDec(a);
	a = "110.011";
	Tarea1 :: BinToDec(a);
       	a ="0.01101";	
	Tarea1 :: BinToDec(a);
	
	cout << "" << endl;
	cout << "Problema 3.3" << endl;
	Tarea1 :: Mepsilon();

	cout << "" << endl;
	cout << "Problema 3.5" << endl;
	Tarea1 :: InfSeries();	

	cout << "" << endl;
	cout << "Problema 3.7" << endl;
	long double b = 0.577;
	Tarea1 :: NumDerivative(b);
	
	cout << "" << endl;
	cout << "Problema 3.9" << endl;
	Tarea1 :: RAM();

	cout << "" << endl;
	cout << "Problema 3.11" << endl;
	Tarea1 :: Polinomio();
	
	return 0;

}
