#include <stdio.h>
#include <math.h>

const int LIMIT = 100;

int main(){
	long long int sqr1 = 0, sqr2 = 0, diff = 0;
	int sum = 0;

	for (int i = 1; i <= 100; i++){
		sqr1 += (long long int)pow((double)i, 2);
		sum += i;
	}
	sqr2 = (long long int)pow((double)sum, 2);
	diff = sqr2 - sqr1;
	printf("%lld\n", diff);
	
	return 0;
}