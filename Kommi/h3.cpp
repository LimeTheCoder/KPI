#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct Node{
	int data = -1;
	Node *next = NULL;
	Node *prev = NULL;
};

typedef Node* PNode;

void fillRand(PNode &, int &);
void display(PNode);
void swap(PNode &, PNode &);
void bubbleSort(PNode &, int);
void insertionSort(PNode &, int);
void selectionSort(PNode &, int);

int main(){
	srand(time(NULL));
	PNode head = NULL;
	int num = 0;
	fillRand(head, num);
	bubbleSort(head, num);
	display(head);

	return 0;
}

void display(PNode head){
	PNode current = head->next;

	while (current->next){
		printf("%d ", current->data);
		current = current->next;
	}
	printf("\n");
}

void selectionSort(PNode &head, int size) {
	PNode curr = head->next, min = NULL, n = NULL;
	while (curr->next->next != NULL) {
		min = curr;
		n = curr->next;
		while (n->next != NULL) {
			if (n->data < min->data)
				min = n;
			n = n->next;
		}
		if (min != curr){
			swap(curr, min);
			curr = min->next;
		}
		else
		curr = curr->next;
	}
}

void insertionSort(PNode &head, int size){
	PNode n = NULL, p = NULL;
	if (size == 1)
		return;

	n = head->next->next;
	
	while (n->next != NULL){
		p = n->prev;
		while (p->prev != NULL && p->data > p->next->data){
			swap(p, p->next);
			p = p->prev->prev;
		}
		n = n->next;
	}
}

void bubbleSort(PNode &head, int num){
	PNode n = NULL, p = NULL;
	bool swapped = true;
	int j = 0;
	while (swapped) {
		swapped = false;
		j++;
		n = head->next;
		p = head->next->next;
		for (int i = 0; i < num - j; i++) {

			if (n->data > p->data) {
				swap(n, p);
				swapped = true;
			}
			else
				n = n->next;
			p = n->next;
		}
	}
}

void fillRand(PNode &head, int &num){
	PNode current = NULL;
	printf("Enter num of elements:\n");
	scanf("%d", &num);
	
	if (num < 1){
		printf("Incorrect number\n");
		return;
	}

	head = new Node;

	for (int i = 0; i < num; i++){
		current = new Node;
		current->data = rand() % 100;
		current->next = head;
		head->prev = current;
		head = current;
	}
	current = new Node;
	head->prev = current;
	current->next = head;
	head = current;
}

void swap(PNode &first, PNode &second){
	PNode n = NULL, one = first, two = second;

	if (first->next == second || second->next == first){
		if (second->next == first){
			one = second;
			two = first;
		}
		two->next->prev = one;
		one->prev->next = two;
		one->next = two->next;
		two->prev = one->prev;
		one->prev = two;
		two->next = one;
	}
	else {
		two->next->prev = one;
		two->prev->next = one;
		one->prev->next = two;
		one->next->prev = two;
		n = one->next;
		one->next = two->next;
		two->next = n;
		n = one->prev;
		one->prev = two->prev;
		two->prev = n;
	}
}