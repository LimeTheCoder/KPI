#include "tfsm.h"

void TransitionTable::addTransition(State start, Event e, State end) {
	table[start][e] = end;
}

State TransitionTable::getEndState(State start, Event trigger) {
	return table[start][trigger];
}

TFSM::TFSM() : FSM() {
	table.addTransition(q0, SLASH, q1);
	table.addTransition(q0, UPPERCASE, ERROR);
	table.addTransition(q0, LOWERCASE, ERROR);
	table.addTransition(q0, ANY, ERROR);
	table.addTransition(q0, EOS, ERROR);

	table.addTransition(q1, SLASH, ERROR);
	table.addTransition(q1, UPPERCASE, q3);
	table.addTransition(q1, LOWERCASE, q2);
	table.addTransition(q1, ANY, ERROR);
	table.addTransition(q1, EOS, ERROR);

	table.addTransition(q2, SLASH, ERROR);
	table.addTransition(q2, UPPERCASE, q3);
	table.addTransition(q2, LOWERCASE, ERROR);
	table.addTransition(q2, ANY, ERROR);
	table.addTransition(q2, EOS, ERROR);

	table.addTransition(q3, SLASH, ERROR);
	table.addTransition(q3, UPPERCASE, q3);
	table.addTransition(q3, LOWERCASE, ERROR);
	table.addTransition(q3, ANY, ERROR);
	table.addTransition(q3, EOS, SUCCESS);
}

void TFSM::handleEvent(Event event) {
	state = table.getEndState(state, event);
}