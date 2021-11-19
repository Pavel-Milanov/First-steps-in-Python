begin_state = "q0"
end_states = {"q0": 1}
FSM = {
    "q0": {"1": "q1", "0": "q2"},
    "q1": {"1": "q0", "0": "q3"},
    "q2": {"0": "q0", "1": "q3"},
    "q3": {"1": "q2", "0": "q1"},
}


def parseFSM(text, FSM, beginState, endStates):
    cur_state = beginState
    i = 0
    try:
        for i in range(0, len(text)):
            if FSM[cur_state][text[i]] is not None:
                cur_state = FSM[cur_state][text[i]]
            else:
                return False
        if endStates[cur_state] is not None:
            return True
        else:
            return False
    except KeyError as e:
        print({"cur_state": cur_state, "exception": e, "text_letter": text[i], "pos": i})
        return False


print(parseFSM("1001", FSM, begin_state, end_states))