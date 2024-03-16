# Constants for the game
GRID_WIDTH, GRID_HEIGHT = 420, 420  # Size of the window, adjust as per your layout's requirement
FPS = 30  # Frames per second

# Constant for the right container
RIGHT_CONTAINER_WIDTH = 240  # Width of the right container

# Constant for the window width and height
WINDOW_WIDTH = GRID_WIDTH + RIGHT_CONTAINER_WIDTH
WINDOW_HEIGHT = GRID_HEIGHT + 50  # Bottom margin to display the score

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
MEDIUM_GREY = (128, 128, 128)

# Define the size of the buttons
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

# Grid configuration
GRID_SIZE_W = 6
GRID_SIZE_H = 6
CELL_SIZE_W = GRID_WIDTH // GRID_SIZE_W
CELL_SIZE_H = GRID_HEIGHT // GRID_SIZE_H
LINE_WIDTH = 1  # Width of the lines in the grid

# Define the reward for an empty field
EMPTY_REWARD = -0.04

# Define hole locations
holes = {
    (1, 1): -1,
    (5, 1): -1,
    (2, 2): -1,
    (3, 3): -1,
    (4, 4): -1,
}

# Define reward locations
rewards = {
    (0, 0): +1,
    (2, 0): +1,
    (5, 0): +1,
    (3, 1): +1,
    (4, 2): +1,
    (5, 3): +1,

}

# Define wall locations
walls = {
    (1, 0),
    (4, 1),
    (1, 4),
    (2, 4),
    (3, 4)
}

# Starting position of the agent
starting_position = (2, 3)

# Define the possible actions and how they affect the position of the agent
actions = {
    'up': (0, -1),
    'right': (1, 0),
    'down': (0, 1),
    'left': (-1, 0)
}

# Define the discount factor
DISCOUNT_FACTOR = 0.99


# Define the transition model
def transition_model(a):
    a_index = list(actions.keys()).index(a)
    left_a = list(actions.keys())[(a_index - 1) % len(actions)]
    right_a = list(actions.keys())[(a_index + 1) % len(actions)]
    # Return the possible actions and their probabilities
    return {left_a: 0.1, a: 0.8, right_a: 0.1}


# Define the constants for the value iteration algorithm
R_MAX = 1.00
C = 0.10
EPSILON = C * R_MAX
SMALL_ENOUGH = EPSILON * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR
