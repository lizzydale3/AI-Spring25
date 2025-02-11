# AI Projects Repository

This repository contains implementations of AI algorithms and problem-solving techniques inspired by *Artificial Intelligence: A Modern Approach*.

## Implemented AI Problems
- **Maze Solver** (BFS-based) → Finds the shortest path in a 2D maze.
- **Vacuum Bot** (Reflex agent) → Simulates a simple cleaning robot.

## Implemented AI Algorithms
- **Breadth-First Search (BFS)** → Graph traversal and pathfinding.
- **Depth-First Search** (coming soon) → Explores all paths before backtracking.

## Maze Solver (BFS-Based)

The **Maze Solver** uses **Breadth-First Search (BFS)** to find the shortest path in a 2D grid-based maze.

### Example Maze
0  0  1  0
1  0  1  0
0  0  0  0

- **0** = Open path
- **1** = Wall
- **Start Position:** `(0,0)`
- **Goal Position:** `(2,3)`

### Expected Output:
Solution path: [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]

### How to Run:
python3 problem_solvers/maze_bot.py

## Vacuum Bot (Reflex Agent)

The **Vacuum Bot** simulates an intelligent cleaning agent in a **2D grid world**.

### Behavior:
- If the agent is in a **dirty** square, it cleans it.
- If the square is **clean**, it moves **right** (or left if blocked).
- Performance is measured based on cleaning efficiency.

### How to Run:
python3 problem_solvers/vacuum_bot.py

## Running Tests
This repository includes **unit tests** to ensure correctness.

To run all tests:
python3 -m unittest discover tests

### Current Tests:
- `test_maze_bot.py` → Tests if BFS finds the shortest path in a sample maze.
- `test_vacuum_bot.py` (coming soon!)

More algorithms coming soon!
