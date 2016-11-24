#include "List.h"
#include <windows.h>

class HashTable {
public:
	HashTable();
	~HashTable();
	int HashFunc(double);
	int Insert(double, Square);
	void Show();
	void DeleteByTask(double);
	Square* Search(double);

private:
	int size;
	List **mass;
};

HashTable::HashTable() {
	size = 11;
	mass = new List*[size];
	for (int i = 0; i < size; i++)
		mass[i] = new List;
}

HashTable::~HashTable() {
	for (int i = 0; i < size; i++)
		delete mass[i];
	delete[] mass;
}

Square* HashTable::Search(double key) {
	int index = HashFunc(key);
	Square *obj = mass[index]->Search(key);
	if (obj != NULL)
		return obj;
	else 
		return NULL;
}

int HashTable::HashFunc(double key) {
	return (int)key % size;
}

int HashTable::Insert(double key, Square data) {
	int index = HashFunc(key);
	mass[index]->Add(data);
	return index;
}

void HashTable::Show() {
	for (int i = 0; i < size; i++) {
		if (!mass[i]->isEmpty()) {
			printf("Cell #%d consist %d elements:\n", i, mass[i]->Size());
			mass[i]->Show();
			printf("\n");
		}
	}
}

void HashTable::DeleteByTask(double key) {
	for (int i = 0; i < size; i++) {
		while (mass[i]->DeleteByParam(key)){};
	}
}

void fillTable(HashTable &);

int main() {
	HashTable h;
	fillTable(h);
	h.Show();
	getchar();
	system("cls");
	printf("After deleting:\n");
	h.DeleteByTask(26);
	h.Show();
	return 0;
}

void fillTable(HashTable &tbl) {
	Coord a;
	Coord b;
	Coord c;
	Coord d;
	Square sqr;

	for (int i = 1; i < 13; i++) {
		a.SetCoords(0, 0);
		b.SetCoords(0, i);
		c.SetCoords(i, 0);
		d.SetCoords(i, i);
		sqr.SetVertex(a, b, c, d);
		tbl.Insert(sqr.Perim(), sqr);
	}
}