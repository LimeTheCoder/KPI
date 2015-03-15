#include <stdio.h>
#include <limits.h>
#include <float.h>
#include "Operations.h"
#include "CheckOverflow.h"

#define CharIntCalculate(a, o, b)\
{\
	 int res = 0; \
     if (CharIntOverflow(a, o, b))\
	     printf("Error overflow\n");\
	 else {\
	     operation(a, o, b, res); \
	     printf("%d\n", res); \
	 }\
}

#define FloatCalculate(a, o, b)\
{\
	float res = 0; \
    if (FloatOverflow(a, o, b))\
	    printf("Error!\n"); \
	else {\
	    operation(a, o, b, res); \
	    printf("%f\n", res); \
	 }\
}

#define AddString(a, b)\
   char res2[50];\
   if (stringOverflow(a, b))\
       printf("Error overflow\n");\
	else {\
	   StringSum(a, b, res2, 50); \
	   printf("%s\n", res2); \
	}