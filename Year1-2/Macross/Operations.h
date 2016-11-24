#include <string>

int StringSum(char *s1, char *s2, char *res, size_t resSize)
{
	strcpy_s(res, resSize, s1);
	strcat_s(res, resSize, s2);
	return 0;
}

template <typename T>
int operation(T a, char o, T b, T &res)
{
	switch (o) {
	case '+':
		res = a + b;
		break;
	case '-':
		res = a - b;
		break;
	case '*':
		res = a * b;
		break;
	case '/':
		res = a / b;
		break;
	}

	return 0;
}