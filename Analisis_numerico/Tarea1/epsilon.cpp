#include <iostream>
#include <math.h>

using namespace std;

int main(){

	long double epsilon = 1;
	long double prevep;
	while(epsilon+1 != 1){
		prevep = epsilon;
		epsilon /= 2;
	}

	cout << prevep << endl;
	return 0;
}
