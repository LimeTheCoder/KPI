#include <stdio.h>
#include <regex>
#include "tfsm.h"

void task1();
void task2();
void task3();

int main() {
	task3();

	return 0;
}

void task1() {
	FILE *input = fopen("task1.txt", "rt");

	if (input == NULL)
		return;
	char str[50];
	regex exp("\/{2}[a-z]*[F-K]+");

	while (!feof(input)) {
		fscanf(input, "%s", str);
		if (regex_match(string(str), exp))
			printf("%s\n", str);
	}

	fclose(input);
}

void task2() {
	FSM fsm;
	char str[50];
	printf("Enter string:\n");
	scanf("%s", str);

	if (fsm.scan(string(str)))
		printf("GOOD\n");
	else
		printf("BAD\n");
}

void task3() {
	FILE *input = fopen("task3.txt", "rt");

	if (input == NULL)
		return;
	
	char buff[500];
	regex exp("[; .]");
	TFSM tfsm;

    fgets(buff, 500, input);
	string str(buff);
	
	auto token = sregex_token_iterator(str.begin(), str.end(), exp, -1);
	auto tokensEnd = sregex_token_iterator();
	
	for (; token != tokensEnd; ++token) {
		printf("%s\t", ((string)(*token)).c_str());
		if (tfsm.scan(*token))
			printf("GOOD\n");
		else
			printf("BAD\n");
	}

	fclose(input);
}