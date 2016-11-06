#include "Tree.h"
#include <string.h>
#include <stdlib.h>
#include <time.h>

void init(Student &);
void input(Student &);
void task3();
void task2();
void task1();

int main(){
	srand(time(NULL));
	
	task2();
	
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

void input(Student &s){
	printf("Enter name, surname, height, weight and ticket:\n");
	scanf("%s %s %u %u %u", &s.name, &s.surname, &s.height, &s.weight, &s.ticket);
	system("cls");
}

void task3() {
	Tree tree;
	Student student;
	int num;

	printf("Enter num of student:\n");
	scanf("%d", &num);
	
	for (int i = 0; i < num; i++){
		input(student);
		tree.Insert(student);
	}

	printf("Before deleting function:\n");
	tree.show();

	tree.deleteByTask();
	
	printf("\nAfter deleting function:\n");
	tree.show();
}

void task2() {
	Tree tree;
	Student student;
	int num;

	printf("Enter num of student:\n");
	scanf("%d", &num);
	for (int i = 0; i < num; i++){
		input(student);
		tree.Insert(student);
	}

	tree.show();
	printf("\nEntities with ideal data:\n");
	tree.PrintSearchRes();
}

void task1(){
	Tree tree;
	Student student;
	int num = 10;

	for (int i = 0; i < num; i++){
		init(student);
		tree.Insert(student);
	}

	tree.show();
}