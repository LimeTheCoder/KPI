#include "List.h"

List::List() {
	head = NULL;
	size = 0;
}

List::~List(){
	Node *tmp = NULL;
	while (head != NULL) {
		tmp = head;
		head = head->next;
		delete tmp;
	}
}

void List::Add(Square s) {
	PNode tmp = new Node;
	tmp->data = s;

	if (isEmpty()){
		head = tmp;
		size++;
		return;
	}
	
	PNode curr = head;
	
	while (curr->next != NULL)
		curr = curr->next;
	curr->next = tmp;
	size++;
}

bool List::isEmpty() {
	if (head == NULL)
		return true;
	else
		return false;
}

bool List::DeleteByParam(double area) {
	PNode curr = NULL, tmp = NULL;
	Square buff;

	if (!isEmpty()) {
		if (head->data.Area() < area){
			tmp = head->next;
			delete head;
			head = tmp;
			size--;
			return true;
		}
		
		curr = head;

		while (curr->next) {
			if (curr->next->data.Area() < area) {
				curr->next = curr->next->next;
				delete curr->next;
				size--;
				return true;
			}
			curr = curr->next;
		}
	}

	return false;
}

Square* List::Search(double per) {
	PNode curr = head;
	Square *tmp = new Square();
	while (curr) {
		if (curr->data.Perim() == per){
			*tmp = curr->data;
			return tmp;
		}
	}
	return NULL;
}

int List::Size() {
	return size;
}

void List::Show() {
	PNode curr = head;
	int i = 0;

	while (curr) {
		printf("Element %d\n", i);
		curr->data.Show();
		curr = curr->next;
		i++;
	}
}