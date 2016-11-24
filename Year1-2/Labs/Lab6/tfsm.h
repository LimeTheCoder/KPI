#include "fsm.h"

const int STATE_CNT = 4;
const int EVENT_CNT = 5;


class TransitionTable {
	State table[STATE_CNT][EVENT_CNT];
public:
	void addTransition(State startstate, Event e, State endstate);
	State getEndState(State startstate, Event e);
};

class TFSM : public FSM {
	TransitionTable table;
public:
	void handleEvent(Event);
	TFSM();
};