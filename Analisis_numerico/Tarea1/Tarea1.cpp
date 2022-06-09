#include "Tarea1.h"

void Tarea1 :: BinToDec(string & num){
	
	bool check = true;

	for(int i = 0;i < num.length();i++){
		if(!isdigit(num[i])){
			check = false;
		}
	}

	if(!check){
		BinToDecfrac(num);
	}
	else{
		BinToDecint(num);
	}


}

long double Tarea1 :: BinToDecfrac(string & num){
	
	stack <long double> stfrac;
	stack <long double> stint;
	int i = 0;
	long double dec = 0;

	while(isdigit(num[i])){
		stint.push(num[i]);
		i++;	
	}

	i++;

	while(i < num.length()){
		stfrac.push(num[i]);
		i++;
	}

	i = stfrac.size();

	while(!stfrac.empty()){
		dec += getnum(stfrac.top())*pow(2,-1*i);
		i--;
		stfrac.pop();	
	}


	while(!stint.empty()){
		dec += getnum(stint.top())*pow(2,i);
		i++;
		stint.pop();
	}

	cout << dec << endl;
	return 0;

}

long double Tarea1 :: BinToDecint(string & num){
	
	int i;
	stack <long double> stint;
	long double dec = 0;

	for(i = 0;i < num.length();i++){
		stint.push(num[i]);
	}

	for(i = 0;i < stint.size();i++){
		dec += getnum(stint.top())*pow(2,i);
	}

	cout << dec << endl;
	return 0;
}

long double Tarea1 :: Mepsilon(){
	
	long double epsilon = 1;
        long double prevep;

        while(epsilon+1 != 1){
                prevep = epsilon;
                epsilon /= 2;
        }

        cout << "Epsilon: " << prevep << endl;
        return 0;
	
}


long double Tarea1 :: InfSeries(){
	
	int i;
	int j=10000;
	long double s1 = 0;
	long double s2 = 0;

	for(i = 1;i <= 10000;i++){
		s1+=1/(pow(i,4));
		s2+=1/(pow(j,4));
		j--;	
	}

	int realvalue = pow(M_PI,4)/90;

	cout <<  "Resultado 1: " << s1 << endl;
	cout << "Error 1: " << (abs(realvalue-s1)/realvalue)*100 << "%" << endl;
	cout <<  "Resultado 2: " << s2 << endl;
	cout << "Error 2: " << (abs(realvalue-s2)/realvalue)*100 << "%" << endl;

	return 0;
}

long double Tarea1 :: NumDerivative(long double & num){

	long double df=6*num/(pow(1-3*pow(num,2),2));

	cout << df << endl;

	long double Df=((1/(1-3*pow(num+0.0000001,2)))-(1/(1-3*pow(num,2))))/(0.0000001);

	cout << Df << endl;
	return 0;

}

long double Tarea1 :: RAM(){
	
	long double volume = 96000;
	long double memory = volume*64/1048576;

	cout << "Memoria: " << memory << endl;
	return 0;
}

void Tarea1 :: Polinomio(){
	NewtonRaphson();
	/*long double a = 1;
	long double b = 1;
	int c = 0;
	vector <long double> v = {};
	NewtonRaphson(a,b,v,c);
	for(int i = 0; i < v.size(); i++){
		cout << v[i] << endl;
	}*/
}

/*vector <long double> Tarea1 :: NewtonRaphson(long double & prevres, long double & res, vector <long double> & list, int & intentos){
	int grado = 2;
	int i;
	bool found = false;
	if(list.size() == grado || intentos >= grado+1){
		return list;
	}
	else if(abs(prevres-res)<0.00000001){
		for(i = 0;i < list.size();i++){
			if(res == list[i]+0.00000001 || res == list[i]-0.00000001){
				found = true;
				break;
			} 
		}
		if(found){
			intentos++;
			NewtonRaphson(prevres,res,list,intentos);
		}
		else{
			list.push_back(res);
			if(prevres-res < 0){
				prevres = res;
				res += res;
			}
			else if(prevres-res > 0){
				prevres = res;
				res -= res;
			}
			intentos++;
		}

	}	
	
	res = prevres - (pow(prevres,2)-5000.002*prevres+10)/(2*prevres-5000.002);
	prevres = res;

	res = prevres - (pow(prevres,2)-5000.002*prevres+10)/(2*prevres-5000.002);
	NewtonRaphson(prevres,res,list,intentos);

}*/

long double Tarea1 :: NewtonRaphson(){
	long double prevres = 1;
	long double res = 0;
	int intentos = 0;

	while(abs(prevres - res) > 0.001){
		res = prevres - (pow(prevres,2)-5000.002*prevres+10)/(2*prevres-5000.002);
	        prevres = res;

        	res = prevres - (pow(prevres,2)-5000.002*prevres+10)/(2*prevres-5000.002);
	}
	cout << res << endl;


}

long double Tarea1 :: getnum(long double & num){
	if(num == 48){
		return 0;
	}
	else if(num == 49){
		return 1;
	}
}
