import random as ran
import numpy as np


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
        next_states = []
        values = []
        for i in range(8):
            temp = state.copy()
            for j in range(8):
                temp[i] = j
                next_states.append(temp.copy())
                values.append(-heuristic_h(temp))
        value = max(values)
        ind = values.index(value)
        new_state = next_states[ind]
        if value == 0:
            return [new_state, cnt]
        if new_state == state:
            return "fail"
        state = new_state
        cnt += 1


# Use binomial:
# prob of not hitting is 55/56
# prob of hitting at least once: 1 - (55/56)^n
# if n = 300 then P=0.996
def hillclimb_fc(state):
    if heuristic_h(state) == 0:
        return [state, 0]
    cnt = 1
    step = 0
    while step < 300:
        next = state.copy()
        while state == next:
            col = ran.randint(0, 7)
            row = ran.randint(0, 7)
            next[col] = row
        if heuristic_h(next) == 0:
            return [next, cnt]
        if -heuristic_h(next) > -heuristic_h(state):
            state = next
            cnt += 1
        step += 1
    return "fail"


def sim_anneal(state, schedule):
    if heuristic_h(state) == 0:
        return [state, 0]
    n = len(schedule)
    cnt = 0
    step = 0
    while step < n and heuristic_h(state) != 0:
        T = schedule[step]
        if T == 0:
            break
        next = state.copy()
        while state == next:
            col = ran.randint(0, 7)
            row = ran.randint(0, 7)
            next[col] = row
        delta = heuristic_h(state) - heuristic_h(next)
        if delta > 0 or np.exp(delta/T) > 0.5:
            state = next
            cnt += 1
        step += 1
    if heuristic_h(state) == 0:
        return [state, cnt]
    else:
        return "fail"


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
        if result != "fail" and result[1] > 0:
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Hillclimb Steepest-Ascent: {sums/cnt:0.6f}")
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")
    return None


def compute_avg_fc(state_dict):
    sums = 0
    cnt = 0
    for _, (key, state) in enumerate(state_dict.items()):
        result = hillclimb_fc(state)
        if result != "fail" and result[1] > 0:
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Hillclimb First-Choice: {sums/cnt:0.6f}")
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")
    return None


def compute_avg_anneal(state_dict, schedule):
    sums = 0
    cnt = 0
    for _, (key, state) in enumerate(state_dict.items()):
        result = sim_anneal(state, schedule)
        if result != "fail" and result[1] > 0:
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Simulated Anneal: {sums/cnt:0.6f}")
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")
    return None


states = create_states(10000)
compute_avg_sa(states)
compute_avg_fc(states)
temps = [0.8**i for i in range(0, 1000, 1)]
temps.append(0)
compute_avg_anneal(states, temps)
