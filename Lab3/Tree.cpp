#include "Tree.h"


void Tree::PreorderTreeWalk(PNode x){
	if (x != NULL){
		printf("Name: %s, Surname: %s, Height: %u, Weight: %u, Ticket No: %u\n", x->key.name, x->key.surname, x->key.height, x->key.weight, x->key.ticket);
		PreorderTreeWalk(x->left);
		PreorderTreeWalk(x->right);
	}
}

void Tree::show(){
	PreorderTreeWalk(root);
}

void Tree::search(){
	InorderTreeSearch(root);
}

void Tree::InorderTreeSearch(PNode x){
	if (x != NULL){
		InorderTreeSearch(x->left);
		if (x->key.height - DIFF == x->key.weight)
			printf("Name: %s Surname: %s Height: %ud Weight: %ud Ticket No: %ud\n", x->key.name, x->key.surname, x->key.height, x->key.weight, x->key.ticket);
		InorderTreeSearch(x->right);
	}
}

void Tree::Insert(Student student){
	Tree_Insert(root, student);
}

void Tree::Tree_Insert(PNode &node, Student value){
	if (node == NULL){
		node = new Node;
		node->key = value;
		return;
	}

	if (node->key.ticket > value.ticket)
		Tree_Insert(node->left, value);
	else
		Tree_Insert(node->right, value);
}