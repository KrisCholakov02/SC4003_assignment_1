# Define hole locations
HOLES = {
    (1, 1): -1,
    (5, 1): -1,
    (2, 2): -1,
    (3, 3): -1,
    (4, 4): -1,
}

# Define reward locations
REWARDS = {
    (0, 0): +1,
    (2, 0): +1,
    (5, 0): +1,
    (3, 1): +1,
    (4, 2): +1,
    (5, 3): +1,

}

# Define wall locations
WALLS = {
    (1, 0),
    (4, 1),
    (1, 4),
    (2, 4),
    (3, 4)
}

# Starting position of the agent
STARTING_POSITION = (2, 3)

# Grid configuration
GRID_SIZE_W = 6
GRID_SIZE_H = 6

# Define the reward for an empty field
EMPTY_REWARD = -0.04
