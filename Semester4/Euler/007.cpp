#include <stdio.h>
#include <math.h>

const int LIMIT = 10001;

bool isPrime(int n);

int main(){
	int cnt = 0;
	int i = 0;
	while (cnt <= LIMIT){
		i++;
		if (isPrime(i))
			cnt++;
	}
	printf("%d\n", i);
	return 0;
}

bool isPrime(int n) {
	int sqr = 0;
        
        if(n == 2)
                return true;
	
        if (n % 2 == 0 || n == 1)
		return false;

	sqr = (int)sqrt((double)n);

	for (int i = 3; i <= sqr; i++) {
		if (n % i == 0)
			return false;
	}

	return true;
}