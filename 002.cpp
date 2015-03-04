#include <stdio.h>

const int LIMIT = 4000000;

int fib(int);

int main(){
	int sum = 0, num = 0, i = 1;

	while (num < LIMIT){
		num = fib(i);
		if (num % 2 == 0)
			sum += num;
		i++;
	}

	printf("%d\n", sum);

	return 0;
}

int fib(int n){
	if (n == 1 || n == 2)
		return 1;
	else
		return fib(n - 1) + fib(n - 2);
}
