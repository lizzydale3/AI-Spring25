import random

class VacuumEnvironment:
    def __init__(self, width=2, height=1, dirt_probability=0.5, movement_cost=0):
        self.width = width
        self.height = height
        self.grid = [[random.choice(["Clean", "Dirty"]) if random.random() < dirt_probability else "Clean"
                      for _ in range(width)] for _ in range(height)]
        self.agent_position = (0, 0)
        self.performance_score = 0
        self.movement_cost = movement_cost
    
    def percept(self):
        x, y = self.agent_position
        return self.grid[y][x]  # Returns "Clean" or "Dirty"
    
    def execute_action(self, action):
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
        elif action == "Up" and y > 0:
            self.agent_position = (x, y - 1)
            self.performance_score -= self.movement_cost
        elif action == "Down" and y < self.height - 1:
            self.agent_position = (x, y + 1)
            self.performance_score -= self.movement_cost

    def is_clean(self):
        return all(all(cell == "Clean" for cell in row) for row in self.grid)

class SimpleReflexAgent:
    def __init__(self):
        pass
    
    def decide(self, percept):
        if percept == "Dirty":
            return "Suck"
        return random.choice(["Left", "Right"])  # Moves randomly if the square is clean

# Run the simulation
def run_simulation(env, agent, steps=10):
    for _ in range(steps):
        percept = env.percept()
        action = agent.decide(percept)
        env.execute_action(action)
        if env.is_clean():
            break  # Stop if everything is clean
    return env.performance_score

# Initialize and test
env = VacuumEnvironment(width=2, height=1, dirt_probability=0.5, movement_cost=1)
agent = SimpleReflexAgent()
score = run_simulation(env, agent, steps=100)
print(f"Final Performance Score: {score}")
