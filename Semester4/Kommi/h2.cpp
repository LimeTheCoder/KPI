#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <conio.h>

const int size = 30;

struct box{
	int apples = rand() % 100;
	box *next = NULL;
};

class container{
public:
	container();
	~container();
	container *next;
	int qtBoxes;
	box *head, *tail;
};

container::container(){
	next = NULL;
	tail = NULL;
	box *current = NULL;
	qtBoxes = rand() % size + 1;
	head = new box;
	if (qtBoxes != 1){
		tail = new box;
		head->next = tail;
		for (int i = 0; i < qtBoxes - 2; i++){
			current = new box;
			tail->next = current;
			tail = current;
		}
	}
}

container::~container(){
	box *tmp = NULL;
	for (int i = 0; i < qtBoxes; i++){
		tmp = head->next;
		delete head;
		head = tmp;
	}
}

void init(container **, int &, container **);
void write(container *);
void contents(container *);
void contents(box *);
void deleting(container **, int &, container **);
void deleting(box **, int &, box **);
void CntMenu(container **, int);
void boxMenu(box **, int, int);

int main(){
	srand(time(NULL));
	container *cHead = NULL, *cTail = NULL, *cCurrent = NULL;
	int numCnt = 0, choice = 0;
	init(&cHead, numCnt, &cTail);
	write(cHead);
	do{
		system("cls");
		printf("Main menu:\n");
		printf("1. Show contents of all containers\n");
		printf("2. Open container\n");
		printf("3. Add container\n");
		printf("4. Delete container\n");
		printf("5. Save\n");
		printf("6. Exit\n");
		scanf("%d", &choice);
		system("cls");
		switch (choice){
		case 1:
			contents(cHead);
			printf("Press any key for return to main menu...\n");
			getch();
			break;
		case 2:
			CntMenu(&cHead, numCnt);
			break;
		case 3:
			if (cHead == NULL)
				cHead = new container;
			else if (cTail == NULL){
				cTail = new container;
				cHead->next = cTail;
			}
			else{
				cCurrent = new container;
				cTail->next = cCurrent;
				cTail = cCurrent;
			}
			numCnt++;
			printf("Container #%d successfully added\n", numCnt);
			printf("Press any key for return to main menu...\n");
			getch();
			break;
		case 4:
			deleting(&cHead, numCnt, &cTail);
			printf("Press any key for return to main menu...\n");
			getch();
			break;
		case 5:
			write(cHead);
			printf("Saving is successful\n");
			printf("Press any key for return to main menu...\n");
			getch();
			break;
		}
	} while (choice != 6);

	return 0;
}

void init(container **cHead, int &numCnt, container **cTail){
	container *cCurrent = NULL;
	numCnt = rand() % size + 1;
	(*cHead) = new container;
	if (numCnt != 1){
		(*cTail) = new container;
		(*cHead)->next = (*cTail);
		for (int i = 0; i < numCnt - 2; i++){
			cCurrent = new container;
			(*cTail)->next = cCurrent;
			(*cTail) = cCurrent;
		}
	}
}

void write(container *cHead){
	container *n = cHead;
	FILE *f = fopen("out.csv", "wt");
	while (n){
		box *tmp = n->head;
		while (tmp->next){
			fprintf(f, "%d;", tmp->apples);
			tmp = tmp->next;
		}
		fprintf(f, "%d\n", tmp->apples);
		n = n->next;
	}
	fclose(f);
}

void contents(container *cHead){
	container *n = cHead;
	int i = 1;
	while (n){
		printf("Container #%d consist %d boxes\n", i, n->qtBoxes);
		n = n->next;
		i++;
	}
}

void contents(box *bHead){
	box *b = bHead;
	int i = 1;
	while (b){
		printf("Box #%d consist %d apples\n", i, b->apples);
		b = b->next;
		i++;
	}
}

void deleting(container **cHead, int &numCnt, container **cTail){
	int choice;
	container *tmp = NULL, *n = NULL;
	printf("Enter number of container for deleting. Total amount of containers: %d\n", numCnt);
	scanf("%d", &choice);
	if (choice > numCnt || choice < 1){
		printf("Incorrect number. Error deleting.\n");
		return;
	}
	else if (choice == 1){
		n = (*cHead)->next;
		delete (*cHead);
		(*cHead) = n;
		if (choice == numCnt)
			(*cTail) = NULL;
	}
	else {
		tmp = (*cHead);
		for (int i = 0; i < choice - 1; i++){
			n = tmp;
			tmp = tmp->next;
		}
		n->next = tmp->next;
		delete tmp;
		if (choice == numCnt)
			(*cTail) = n;
	}
	printf("Container #%d successfully deleted\n", choice);
	numCnt--;
}

void deleting(box **bHead, int &num, box **bTail){
	int choice;
	box *tmp = NULL, *n = NULL;
	printf("Enter number of box for deleting. Total amount of boxes: %d\n", num);
	scanf("%d", &choice);
	if (choice > num || choice < 1){
		printf("Incorrect number. Error deleting.\n");
		return;
	}
	else if (choice == 1){
		n = (*bHead)->next;
		delete (*bHead);
		(*bHead) = n;
		if (choice == num)
			(*bTail) = NULL;
	}
	else {
		tmp = (*bHead);
		for (int i = 0; i < choice - 1; i++){
			n = tmp;
			tmp = tmp->next;
		}
		n->next = tmp->next;
		delete tmp;
		if (choice == num)
			(*bTail) = n;
	}
	printf("Box #%d successfully deleted\n", choice);
	num--;
}
void CntMenu(container **cHead, int numCnt){
	int choice, number;
	container *n = NULL;
	printf("Enter number of container for opening. Total amount of containers: %d\n", numCnt);
	scanf("%d", &number);
	if (number > numCnt || number < 1){
		printf("Incorrect number. Error opening\n.");
		return;
	}
	n = (*cHead);
	for (int i = 0; i < number - 1; i++){
		n = n->next;
	}
	printf("Container #%d opened succesfull\n", number);
	printf("Press any key to continue\n");
	getch();

	box *bHead = n->head, *bTail = n->tail, *bCurrent = NULL;
	do{
		system("cls");
		printf("Container #%d menu:\n", number);
		printf("1. Show contents of all boxes\n");
		printf("2. Open box\n");
		printf("3. Add box\n");
		printf("4. Delete box\n");
		printf("5. Back to main menu\n");
		scanf("%d", &choice);
		system("cls");
		switch (choice){
		case 1:
			contents(bHead);
			printf("Press any key for return to main menu...\n");
			getch();
			break;
		case 2:
			boxMenu(&bHead, n->qtBoxes, number);
			break;
		case 3:
			if (bHead == NULL)
				bHead = new box;
			else if (bTail == NULL){
				bTail = new box;
				bHead->next = bTail;
			}
			else{
				bCurrent = new box;
				bTail->next = bCurrent;
				bTail = bCurrent;
			}
			n->qtBoxes++;
			printf("Box #%d successfully added\n", n->qtBoxes);
			printf("Press any key for return to container menu...\n");
			getch();
			break;
		case 4:
			deleting(&bHead, n->qtBoxes, &bTail);
			printf("Press any key for return to container menu...\n");
			getch();
			break;
		}
	} while (choice != 5);
}

void boxMenu(box **bHead, int numBoxes, int noCnt){
	int choice, number, qt;
	box *b = NULL;
	printf("Enter number of box for opening. Total amount of boxes: %d\n", numBoxes);
	scanf("%d", &number);
	if (number > numBoxes || number < 1){
		printf("Incorrect number. Error opening\n.");
		return;
	}
	b = (*bHead);
	for (int i = 0; i < number - 1; i++){
		b = b->next;
	}
	printf("Box #%d opened succesfull\n", number);
	printf("Press any key to continue\n");
	getch();

	do{
		system("cls");
		printf("Container #%d, Box #%d menu:\n", noCnt, number);
		printf("In this box %d apples\n", b->apples);
		printf("1. Add apples\n");
		printf("2. Delete apples\n");
		printf("3. Back to container menu\n");
		scanf("%d", &choice);
		system("cls");
		switch (choice){
		case 1:
			printf("Enter quantity of apples for adding\n");
			scanf("%d", &qt);
			system("cls");
			b->apples += qt;
			printf("Apples successfully added\n");
			printf("Press any key for return to box menu...\n");
			getch();
			break;
		case 2:
			printf("Enter quantity of apples for deleting\n");
			scanf("%d", &qt);
			system("cls");
			if (qt > b->apples)
				printf("Enough apples\n");
			else {
				b->apples -= qt;
				printf("Apples successfully deleted\n");
			}
			printf("Press any key for return to box menu...\n");
			getch();
			break;
		}
	} while (choice != 3);
}