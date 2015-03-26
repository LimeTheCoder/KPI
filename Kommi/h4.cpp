#include <stdio.h>
#include <string>

using namespace std;

const int MAX_LEN = 50;

struct Node{
	char str[50];
	int count = -1;
	Node* next = NULL;
	Node* prev = NULL;
};

typedef Node* PNode;

void swap(PNode &first, PNode &second);

class List{
public:
	List();
	~List();

	void AddNode(char*);
	void Display();
	int Search(char*);
	void insertionSort();

private:
	PNode head;
	int entity;
};

List::List(){
	PNode curr = new Node;

	entity = 0;
	head = new Node;
	head->next = curr;
	curr->prev = head;
}

List::~List(){
	PNode curr = NULL;

	while (head){
		curr = head;
		head = head->next;
		delete curr;
	}
}

int List::Search(char word[]){
	PNode curr = head->next;

	while (curr->next){
		if (!strcmp(curr->str, word)){
			curr->count++;
			return curr->count;
		}
		curr = curr->next;
	}

	return 0;
}

void List::AddNode(char word[]){
	PNode tmp = NULL;
	
	if (!Search(word)){
		tmp = new Node;
		tmp->count = 1;
		strcpy(tmp->str, word);
		
		tmp->prev = head;
		tmp->next = head->next;
		head->next->prev = tmp;
		head->next = tmp;
	}
	
	entity++;
}

void List::Display(){
	PNode current = head->next;
	double prob;
	int i = 0;
	while (current->next && i < 100){
		prob = (double)current->count / (double)entity;
		printf("%s %0.6f\n", current->str, prob);
		current = current->next;
		i++;
	}
}


void List::insertionSort(){
	PNode n = NULL, p = NULL;
	if (entity == 1)
		return;

	n = head->next->next;

	while (n->next != NULL){
		p = n->prev;
		while (p->prev != NULL && p->count < p->next->count){
			swap(p, p->next);
			p = p->prev->prev;
		}
		n = n->next;
	}
}

int main(){
	List L;
	char c;
	char word[MAX_LEN];
	int cnt = 0;
	FILE* input = fopen("in.txt", "rt");
	if (input == NULL)
		return -1;
	while (fscanf(input, "%c", &c) > 0){
		if (c != ' ' && c != 13 && c != ',' && c != '.' && c != ';' && c != '\n'){
			word[cnt] = c;
			cnt++;
		}
		else{
			if (cnt != 0){
				word[cnt] = '\0';
				L.AddNode(word);
			}
			cnt = 0;
		}
	}

	L.insertionSort();
	L.Display();

	fclose(input);
	return 0;
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