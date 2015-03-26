#include <stdio.h>

const int MAX_SIZE = 50;

struct Node{
	char data = 0;
	Node *next = NULL;
};

typedef Node* PNode;

class Stack{
public:
	void push(char x);
	char pop();
	bool isEmpty();

private:
	PNode head = NULL;
};

void Stack::push(char x){
	PNode tmp = new Node;
	tmp->data = x;

	if (head == NULL)
		head = tmp;
	else {
		tmp->next = head;
		head = tmp;
	}
}

char Stack::pop(){
	PNode tmp = head;
	char c = 0;

	if (head == NULL){
		printf("Error deleting\n");
		return -1;
	}

	c = head->data;
	head = head->next;

	delete tmp;
	return c;
}

bool Stack::isEmpty(){
	if (head == NULL)
		return true;
	else
		return false;
}

int main(){
	char namefile[MAX_SIZE];
	char c = 0, c2 = 0;
	Stack S;

	printf("Enter name of file:\n");
	gets(namefile);

	FILE *input = fopen(namefile, "rt");

	if (input == NULL){
		printf("Cannot open %s\n", namefile);
		return -1;
	}

	while (fscanf(input, "%c", &c) >= 0){
		if (c == '(' || c == '{' || c == '[')
			S.push(c);

		if (c == ')'){
			if (S.isEmpty()){
				printf("Error! Missing '('\n");
				fclose(input);
				return -1;
			}

			c2 = S.pop();
			if (c2 != '('){
				printf("Error in %c%c\n", c2, c);
				fclose(input);
				return -1;
			}
			c2 = 0;
		}

		if (c == ']'){
			if (S.isEmpty()){
				printf("Error! Missing '['\n");
				fclose(input);
				return -1;
			}

			c2 = S.pop();
			if (c2 != '['){
				printf("Error in %c%c\n", c2, c);
				fclose(input);
				return -1;

			}
			c2 = 0;
		}

		if (c == '}'){
			if (S.isEmpty()){
				printf("Error! Missing '{'\n");
				fclose(input);
				return -1;
			}

			c2 = S.pop();
			if (c2 != '{'){
				printf("Error in %c%c\n", c2, c);
				fclose(input);
				return -1;

			}
			c2 = 0;
		}
	}

	if (S.isEmpty())
		printf("Correct!\n");
	else {
		c2 = S.pop();
		printf("Error!\n", c2);
	}

	fclose(input);
	return 0;
}