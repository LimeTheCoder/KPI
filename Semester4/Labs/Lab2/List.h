#include "Square.h"

struct Node {
	Square data;
	Node *next = NULL;
};

typedef Node* PNode;

class List {
public:
	List();
	~List();

	void Add(Square);
	bool DeleteByParam(double);
	bool isEmpty();
	Square* Search(double);
	int Size();
	void Show();

private:
	PNode head;
	int size;
};