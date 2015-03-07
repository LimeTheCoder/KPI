#include <stdio.h>

const int degree = 1000;
const int NumOfDigits = 400;

int main(){
	char mass[400];
	char tmp = 0;
	int sum = 0;

	mass[0] = '1';
	for (int i = 1; i < NumOfDigits; i++)
		mass[i] = '0';

	for (int j = 0; j < degree; j++){
		for (int i = 0; i < NumOfDigits; i++){
			mass[i] = (mass[i] - '0') * 2 + tmp;
			
			if (mass[i] > 9){
				mass[i] -= 10;
				tmp = 1;
			}
			else
				tmp = 0;
			
			mass[i] += 48;
		}
	}
	for (int i = 0; i < NumOfDigits; i++)
		sum += mass[i] - '0';

	printf("%d\n", sum);
	return 0;
}