import random as ran
from queue import PriorityQueue


def heuristic_h(state):
    h = 0
    for i in range(8):
        row_up = state[i]
        row_down = row_up
        for j in range(i+1, 8):
            row_up += 1
            row_down -= 1
            if state[i] == state[j]:
                h += 1
            if row_up == state[j]:
                h += 1
            if row_down == state[j]:
                h += 1
    return h


def hillclimb_sa(state):
    if heuristic_h(state) == 0:
        return [state, 0]
    cnt = 1
    while True:
        next_states = PriorityQueue()
        for i in range(8):
            temp = state.copy()
            for j in range(8):
                temp[i] = j
                next_states.put((heuristic_h(temp), temp.copy()))
        value, new_state = next_states.get()
        if value == 0:
            return [new_state, cnt]
        if new_state == state:
            return "fail"
        state = new_state
        cnt += 1


def create_states(n):
    state_dict = {}
    for i in range(n):
        state = [ran.randint(0, 7) for j in range(8)]
        state_dict.update({i: state})
    return state_dict


def compute_avg_sa(state_dict):
    sums = 0
    cnt = 0
    for _, (key, state) in enumerate(state_dict.items()):
        result = hillclimb_sa(state)
        if result != "fail":
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve hillclimb steepest-ascent: {sums/cnt:0.6f}")
    return None


states = create_states(10000)
compute_avg_sa(states)
