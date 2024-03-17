# Define hole locations
HOLES = {
    (2, 7): -1, (6, 4): -1, (5, 7): -1, (4, 0): -1, (0, 1): -1,
    (7, 4): -1, (2, 6): -1, (4, 9): -1, (9, 2): -1, (8, 4): -1,
    (0, 6): -1, (3, 0): -1, (3, 5): -1, (4, 6): -1, (1, 6): -1,
    (5, 5): -1
}

# Define reward locations
REWARDS = {
    (9, 5): 1, (9, 0): 1, (7, 1): 1, (6, 3): 1, (8, 1): 1,
    (4, 8): 1, (1, 1): 1, (0, 7): 1, (1, 5): 1, (7, 8): 1,
    (6, 1): 1, (6, 0): 1, (7, 7): 1, (0, 0): 1, (3, 9): 1,
    (0, 3): 1
}

# Define wall locations
WALLS = {
    (2, 4), (3, 1), (2, 3), (1, 7), (0, 2), (4, 5), (5, 6),
    (8, 6), (2, 2), (6, 6), (5, 9), (7, 5), (5, 2), (1, 3),
    (4, 7), (9, 4)
}

# Starting position of the agent
STARTING_POSITION = (4, 4)

# Grid configuration
GRID_SIZE_W = 10
GRID_SIZE_H = 10

# Define the reward for an empty field
EMPTY_REWARD = -0.04
