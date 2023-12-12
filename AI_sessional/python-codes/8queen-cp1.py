# Checkpoint 1:

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


# Initial state
initial_state = [4, 3, 6, 2, 5, 4, 7, 3]

# Find the local minimum using hill-climbing
local_min = local_search(initial_state)

print("Initial state:", initial_state)
print("Attacking queens in initial state:", attacking_queens(initial_state))
print("Local minimum state:", local_min)
print("Attacking queens in local minimum state:", attacking_queens(local_min))