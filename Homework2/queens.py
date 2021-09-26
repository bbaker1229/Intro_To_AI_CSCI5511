import random as ran

# Create a sample state
state = [ran.randint(0, 7) for i in range(8)]

h=0
for i in range(8):
    row_up = state[i]
    row_down = row_up
    for j in range(i+1, 8):
        row_up += 1
        row_down -= 1
        if state[i] == state[j] or row_up == state[j] or row_down == state[j]:
            h+=1