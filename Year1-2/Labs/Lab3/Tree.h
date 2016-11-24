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
	void PrintSearchRes();
	void Insert(Student);
	void deleteByTask();

private:
	PNode root = NULL;
	
	void Search(PNode);
	void PreorderTreeWalk(PNode);
	void Tree_Insert(PNode &, Student);
	void DeleteNode(PNode &);
	PNode Tree_Min_Parent(PNode);
	bool dell(PNode &);
};