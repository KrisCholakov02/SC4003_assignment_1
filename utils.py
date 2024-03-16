import pygame
from config import *
import time


# Function to get the current path
def get_path():
    import os
    return os.path.dirname(os.path.abspath(__file__))


# Function to check if system directory exists otherwise create it
def check_directory(name):
    import os
    if not os.path.exists(name):
        os.makedirs(name)


# Function to capture the window
def capture_window(screen, name='', start_x=0, start_y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
    rect = pygame.Rect(start_x, start_y, width, height)
    surface = screen.subsurface(rect)
    if name == '':
        # Generate name based on the current time
        name = time.strftime("%Y%m%d-%H%M%S")
    check_directory('window_capture')
    pygame.image.save(surface, get_path() + '/window_capture/' + name + '.png')


# Function to return a copy of an environment
def copy_env(env):
    return [[env[y][x] for x in range(GRID_SIZE_W)] for y in range(GRID_SIZE_H)]
