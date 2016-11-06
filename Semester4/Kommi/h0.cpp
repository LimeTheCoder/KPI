#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

struct Node{
	int data = 0;
	Node *next = NULL;
};

typedef Node* PNode;

void display(PNode, PNode);
void hideCursor();
void mainFunc();

int main(){
	srand(time(NULL));
	hideCursor();
	mainFunc();

	return 0;
}

void mainFunc(){
	PNode head = NULL, current = NULL, tail = NULL, n = NULL;
	int num = 0;
	head = new Node;
	head->data = rand() % 101;
	SetConsoleTextAttribute(hConsole, (WORD)((0 << 4) | 4));
	printf("%d ", head->data);

	if (getchar() != '\n')
		return;

	tail = new Node;
	while (num < head->data){
		num = rand() % 101;
	}
	tail->data = num;
	head->next = tail;
	
	system("cls");
	SetConsoleTextAttribute(hConsole, (WORD)((0 << 4) | 7));
	printf("%d ", head->data);
	SetConsoleTextAttribute(hConsole, (WORD)((0 << 4) | 4));
	printf("%d ", tail->data);

	while (getchar() == '\n'){
		current = new Node;
		current->data = rand() % 101;

		if (current->data < head->data){
			current->next = head;
			head = current;
			display(head, head);
		}
		else if (current->data > tail->data){
			tail->next = current;
			tail = current;
			display(head, tail);
		}
		else{
			n = head;
			while (n->next->data < current->data){
				n = n->next;
			}
			current->next = n->next;
			n->next = current;
			display(head, n->next);
		}
	}
}

void display(PNode head, PNode keyNode){
	system("cls");
	PNode n = head;
	while (n){
		if (n == keyNode)
			SetConsoleTextAttribute(hConsole, (WORD)((0 << 4) | 4));
		else
			SetConsoleTextAttribute(hConsole, (WORD)((0 << 4) | 7));
		printf("%d ", n->data);
		n = n->next;
	}
	printf("\n");
}

void hideCursor(){
	CONSOLE_CURSOR_INFO info;
	info.dwSize = 100;
	info.bVisible = false;
	SetConsoleCursorInfo(hConsole, &info);
}