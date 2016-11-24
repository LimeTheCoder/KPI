#ifndef MYSTRING_H
#define MYSTRING_H

#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <stdexcept>

using namespace std;

const int BLOCK_SIZE = 16;

class MyString
{
	size_t size;
	size_t buff_size;
	char *str;

public:
	MyString();
	MyString(const char*);
	MyString(const MyString &);
	~MyString();

	MyString &operator= (MyString);
	MyString operator+ (const MyString &);
	MyString &operator+= (const MyString &);

	char &at(size_t);
	const char &at(size_t) const;
	char &operator[](size_t);
	const char &operator[](size_t) const;

	friend int cmp(MyString &, MyString &);
	
	size_t Length() const;
	size_t BufferSize() const;
	const char *c_str() const;
};

#endif // MYSTRING_H
