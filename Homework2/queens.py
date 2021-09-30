#!/usr/bin/python3

""""
Bryan Baker
bake1358@umn.edu
CSCI 5511 - Homework 2

A note on states:
Each state is a list of length 8.  This list represents each column of the board.  One queen is placed in each
column.  This ensures that there will be no attacks in any column.  Each column is given a number from 0 to 7
representing the row number that the queen is placed in.
"""

import random as ran
import numpy as np


def heuristic_h(state):
    """
    This is a cost function that finds and counts all of the pairs of attacking queens.
    :param state: This is a state as a list.
    :return: Returns an integer that is a count of the number of pairs of attacking queens in this state.
    """
    h = 0  # Initialize the counter
    for i in range(8):  # Check in each column
        row_up = state[i]  # This is a variable to check the upper diagonal direction from the queen.
        row_down = row_up  # This is a variable to check the lower diagonal direction from the queen.
        for j in range(i+1, 8):  # Only check queens to the right of the queen we are on to prevent double counting.
            row_up += 1
            row_down -= 1
            if state[i] == state[j]:  # Count if queens found in the same row
                h += 1
            if row_up == state[j]:  # Count if queens found in the upper diagonal direction
                h += 1
            if row_down == state[j]:  # Count if queens found in the lower diagonal direction
                h += 1
    return h


def hillclimb_sa(state):
    """
    This is the algorithm to implement steepest-ascent hill climb.
    :param state: This is a state as a list
    :return: Either a list of the final state and the count of the number of steps to reach this state from the
            initial state or a string indicating failure to find a solution.
    """
    if heuristic_h(state) == 0:  # If this initial state is a solution then return the state and give it a count of 0.
        return [state, 0]
    cnt = 1  # Initialize the counter
    while True:
        next_states = []  # Use this list to track the neighboring states
        values = []  # Use this to track the pairs of attacking queens for each neighboring state
        # The following code section generates all neighbors for the current state along with their values.
        for i in range(8):
            temp = state.copy()
            for j in range(8):
                temp[i] = j
                next_states.append(temp.copy())
                values.append(-heuristic_h(temp))
        value = max(values)  # Find the max value from the objective function to decide which state to move to.
        ind = values.index(value)  # Find the index of the list for this state.
        new_state = next_states[ind]  # Find the new state in the list of all neighboring states.
        if value == 0:  # If we have found a solution return the solution and the step count needed to get there.
            return [new_state, cnt]
        if new_state == state:  # If there is no state that is better than the current state then return fail.
            return "fail"
        state = new_state  # Update to the new state for the next loop iteration
        cnt += 1  # Update the step counter for the next loop iteration


"""
For the first choise method, use the binomial theorem to determine when to stop randomly searching:
If there exists one better state out of the 56 neighbors then
the probability of not hitting the state is 55/56 for a given random state
The probability of hitting the better state at least once is: 1 - (55/56)^n where n is the number of random states tried
Therefore, if n = 300 then we will hit the state sometime in the 300 steps with a probability of 99.6%
"""


def hillclimb_fc(state):
    """
    This is the algorithm to implement first-choice hill climb.
    :param state: This is a state as a list
    :return: Either a list of the final state and the count of the number of steps to reach this state from the
            initial state or a string indicating failure to find a solution.
    """
    if heuristic_h(state) == 0:  # If this initial state is a solution then return the state and give it a count of 0.
        return [state, 0]
    cnt = 1  # Initialize the counter
    while True:
        step = 0  # Initialize the random state counter
        while step < 300:  # Use 300 based on binomial prob of seeing 99.6% of states if assuming one is the best.
            next = state.copy()
            while state == next:  # This code block prevents the random state from being the same as the initial state.
                col = ran.randint(0, 7)
                row = ran.randint(0, 7)
                next[col] = row
            if heuristic_h(next) == 0:  # If we have found a solution return the solution and the step count.
                return [next, cnt]
            if -heuristic_h(next) > -heuristic_h(state):  # If the new state is better then go there.
                state = next
                cnt += 1
                break
            step += 1  # Update the random state counter
        if step == 300 and heuristic_h(state) != 0 and heuristic_h(next) != 0:  # Fail on reaching max step
            return "fail"


def sim_anneal(state, schedule):
    """
    This is the algorithm to implement simulated annealing.
    :param state: This is a state as a list
    :param schedule: This is a schedule of temps as a list
    :return: Either a list of the final state and the count of the number of steps to reach this state from the
            initial state or a string indicating failure to find a solution.
    """
    if heuristic_h(state) == 0:  # If this initial state is a solution then return the state and give it a count of 0.
        return [state, 0]
    n = len(schedule)
    cnt = 0  # Initialize the counter
    step = 0  # Initialize the temperature step counter
    while step < n and heuristic_h(state) != 0:
        T = schedule[step]
        if T == 0:  # If this is the end of the temperature schedule then break the loop
            break
        next = state.copy()
        while state == next:  # This code block prevents the random state from being the same as the initial state.
            col = ran.randint(0, 7)
            row = ran.randint(0, 7)
            next[col] = row
        delta = heuristic_h(state) - heuristic_h(next)  # Calculate the energy delta
        if delta > 0 or np.exp(delta/T) > 0.5:  # If next state better or probability greater than 0.5 go to next state
            state = next
            cnt += 1  # Increment the state change counter
        step += 1  # Increment the temperature counter
    if heuristic_h(state) == 0:  # If we have found a solution return the solution and the step count.
        return [state, cnt]
    else:  # Otherwise fail
        return "fail"


def create_states(n):
    """
    This function creates a dictionary of initial states to use for each algorithm.
    :param n: This is the number of initial states to create as an integer.
    :return: This returns a dictionary of initial states.
    """
    state_dict = {}  # Initialize an empty dictionary
    for i in range(n):
        state = [ran.randint(0, 7) for j in range(8)]  # Create a random state
        state_dict.update({i: state})  # Add the state to the dictionary
    return state_dict


def compute_avg_sa(state_dict):
    """
    This function tries each initial state in the hillclimb_sa algorithm and reports some statistics.
    :param state_dict: This is a dictionary of initial states created by the create_states() function
    :return: Nothing to return
    """
    sums = 0  # Initialize sum variable
    cnt = 0  # Initialize solution counter
    for _, (key, state) in enumerate(state_dict.items()):  # Loop over all initial states in the dictionary
        result = hillclimb_sa(state)  # Apply the hillclimb SA function
        if result != "fail" and result[1] > 0:  # Only count solutions found by the algorithm no initial states
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Hillclimb Steepest-Ascent: {sums/cnt:0.6f}")  # Report the average step count
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")  # Report the number of cases solved.
    print(" ")
    return None


def compute_avg_fc(state_dict):
    """
    This function tries each initial state in the hillclimb_fc algorithm and reports some statistics.
    :param state_dict: This is a dictionary of initial states created by the create_states() function
    :return: Nothing to return
    """
    sums = 0  # Initialize sum variable
    cnt = 0  # Initialize solution counter
    for _, (key, state) in enumerate(state_dict.items()):  # Loop over all initial states in the dictionary
        result = hillclimb_fc(state)  # Apply the hillclimb FC function
        if result != "fail" and result[1] > 0:  # Only count solutions found by the algorithm no initial states
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Hillclimb First-Choice: {sums/cnt:0.6f}")  # Report the average step count
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")  # Report the number of cases solved.
    print(" ")
    return None


def compute_avg_anneal(state_dict, schedule):
    """
    This function tries each initial state in the simulated annealing algorithm and reports some statistics.
    :param state_dict: This is a dictionary of initial states created by the create_states() function
    :param schedule: This is a list of temperatures to try
    :return: Nothing to return
    """
    sums = 0  # Initialize sum variable
    cnt = 0  # Initialize solution counter
    for _, (key, state) in enumerate(state_dict.items()):  # Loop over all initial states in the dictionary
        result = sim_anneal(state, schedule)  # Apply the simulated anneal function
        if result != "fail" and result[1] > 0:  # Only count solutions found by the algorithm no initial states
            sums += result[1]
            cnt += 1
    print(f"The average steps to solve Simulated Anneal: {sums/cnt:0.6f}")  # Report the average step count
    print(f"Solved {cnt/len(state_dict) * 100:0.6f} percent of the cases.")  # Report the number of cases solved.
    print(" ")
    return None


if __name__ == "__main__":
    print("Creating 10000 initial states:")
    states = create_states(10000)  # Create 10000 initial states
    print(" ")

    print("Solving using Hillclimb Steepest-Ascent:")
    compute_avg_sa(states)  # Solve the initial states using hillclimb_sa

    print("Solving using Hillclimb First-Choice:")
    compute_avg_fc(states)  # Solve the initial states using hillclimb_fc

    print("Creating the temperature schedule:")
    # Define the temperature schedule for simulated annealing
    temps = [0.8**i for i in range(0, 1000, 1)]
    temps.append(0)
    print("Solving using Simulated Annealing:")
    compute_avg_anneal(states, temps)  # Solve the initial states using sim_anneal
