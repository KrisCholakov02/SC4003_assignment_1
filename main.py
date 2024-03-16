import pygame
import pygame_gui
from grid import Grid
from config import *
from utils import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze")

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define the font
font = pygame.font.SysFont(None, CELL_SIZE_H // 3)

# Calculate the x-coordinate of the buttons
BUTTON_X = GRID_HEIGHT + 10  # 200 is the total width of the buttons, 10 is a margin
# Calculate the y-coordinate of the buttons
BUTTON_Y = 10

button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((BUTTON_X, BUTTON_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)),
                                       text='Button 1',
                                       manager=manager)
button2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((BUTTON_X + BUTTON_WIDTH + 20, BUTTON_Y), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    text='Capture',
    manager=manager)

# Update the y-coordinate for the next button
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

# Update the y-coordinate for the next button
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
grid = Grid(screen, REWARDS, HOLES, WALLS, STARTING_POSITION)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    print('Button 1 clicked')
                elif event.ui_element == button2:
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

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((255, 255, 255))

    # Draw the grid
    grid.draw()

    # Draw the score
    score_label = font.render(f'Score: {grid.get_score():.2f}', True, BLACK)
    screen.blit(score_label, (10, WINDOW_HEIGHT - 30))  # Adjust the position as needed

    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
