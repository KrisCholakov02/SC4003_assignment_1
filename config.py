# Import the different maze configurations
import maze_configs.base as base_config
import maze_configs.increased_size as increased_size_config
import maze_configs.labyrinth as labyrinth_config
import maze_configs.blockages as blockages_config

# Constants for the game
GRID_WIDTH, GRID_HEIGHT = 720, 720  # Size of the window, adjust as per your layout's requirement
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
BLUE = (0, 0, 255)


# Define a function to get the color of the cell based on its position
def get_cell_color(pos):
    if pos in REWARDS:
        return GREEN
    elif pos in HOLES:
        return ORANGE
    elif pos in WALLS:
        return MEDIUM_GREY
    elif pos == STARTING_POSITION:
        return BLUE
    else:
        return WHITE


# Define the size of the buttons
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

# Grid configuration
LINE_WIDTH = 1  # Width of the lines in the grid

MAZE_CONFIG = 'base'  # Possible values: 'base', 'increased_size', 'labyrinth', 'blockages'


# Define the get methods for the maze configuration
def get_cell_size_w():
    return GRID_WIDTH // GRID_SIZE_W


def get_cell_size_h():
    return GRID_HEIGHT // GRID_SIZE_H


def get_rewards():
    return REWARDS


def get_holes():
    return HOLES


def get_walls():
    return WALLS


def get_starting_position():
    return STARTING_POSITION


def get_grid_size_h():
    return GRID_SIZE_H


def get_grid_size_w():
    return GRID_SIZE_W


def get_empty_reward():
    return EMPTY_REWARD


def set_maze_config(maze_config):
    global MAZE_CONFIG, REWARDS, HOLES, WALLS, STARTING_POSITION, GRID_SIZE_H, GRID_SIZE_W, EMPTY_REWARD
    MAZE_CONFIG = maze_config
    if MAZE_CONFIG == 'base':
        REWARDS = base_config.REWARDS
        HOLES = base_config.HOLES
        WALLS = base_config.WALLS
        STARTING_POSITION = base_config.STARTING_POSITION
        GRID_SIZE_H = base_config.GRID_SIZE_H
        GRID_SIZE_W = base_config.GRID_SIZE_W
        EMPTY_REWARD = base_config.EMPTY_REWARD
    elif MAZE_CONFIG == 'increased_size':
        REWARDS = increased_size_config.REWARDS
        HOLES = increased_size_config.HOLES
        WALLS = increased_size_config.WALLS
        STARTING_POSITION = increased_size_config.STARTING_POSITION
        GRID_SIZE_H = increased_size_config.GRID_SIZE_H
        GRID_SIZE_W = increased_size_config.GRID_SIZE_W
        EMPTY_REWARD = increased_size_config.EMPTY_REWARD
    elif MAZE_CONFIG == 'labyrinth':
        REWARDS = labyrinth_config.REWARDS
        HOLES = labyrinth_config.HOLES
        WALLS = labyrinth_config.WALLS
        STARTING_POSITION = labyrinth_config.STARTING_POSITION
        GRID_SIZE_H = labyrinth_config.GRID_SIZE_H
        GRID_SIZE_W = labyrinth_config.GRID_SIZE_W
        EMPTY_REWARD = labyrinth_config.EMPTY_REWARD
    elif MAZE_CONFIG == 'blockages':
        REWARDS = blockages_config.REWARDS
        HOLES = blockages_config.HOLES
        WALLS = blockages_config.WALLS
        STARTING_POSITION = blockages_config.STARTING_POSITION
        GRID_SIZE_H = blockages_config.GRID_SIZE_H
        GRID_SIZE_W = blockages_config.GRID_SIZE_W
        EMPTY_REWARD = blockages_config.EMPTY_REWARD


# Call the function initially to set the default values
set_maze_config(MAZE_CONFIG)

# Define the possible actions and how they affect the position of the agent
ACTIONS = {
    'up': (0, -1),
    'right': (1, 0),
    'down': (0, 1),
    'left': (-1, 0)
}

# Define the discount factor
DISCOUNT_FACTOR = 0.99


# Define the transition model
def transition_model(a):
    a_index = list(ACTIONS.keys()).index(a)
    left_a = list(ACTIONS.keys())[(a_index - 1) % len(ACTIONS)]
    right_a = list(ACTIONS.keys())[(a_index + 1) % len(ACTIONS)]
    # Return the possible actions and their probabilities
    return {left_a: 0.1, a: 0.8, right_a: 0.1}


# Define the constants for the value iteration algorithm
R_MAX = 1  # Maximum reward
C = 0.1  # Constant for the tolerance
EPSILON = C * R_MAX  # Calculate the epsilon
TOLERANCE = EPSILON * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR
