"""
Vacuum Bot Environment - AI Agent
Simulates a simple reflex agent in a 2D grid-based environment.
Inspired by Artificial Intelligence: A Modern Approach.
"""

import random

class VacuumEnvironment:
    """
    Represents a 2D vacuum world where an agent moves and cleans.
    The grid consists of Clean and Dirty cells.
    """
    def __init__(self, width=2, height=1, dirt_probability=0.5, movement_cost=1):
        self.width = width
        self.height = height
        self.movement_cost = movement_cost
        self.performance_score = 0

        # Initialize grid with random dirt
        self.grid = [[random.choice(["Clean", "Dirty"]) if random.random() < dirt_probability else "Clean"
                      for _ in range(width)] for _ in range(height)]

        # Agent starts at (0,0)
        self.agent_position = (0, 0)

    def perceive(self):
        """ Returns the dirt status at the agent's current position. """
        x, y = self.agent_position
        return self.grid[y][x]  # "Clean" or "Dirty"

    def execute_action(self, action):
        """ Executes an action: Move or Clean. """
        x, y = self.agent_position

        if action == "Suck":
            if self.grid[y][x] == "Dirty":
                self.grid[y][x] = "Clean"
                self.performance_score += 10  # Reward for cleaning
        elif action == "Left" and x > 0:
            self.agent_position = (x - 1, y)
            self.performance_score -= self.movement_cost
        elif action == "Right" and x < self.width - 1:
            self.agent_position = (x + 1, y)
            self.performance_score -= self.movement_cost

    def display_grid(self):
        """ Prints the environment grid. """
        for row in self.grid:
            print(" ".join(row))
        print(f"Agent Position: {self.agent_position}, Score: {self.performance_score}")

class VacuumBot:
    """ Simple Reflex Agent for cleaning a grid environment. """
    def __init__(self, environment):
        self.environment = environment

    def run(self, steps=5):
        """ Runs the agent for a number of steps. """
        for _ in range(steps):
            status = self.environment.perceive()
            if status == "Dirty":
                self.environment.execute_action("Suck")
            else:
                self.environment.execute_action("Right")  # Moves right if clean
            self.environment.display_grid()

# Run the simulation
if __name__ == "__main__":
    env = VacuumEnvironment(width=5, height=1, dirt_probability=0.4)
    bot = VacuumBot(env)
    bot.run()
