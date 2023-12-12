# Checkpoint 3 (Generic algorithm):
import random

# Part 1:

def attacking_queens(state):
    """
    This function calculates the number of attacking queens for each queen in the state.
    """
    attacks = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                # Check for same column or diagonal
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacks += 1
    return attacks


def local_search(state):
    """
    This function performs hill-climbing search to find the local minimum for the given initial state.
    """
    current = state
    while True:
        attacks = attacking_queens(current)
        neighbors = []
        for col in range(len(current)):
            for row in range(1, 9):
                if row != current[col]:
                    neighbor = list(current)
                    neighbor[col] = row
                    neighbors.append(neighbor)
        if not neighbors:
            return current
        neighbor_attacks = [attacking_queens(neighbor) for neighbor in neighbors]
        min_attacks = min(neighbor_attacks)
        if min_attacks >= attacks:
            return current
        current = neighbors[neighbor_attacks.index(min_attacks)]


# Part 2:

# Generate 5 random initial states
initial_states = []
for i in range(5):
    state = [random.randint(1, 8) for i in range(8)]
    initial_states.append(state)

# Find local minimum for each initial state using hill-climbing
local_mins = []
for state in initial_states:
    local_min = local_search(state)
    local_mins.append(local_min)

# Sort the local minimum states by number of attacking queens
local_mins_sorted = sorted(local_mins, key=attacking_queens)

# Select two states with the lowest minima value
state1 = None
for state in local_mins_sorted:
    if attacking_queens(state) != 0:
        state1 = state
        break

state2 = None
for state in local_mins_sorted[1:]:
    if state != state1 and attacking_queens(state) != 0:
        state2 = state
        break

# Part 3:

def genetic_algorithm(state1, state2):
    """
    This function performs Genetic Algorithm on two states to generate a new state with improved heuristics.
    """
    # Crossover
    crossover_index = int(0.75 * len(state1))
    offspring = state2[:crossover_index] + state1[crossover_index:]

    # Mutation
    mutation_index = random.randint(0, len(offspring)-1)
    mutation_value = random.randint(1, 8)
    offspring[mutation_index] = mutation_value

    return offspring


# Generate a new state using Genetic Algorithm
new_state = genetic_algorithm(state1, state2)

# Perform local search on the new state to find the local minimum
local_min = local_search(new_state)

print("State 1:", state1)
print("Attacking queens in state 1:", attacking_queens(state1))
print("State 2:", state2)
print("Attacking queens in state 2:", attacking_queens(state2))
print()
print("After crossover & mutating, New state:", new_state)
print("Attacking queens in new state:", attacking_queens(new_state))
print()
print("Local minimum state:", local_min)
print("Attacking queens in local minimum state:", attacking_queens(local_min))