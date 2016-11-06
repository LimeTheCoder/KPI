#include "Square.h"

Square::Square() {
	a.x = 0;
	a.y = 0;
	b.x = 0;
	b.y = 0;
	c.x = 0;
	c.y = 0;
	d.x = 0;
	d.y = 0;
}

Square::Square(Coord coordA, Coord coordB, Coord coordC, Coord coordD) {
	a = coordA;
	b = coordB;
	c = coordC;
	d = coordD;
}

void Square::SetVertex(Coord coordA, Coord coordB, Coord coordC, Coord coordD) {
	a = coordA;
	b = coordB;
	c = coordC;
	d = coordD;
}

Square::~Square() {}

double Square::Side(Coord coordA, Coord coordB) {
	return sqrt((double)((coordB.x - coordA.x) * (coordB.x - coordA.x) + (coordB.y - coordA.y) * (coordB.y - coordA.y)));
}

double Square::Area(){
	return Side(a, b) * Side(a, b);
}

double Square::Perim() {
	return 4 * Side(a, b);
}

void Square::Show() {
	printf("Area: %0.2f, Perimeter: %0.2f\n", Area(), Perim());
}