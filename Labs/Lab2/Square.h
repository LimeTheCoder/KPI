#include <math.h>
#include <stdio.h>

struct Coord {
	Coord(){ x = 0; y = 0; };
	Coord(int a, int b) { x = a; y = b; };
	~Coord(){};

	void SetCoords(int a, int b) { x = a; y = b; };

	int x, y;
};


class Square {
public:
	Square();
	Square(Coord, Coord, Coord, Coord);
	~Square();
	double Side(Coord, Coord);
	double Area();
	double Perim();
	void Show();
	void SetVertex(Coord, Coord, Coord, Coord);
private:
	Coord a, b, c, d;
};