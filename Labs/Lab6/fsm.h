#include <string>

using namespace std;

enum State {q0, q1, q2, q3, ERROR, SUCCESS};
enum Event {SLASH, UPPERCASE, LOWERCASE, ANY, EOS};

class FSM {
protected:
	State state;
	Event recognizeEvent(char);
	virtual void handleEvent(Event);

public:
	FSM();
	bool scan(string);
};