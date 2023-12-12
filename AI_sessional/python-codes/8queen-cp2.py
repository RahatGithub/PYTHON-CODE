# Checkpoint 2 (For 5 random starting states):
import random


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


# Function to perform local search on 5 random initial states
def local_search_random_starts():
    for i in range(5):
        # Generate a random initial state
        initial_state = [random.randint(1, 8) for j in range(8)]
        print("Random initial state", i + 1, ":", initial_state)
        # Perform local search on the initial state
        local_min = local_search(initial_state)
        # Check if the local minimum is the goal state (0 attacking queens)
        if attacking_queens(local_min) == 0:
            print("Solution found for random initial state", i + 1, ":", local_min)
        else:
            print("No solution found for random initial state", i + 1)
        print("Attacking queens in local minimum state:", attacking_queens(local_min))
        print()


# Perform local search on 5 random initial states
local_search_random_starts()

#
# # Initial state
# initial_state = [4, 3, 6, 2, 5, 4, 7, 3]
#
# # Find the local minimum using hill-climbing
# local_min = local_search(initial_state)
#
# print("Initial state:", initial_state)
# print("Attacking queens in initial state:", attacking_queens(initial_state))
# print("Local minimum state:", local_min)
# print("Attacking queens in local minimum state:", attacking_queens(local_min))