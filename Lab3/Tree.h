#include <stdio.h>
#include "student.h"

struct Node {
	Student key;
	Node *left = NULL, *right = NULL;
};

typedef Node* PNode;

class Tree {
public:
	void show();
	void search();
	void Insert(Student);

private:
	PNode root = NULL;
	void InorderTreeSearch(PNode);
	void PreorderTreeWalk(PNode);
	void Tree_Insert(PNode &, Student);
};