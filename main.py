import pygame
import pygame_gui
from grid import Grid
from config import *
from utils import *

# Initialize pygame
pygame.init()

# Initialize the pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze")  # Set the title of the window

# Initialize the pygame_gui manager
manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define the font
font = pygame.font.SysFont(None, get_cell_size_h() // 3)

# Calculate the x-coordinate of the buttons
BUTTON_X = GRID_WIDTH + 10  # 10 is the margin
# Calculate the y-coordinate of the buttons
BUTTON_Y = 10  # 10 is the margin

# Add a button to capture the window
capture_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X, BUTTON_Y), (2 * BUTTON_WIDTH + 20, BUTTON_HEIGHT)),
    text='Capture Window',
    manager=manager)

# Update the y-coordinate for the next buttons
BUTTON_Y += WINDOW_HEIGHT - 50 - 3 * BUTTON_HEIGHT - 10

# Add arrow buttons
button_up = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X + BUTTON_WIDTH // 2 + 10, BUTTON_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    text='Up',
    manager=manager)
button_down = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X + BUTTON_WIDTH // 2 + 10, BUTTON_Y + 2 * BUTTON_HEIGHT),
                              (BUTTON_WIDTH, BUTTON_HEIGHT)),
    text='Down',
    manager=manager)

# Update the y-coordinate for the next buttons
BUTTON_Y += BUTTON_HEIGHT

button_left = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X, BUTTON_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    text='Left',
    manager=manager)
button_right = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X + BUTTON_WIDTH + 20, BUTTON_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    text='Right',
    manager=manager)

# Initialize grid
grid = Grid(screen, get_rewards(), get_holes(), get_walls(), get_starting_position())

# Initialize the clock
clock = pygame.time.Clock()
# Set the running flag to True
is_running = True

# Main loop
while is_running:
    # Update the time delta
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Process the button events
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == capture_button:
                    print('Capture Window')
                    capture_window(screen)
                elif event.ui_element == button_up:
                    grid.move('up')
                elif event.ui_element == button_down:
                    grid.move('down')
                elif event.ui_element == button_left:
                    grid.move('left')
                elif event.ui_element == button_right:
                    grid.move('right')

        # Process the pygame_gui events
        manager.process_events(event)

    # Update the pygame_gui manager
    manager.update(time_delta)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    grid.draw()

    # Draw the score
    score_label = font.render(f'Score: {grid.get_score():.2f}', True, BLACK)
    screen.blit(score_label, (10, WINDOW_HEIGHT - 30))  # Adjust the position as needed

    # Draw the pygame_gui manager
    manager.draw_ui(screen)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()