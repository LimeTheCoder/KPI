#include <stdio.h>
#include <math.h>

bool isPrime(int);

int main(){
	long long int num = 600851475143;
	const int LIMIT = sqrt((double)num);
	int max = 1, i = 3;
	
	do{
		if (num % i == 0 && isPrime(i))
			max = i;
		i++;
	} while (i <= LIMIT);

	printf("%d\n", max);
	return 0;
}

bool isPrime(int n) {
	int sqr = 0;
        
        if(n == 1 || n == 2)
           return true;

	if (n % 2 == 0) 
		return false;

	sqr = (int)sqrt((double)n);
	
	for (int i = 3; i <= sqr; i++) {
		if (n % i == 0)
			return false;
	}

	return true;
}