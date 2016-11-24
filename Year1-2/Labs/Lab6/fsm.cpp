#include "fsm.h"

FSM::FSM() {
	state = q0;
}

Event FSM::recognizeEvent(char ch) {
	Event event = ANY;

	if (ch == '/')
		event = SLASH;
	if (ch >= 'a' && ch <= 'z')
		event = LOWERCASE;
	if (ch >= 'F' && ch <= 'K')
		event = UPPERCASE;

	return event;
}

bool FSM::scan(string str) {
	Event event = ANY;
	size_t i = 0;

	state = q0;

	do {
		
		if (i < str.size())
			event = recognizeEvent(str[i]);
		else
			event = EOS;

		handleEvent(event);
		i++;

	} while (!(state == SUCCESS || state == ERROR));

	return state == SUCCESS;
}

void FSM::handleEvent(Event event) {
	switch (state) {
	case q0:
		if (event == SLASH)
			state = q1;
		else
			state = ERROR;

		break;

	case q1:
		switch (event) {
		case LOWERCASE:
			state = q2;
			break;
		case UPPERCASE:
			state = q3;
			break;
		default:
			state = ERROR;
		}

		break;

	case q2:
		if (event == UPPERCASE)
			state = q3;
		else if (event == LOWERCASE)
			state = q2;
		else
			state = ERROR;
		break;

	case q3:
		switch (event) {
		case UPPERCASE:
			state = q3;
			break;
		case EOS:
			state = SUCCESS;
			break;
		default:
			state = ERROR;
			break;
		}
	default:
		break;
	}
}