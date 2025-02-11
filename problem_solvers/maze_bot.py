"""
Maze Solver - AI Agent
Solves a maze using Breadth-First Search (BFS).
"""

from collections import deque

class Maze:
    """ Represents a 2D maze where an agent finds the shortest path. """
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def get_successors(self, state):
        """ Returns valid neighboring positions the agent can move to. """
        x, y = state
        successors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] != 1:
                successors.append((nx, ny))
        
        return successors

def bfs_maze_solver(maze):
    """ Solves the maze using BFS. """
    frontier = deque([maze.start])
    explored = set()
    parent_map = {maze.start: None}  # To reconstruct the path

    while frontier:
        state = frontier.popleft()
        if maze.is_goal(state):
            path = []
            while state:
                path.append(state)
                state = parent_map[state]
            return path[::-1]  # Return reversed path
        
        explored.add(state)
        for neighbor in maze.get_successors(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)
                parent_map[neighbor] = state

    return None  # No solution found

# Run the maze solver
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    maze = Maze(grid, (0, 0), (2, 3))
    solution = bfs_maze_solver(maze)
    print("Solution path:", solution)
