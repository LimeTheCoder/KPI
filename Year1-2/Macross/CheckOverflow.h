#include <math.h>

int stringOverflow(char* a, char *b)
{
	if (!a || !b)
		return -1;
	return 0;
}

template <typename T>
int CharIntOverflow(T a, char o, T b)
{
	T result = 0;
	int status;
	switch (o) {
	case '+':
		result = a + b;
		status = (a > 0 && b > 0 && result < 0) || (a < 0 && b < 0 && result >= 0);
		break;
	case '-':
		result = a - b;
		// @todo: correct overflow check
		status = (a > 0 && b < 0 && result <= 0)	|| (a < 0 && b > 0 && result > 0);
		break;
	case '*':
		result = a * b;
		status = (a != 0 && result / a != b);
		break;
	case '/':
		status = !b;
		break;
	}

	return status;
}

int FloatOverflow(float a, char o, float b){
	float res = 0;

	if (o == '+' || o == '-'){
		if (o == '+')
			res = a + b;
		else
			res = a - b;

		if (res == INFINITY)
			return -1;
	}
	else if (o == '*') {
		res = a * b;
		if (b != 0 && res / b != a)
			return -1;
	}

	return 0;
}