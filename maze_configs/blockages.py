# Define hole locations
HOLES = {
    (0, 1): -1, (0, 4): -1,
    (1, 1): -1,
    (2, 0): -1, (2, 8): -1,
    (3, 0): -1,
    (4, 6): -1,
    (5, 0): -1,
    (6, 8): -1,
    (8, 1): -1, (8, 2): -1
}

# Define reward locations
REWARDS = {
    (1, 0): 1,
    (4, 0): 1,
    (8, 0): 1,
}

# Define wall locations
WALLS = {
    (0, 8), (1, 8), (3, 8), (4, 8), (5, 8), (7, 8), (8, 8),
    (1, 6), (2, 6), (3, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
    (8, 5), (9, 5),
    (1, 4), (3, 4), (4, 4), (5, 4), (6, 4),
    (0, 2), (1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (9, 2)
}

# Starting position of the agent
STARTING_POSITION = (4, 9)

# Grid configuration
GRID_SIZE_W = 10
GRID_SIZE_H = 10

# Define the reward for an empty field
EMPTY_REWARD = -0.04
