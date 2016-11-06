#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>

struct Node{
	int data = 0;
	Node* next = NULL;
};

typedef Node* PNode;

class Queue{
public:
	void enqueue(int x);
	int dequeue();
	void display();

private:
	PNode head = NULL;
	PNode tail = NULL;
};

void Queue::enqueue(int x){
	PNode n = new Node;
	n->data = x;
	if (head == NULL)
		head = n;
	else if (tail == NULL){
		tail = n;
		head->next = tail;
	}
	else {
		tail->next = n;
		tail = n;
	}
}

int Queue::dequeue(){
	PNode tmp = head;
	int x = 0;
	if (head == NULL){
		printf("Error deleting\n");
		return -1;
	}
	x = head->data;
	head = head->next;
	delete tmp;
	return x;
}

void Queue::display(){
	PNode current = head;
	system("cls");

	while (current){
		printf("%d ", current->data);
		current = current->next;
	}
	printf("\n");
}

int main(){
	srand(time(NULL));
	Queue Q;
	char c = 0;

	while (c != 27){
		if (!kbhit()){
			c = getch();

			if (c == 'A')
				Q.enqueue(rand() % 100);
			
			if (c == 'Z')
				Q.dequeue();

			Q.display();
		}
	}
	return 0;
}