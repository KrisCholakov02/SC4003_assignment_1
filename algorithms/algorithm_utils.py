from config import *
import pygame
from utils import *


# Function to check if the state is a wall or out of bounds
def is_wall(s):
    return s in get_walls() or s[0] < 0 or s[0] >= get_grid_size_w() or s[1] < 0 or s[1] >= get_grid_size_h()


# Function to calculate the utility of the next state based on the current state and action
def next_state_utility(pi_env, s, a):
    # Check if the current state is a wall
    if s in get_walls():
        return pi_env[s[1]][s[0]]

    # Calculate the next state based on the action
    new_x, new_y = s
    new_x += ACTIONS[a][0]
    new_y += ACTIONS[a][1]

    # Check if the next state is a wall or out of bounds
    if is_wall((new_x, new_y)):
        # Return the utility of the current state
        return pi_env[s[1]][s[0]]
    else:
        # Return the utility of the next state
        return pi_env[new_y][new_x]


# Function to calculate the expected utility of taking action 'a' in state 's'
# Expected utility for state s and action a: EU(s, a) = Σ_s' P(s' | s, a) * U_i(s')
def expected_utility(vi_env, s, a):
    # Initialize the expected utility to 0
    exp_utility = 0
    # Loop through all possible next states (according to the transition model) and calculate the expected utility
    for action, prob in transition_model(a).items():
        exp_utility += prob * next_state_utility(vi_env, s, action)
    return exp_utility


# Function to draw the action arrows on the grid (using this symbols ←, →, ↑, ↓)
def draw_action(screen, action, x, y):
    # Define the arrow image for each action
    arrow_img = pygame.image.load(get_path() + '/assets/' + action + '-arrow.png')
    arrow_img = pygame.transform.scale(arrow_img, (get_cell_size_w() // 2, get_cell_size_h() // 2))
    screen.blit(arrow_img, (x * get_cell_size_w() + get_cell_size_w() // 4, y * get_cell_size_h() + get_cell_size_h() // 4))


# Function to draw text on the grid
def draw_text(screen, text, x, y):
    # Define the font and size
    font = pygame.font.Font(None, get_cell_size_h() // 3)

    # Define the label rectangle
    rect = pygame.Rect(x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h())

    # Render the text label with the text centered on the cell
    label = font.render(text, True, BLACK)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


# Function to visualize the environment
def visualize_env(image_name):
    # Initialize the visualization
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(WHITE)
    # Loop through all the states in the environment
    for y in range(get_grid_size_h()):
        for x in range(get_grid_size_w()):
            # Define the color of the current state based on the utility
            color = get_cell_color((x, y))
            # Draw a rectangle for the current state
            pygame.draw.rect(screen, color, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()))
            # Draw the grid lines
            pygame.draw.rect(screen, BLACK, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()), LINE_WIDTH)
            if (x, y) not in get_walls():
                # Define the text for the current state
                if (x, y) in get_rewards():
                    text_content = str(get_rewards()[(x, y)])
                elif (x, y) in get_holes():
                    text_content = str(get_holes()[(x, y)])
                elif (x, y) in get_walls():
                    text_content = 'Wall'
                else:
                    text_content = ''
                draw_text(screen, text_content, x, y)
    # Update the display
    pygame.display.flip()

    # Save the visualization
    capture_window(screen, image_name, 0, 0, GRID_WIDTH, GRID_HEIGHT)

    # Quit the visualization
    pygame.quit()

# Function to visualize the policy
def visualize_policy(policy, image_name):
    # Initialize the visualization
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Value Iteration')
    screen.fill(WHITE)
    # Loop through all the states in the environment
    for y in range(get_grid_size_h()):
        for x in range(get_grid_size_w()):
            # Define the color of the current state based on the utility
            color = get_cell_color((x, y))
            # Draw a rectangle for the current state
            pygame.draw.rect(screen, color, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()))
            # Draw the grid lines
            pygame.draw.rect(screen, BLACK, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()), LINE_WIDTH)
            # Check if the current state is not a wall
            if (x, y) not in get_walls():
                # Get the optimal action for the current state
                action = policy[y][x]
                # Draw the optimal action on the screen
                draw_action(screen, action, x, y)
    # Update the display
    pygame.display.flip()

    # Save the visualization
    capture_window(screen, image_name, 0, 0, GRID_WIDTH, GRID_HEIGHT)

    # Quit the visualization
    pygame.quit()


# Function to visualize the utility values
def visualize_utility(env, image_name):
    # Initialize the visualization
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Value Iteration')
    screen.fill(WHITE)
    # Loop through all the states in the environment
    for y in range(get_grid_size_h()):
        for x in range(get_grid_size_w()):
            # Define the color of the current state based on the utility
            color = get_cell_color((x, y))
            # Draw a rectangle for the current state
            pygame.draw.rect(screen, color, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()))
            # Draw the grid lines
            pygame.draw.rect(screen, BLACK, (x * get_cell_size_w(), y * get_cell_size_h(), get_cell_size_w(), get_cell_size_h()), LINE_WIDTH)
            if (x, y) not in get_walls():
                # Add the utility value to the visualization
                draw_text(screen, f'{env[y][x]:.2f}', x, y)
    # Update the display
    pygame.display.flip()

    # Save the visualization
    capture_window(screen, image_name, 0, 0, GRID_WIDTH, GRID_HEIGHT)

    # Quit the visualization
    pygame.quit()
