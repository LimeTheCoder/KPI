#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

const int N = 20;

void getMass(int(*arr)[N]);
void showMass(int(*arr)[N]);
int sproduct(int(*arr)[N]);

int main()
{
	int mass[N][N] = { 0 };
	getMass(mass);
	showMass(mass);
	printf("============================================================\n");
	printf("Maximum product of 4 elements in the array: %d\n", sproduct(mass));
	return 0;
}

void getMass(int(*arr)[N]){
	FILE *input = fopen("1.txt", "rt");
	
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++)
			fscanf(input, "%d", &arr[i][j]);
	}

	fclose(input);
}

void showMass(int(*arr)[N]){
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++)
			printf("%3d", arr[i][j]);
		printf("\n");
	}
}

int sproduct(int(*arr)[N]){
	int prod = 0, maxprod = 0;

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++) {                          
			if ((j + 4) < N)
				prod = arr[i][j] * arr[i][j + 1] * arr[i][j + 2] * arr[i][j + 3];
			if (prod > maxprod)
				maxprod = prod;
			if ((i + 4) < N)
				prod = arr[i][j] * arr[i+1][j] * arr[i + 2][j] * arr[i + 3][j];
			if (prod > maxprod)
				maxprod = prod;
			if (((i + 4) < N) && (j + 4) < N)
				prod = arr[i][j] * arr[i + 1][j + 1] * arr[i + 2][j + 2] * arr[i + 3][j + 3];
			if (prod > maxprod)
				maxprod = prod;
			if (((i + 4) < N) && (j - 4) > 0)
				prod = arr[i][j] * arr[i + 1][j - 1] * arr[i + 2][j - 2] * arr[i + 3][j - 3];
			if (prod > maxprod)
				maxprod = prod;
		}
	}
	return maxprod;
}