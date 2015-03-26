#include <stdio.h>
#include <windows.h>

const int MAX_SIZE = 50;

struct Node{
	char word[MAX_SIZE];
	Node *next = NULL;
};

int main(){
	Node *head = NULL, *current = NULL, *n = NULL;
	
	FILE *input = fopen("i.txt", "rt");
	if (input == NULL)
		return -1;

	FILE *output = fopen("o.txt", "w");

	head = new Node;
	fscanf(input, "%s", head->word);

	while (!feof(input)){
		current = new Node;
		if (fscanf(input, "%s", current->word) <= 0)
			break;
		current->next = head;
		head = current;
	}

	system("cls");
	n = head;
	while (n){
		fprintf(output, "%s ", n->word);
		n = n->next;
	}

	fclose(input);
	fclose(output);

	return 0;
}