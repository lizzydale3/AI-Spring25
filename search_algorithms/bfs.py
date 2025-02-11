""" 
Breadth First Search (BFS) Algorithm
Used for finding the shortest path in an unweighted graph
"""

from collections import deque

def breadth_first_search (start_state, goal_test, successors):
    """
    Generic BFS implementation.
    :param start_state: The initial state.
    :param goal_test: Function to check if we reached the goal.
    :param successors: Function returning the next possible states.
    :return: The shortest path to the goal if found, otherwise None.
    """

    frontier = deque([start_state])
    explored = set
    parent_map = {start_state: None}

    while frontier:
        state = frontier.popleft()
        if goal_test(state):
            path = []
            while state:
                path.append(state)
                state = parent_map[state]
            return path[::-1]  # Reverse the path to get correct order

        explored.add(state)
        for neighbor in successors(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)
                parent_map[neighbor] = state  # Track path

    return None  # No solution found