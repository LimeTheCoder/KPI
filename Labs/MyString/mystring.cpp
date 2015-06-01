#include "mystring.h"

MyString::MyString() {
	str = NULL;
	size = 0;
	buff_size = 0;
}

MyString::MyString(const char *s) {
	str = NULL;

	if (NULL == s) {
		str = NULL;
		size = 0;
		buff_size = 0;
		return;
	}

	size = strlen(s);
	buff_size = 0;

	if (size) {
		buff_size = ((size + 1) / BLOCK_SIZE + 1) * BLOCK_SIZE;
		str = (char*)calloc(buff_size, sizeof(char));
		strcpy(str, s);
	}
}

MyString::MyString(const MyString &s) {
	str = NULL;
	size = s.Length();
	buff_size = 0;

	if (size) {
		buff_size = ((size + 1) / BLOCK_SIZE + 1) * BLOCK_SIZE;
		str = (char*)calloc(buff_size, sizeof(char));
		strcpy(str, s.c_str());
	}
}

MyString::~MyString() {
	if (str) {
		free(str);
		str = NULL;
	}
}

size_t MyString::BufferSize() const {
	return buff_size;
}

size_t MyString::Length() const {
	return size;
}

const char * MyString::c_str() const {
	return str;
}

MyString& MyString::operator= (MyString s) {
	swap(str, s.str);
	swap(size, s.size);
	swap(buff_size, s.buff_size);

	return *this;
}

char &MyString::at(size_t index){
	if (index < size) {
		return str[index];
	}
	throw invalid_argument("In function 'at'");
}

const char &MyString::at(size_t index) const {
	if (index < size) {
		return str[index];
	}
	throw invalid_argument("In function 'at'");
}

char &MyString::operator[](size_t index) {
	return str[index];
}

const char &MyString::operator[](size_t index) const {
	return str[index];
}

int cmp(MyString &a, MyString &b) {
	return strcmp(a.str, b.str);
}

MyString MyString::operator+ (const MyString &s) {
	size_t tmp_size = size + s.size;
	char *tmp = NULL;
	
	if (tmp_size) {
		tmp = (char*)calloc(tmp_size + 1, sizeof(char));
		// check mem

		if (str)
			strcpy(tmp, str);

		if (s.str)
			strcpy(tmp + size, s.str);
	}

	return tmp;
}

MyString &MyString::operator+= (const MyString &s) {
	return *this = *this + s;
}

