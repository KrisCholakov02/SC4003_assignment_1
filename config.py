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
GRID_SIZE = 6  # Grid size of the maze, adjust according to your design
CELL_SIZE = GRID_WIDTH // GRID_SIZE
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