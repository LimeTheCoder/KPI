#include <stdio.h>
#include <windows.h>

int** create(int size);
void freeMass(int** mass, int size);
void initMatr(int**, int);
void display(int**, int);
void addMatrix(int**, int**, int**, int);
void multMatrix(int**, int**, int**, int);
void mainFunc(int**, int);
void connectFunc(int**, int);
void getPath(int &, int &, int** , int);

int main(){
	int size = 0;
	int **adjMatr = NULL;

	printf("Enter size of adjacency matrix:\n");
	scanf("%d", &size);

	adjMatr = create(size);

	initMatr(adjMatr, size);
	mainFunc(adjMatr, size);

	freeMass(adjMatr, size);

	return 0;
}

void initMatr(int** adjMatr, int size){
	printf("Enter adjacency matrix:\n");

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			scanf("%d", &adjMatr[i][j]);
		}
	}
	system("cls");
}

void display(int** mass, int size){
	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++)
				printf("%3d", mass[i][j]);
		printf("\n");
	}
}

void addMatrix(int** matr, int** matr2, int** res, int n){
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++)
			res[i][j] = matr[i][j] + matr2[i][j];
	}
}

void multMatrix(int** matr, int** matr2, int** res, int n){
	int **mass = create(n);

	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			mass[i][j] = 0;
			for (int k = 0; k < n; k++)
				mass[i][j] += matr[i][k] * matr2[k][j];
		}
	}

	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++)
			res[i][j] = mass[i][j];
	}

	freeMass(mass, n);
}

void mainFunc(int** adjMatr, int size){
	int** gradeMatr = create(size);
	int** distMatr = create(size);
	int** buffMatr = create(size);

	int path = 0, cycle = 0;

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (adjMatr[i][j] == 1 && i != j)
				distMatr[i][j] = 1;
			else if (i == j)
				distMatr[i][j] = 0;
			else
				distMatr[i][j] = -1;
		}
	}

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++)
			gradeMatr[i][j] = adjMatr[i][j];
	}

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (i == j)
				buffMatr[i][j] = 1;
			else
				buffMatr[i][j] = 0;
			buffMatr[i][j] += adjMatr[i][j];
		}
	}

	printf("Matrix of grade 1:\n");
	display(adjMatr, size);

	getPath(path, cycle, adjMatr, size);
	printf("There are %d path and %d cycles lenght of 1\n", path, cycle);
	printf("\n\n");

	for (int i = 2; i < size; i++){
		multMatrix(adjMatr, gradeMatr, gradeMatr, size);
		
		printf("Matrix of grade %d:\n", i);
		display(gradeMatr, size);

		getPath(path, cycle, gradeMatr, size);
		printf("There are %d path and %d cycles lenght of %d\n", path, cycle, i);
		printf("\n\n");

		addMatrix(buffMatr, gradeMatr, buffMatr, size);
		
		for (int k = 0; k < size; k++){
			for (int j = 0; j < size; j++){
				if (gradeMatr[k][j] > 0 && distMatr[k][j] == -1)
					distMatr[k][j] = i;
			}
		}
	}

	printf("Distance matrix:\n");
	display(distMatr, size);
	printf("\n");
	
	connectFunc(buffMatr, size);

	freeMass(gradeMatr, size);
	freeMass(distMatr, size);
	freeMass(buffMatr, size);
}

int** create(int size){
	int **mass = new int*[size];

	for (int i = 0; i < size; i++)
		mass[i] = new int[size];
	return mass;
}

void freeMass(int** mass, int size){
	for (int i = 0; i < size; i++)
		delete[]mass[i];

	delete[] mass;
}

void connectFunc(int** buffMass, int size){
	int** connectMatr = create(size);
	int tmp = 0;

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (buffMass[i][j])
				buffMass[i][j] = 1;
			else
				buffMass[i][j] = 0;
		}
	}

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++)
			connectMatr[i][j] = buffMass[i][j];
	}

	for (int i = 0; i < size - 1; i++){
		for (int j = i + 1; j < size; j++){
			tmp = buffMass[i][j];
			buffMass[i][j] = buffMass[j][i];
			buffMass[j][i] = tmp;
		}
	}

	addMatrix(buffMass, connectMatr, buffMass, size);

	printf("Connection matrix:\n");
	display(connectMatr, size);
	printf("\n");

	printf("Quadratic-Diagonal matrix:\n");
	display(buffMass, size);
	printf("\n");

	freeMass(connectMatr, size);
}

void getPath(int &path, int &cycle, int** mass, int size){
	path = 0, cycle = 0;
	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			if (mass[i][j] > 0){
				if (i == j)
					cycle += mass[i][j];
				path += mass[i][j];
			}
		}
	}
}