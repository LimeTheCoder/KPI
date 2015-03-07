#include <stdio.h>

int main(){
	int num = 2520;
	bool isContinue = false;

	do {
		isContinue = false;
		num += 20;

		for (int i = 0; i < 20; i++){
			if (num % (i + 1) != 0){
				isContinue = true;
				break;
			}
		}
	} while (isContinue);

	printf("%d\n", num);

	return 0;
}