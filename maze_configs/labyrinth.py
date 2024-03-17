# Define hole locations
HOLES = {
    (0, 2): -1,
    (2, 6): -1,
    (3, 0): -1, (3, 1): -1, (3, 2): -1,
    (4, 2): -1, (4, 7): -1, (4, 9): -1,
    (5, 4): -1, (5, 8): -1,
    (6, 0): -1,
    (7, 5): -1, (7, 9): -1,
    (8, 4): -1,
    (9, 1): -1, (9, 8): -1
}

# Define reward locations
REWARDS = {
    (1, 2): 1, (1, 6): 1, (1, 8): 1,
    (2, 0): 1,
    (3, 9): 1,
    (5, 0): 1, (5, 7): 1, (5, 9): 1,
    (7, 7): 1,
    (9, 0): 1, (9, 2): 1, (9, 5): 1, (9, 9): 1
}

# Define wall locations
WALLS = {
    (0, 4),
    (1, 0), (1, 1), (1, 4),
    (2, 1), (2, 2), (2, 8), (2, 9),
    (3, 3), (3, 5), (3, 6),
    (4, 0), (4, 1),
    (5, 3), (5, 6),
    (6, 2), (6, 3), (6, 4), (6, 7), (6, 8), (6, 9),
    (7, 1), (7, 3),
    (8, 3), (8, 7),
    (9, 3)
}

# Starting position of the agent
STARTING_POSITION = (4, 5)

# Grid configuration
GRID_SIZE_W = 10
GRID_SIZE_H = 10

# Define the reward for an empty field
EMPTY_REWARD = -0.04
