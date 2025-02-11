"""
8-Puzzle Solvability Checker

This module determines if a given 8-puzzle state is solvable by checking its inversion parity.
If two states have the same number of inversions modulo 2, they are in the same set.

A state is represented as a list of numbers (0-8), where 0 represents the blank space.

Example:
    initial_state = [1, 2, 3, 4, 6, 5, 7, 8, 0]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print(is_solvable(initial_state, goal_state))  # Output: True or False
"""

def count_inversions(state):
    """
    Counts the number of inversions in an 8-puzzle state.
    An inversion is when a higher-numbered tile appears before a lower-numbered tile.
    
    :param state: List of 9 integers (0 represents the blank space)
    :return: Number of inversions
    """
    flattened = [tile for tile in state if tile != 0]  # Remove the blank space (0)
    inversions = 0
    
    for i in range(len(flattened)):
        for j in range(i + 1, len(flattened)):
            if flattened[i] > flattened[j]:
                inversions += 1
    
    return inversions

def is_solvable(initial_state, goal_state):
    """
    Determines if an 8-puzzle state is solvable by comparing its inversion count
    with the goal state's inversion count.

    :param initial_state: List of 9 integers representing the initial configuration
    :param goal_state: List of 9 integers representing the goal configuration
    :return: True if solvable, False otherwise
    """
    return count_inversions(initial_state) % 2 == count_inversions(goal_state) % 2

# Example Usage
if __name__ == "__main__":
    initial_state = [1, 2, 3, 4, 6, 5, 7, 8, 0]  # 0 represents the blank space
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    if is_solvable(initial_state, goal_state):
        print("The puzzle is solvable.")
    else:
        print("The puzzle is NOT solvable.")
