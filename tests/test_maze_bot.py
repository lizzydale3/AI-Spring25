import unittest
from problem_solvers.maze_bot import bfs_maze_solver, Maze

class TestMazeBot(unittest.TestCase):
    def test_maze_solver(self):
        """Tests BFS Maze Solver with a simple 3x4 maze."""
        grid = [
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0]
        ]
        maze = Maze(grid, (0, 0), (2, 3))
        solution = bfs_maze_solver(maze)

        expected_solution = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]
        self.assertEqual(solution, expected_solution)  # Check if paths match

if __name__ == "__main__":
    unittest.main()
