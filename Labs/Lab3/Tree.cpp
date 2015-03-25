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

void Tree::PrintSearchRes(){
	Search(root);
}

void Tree::Search(PNode x){
	if (x != NULL){
		if (x->key.height - DIFF == x->key.weight)
			printf("Name: %s Surname: %s Height: %u Weight: %u Ticket No: %u\n", x->key.name, x->key.surname, x->key.height, x->key.weight, x->key.ticket);
		Search(x->left);
		Search(x->right);
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

PNode Tree::Tree_Min_Parent(PNode x) {
	if (x->left->left == NULL)
		return x;
	else
		return Tree_Min_Parent(x->left);
}

void Tree::DeleteNode(PNode &node) {
	PNode l = NULL, r = NULL;

	if (node == NULL)
		return;

	if (node->left == NULL){
		r = node->right;
		delete node;
		node = r;
	}
	else if (node->right == NULL){
		l = node->left;
		delete node;
		node = l;
	} else {
		r = node->right;
		if (r->left == NULL){
			node->key = r->key;
			node->right = r->right;
			delete r;
		} else {
			PNode minParent = Tree_Min_Parent(r);
			PNode min = minParent->left;
			
			node->key = min->key;
			minParent->left = min->right;
			
			delete min;
		}
	}
}

bool Tree::dell(PNode& node){
	if (node != NULL){
		if (dell(node->left)){
			return true;
		}
		else{
			if (node->key.height - DIFF == node->key.weight){
				DeleteNode(node);
				return true;
			}

			return dell(node->right);
		}
	}
	return false;
}

void Tree::deleteByTask(){
	while (dell(root)){

	}
}