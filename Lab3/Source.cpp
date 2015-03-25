#include "Tree.h"
#include <string.h>
#include <stdlib.h>
#include <time.h>

void init(Student &);

int main(){
	//srand(time(NULL));
	Tree tree;
	Student student;

	for (int i = 0; i < 10; i++){
		init(student);
		tree.Insert(student);
	}

	tree.show();
	
	return 0;
}

void init(Student &student){
	int num = rand() % MAX_CNT;

	student.height = rand() % HEIGHT_RANGE + HEIGHT_BOUND;
	student.weight = rand() % WEIGHT_RANGE + WEIGHT_BOUND;
	
	strcpy(student.name, name[num]);
	num = rand() % MAX_CNT;

	strcpy(student.surname, surname[num]);

	student.ticket = rand() % (INT_MAX - 1) + 1;
}