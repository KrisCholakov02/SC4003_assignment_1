import random

import pygame
from config import *


# Define the Grid class to manage the grid
class Grid:
    def __init__(self, screen, rewards, holes, walls, start_pos):
        self.screen = screen
        self.rewards = rewards
        self.holes = holes
        self.walls = walls
        self.player_pos = start_pos
        self.font = pygame.font.SysFont(None, get_cell_size_h() // 3)
        self.player_icon = pygame.transform.scale(pygame.image.load('./assets/player_icon.png'), (get_cell_size_w(), get_cell_size_h()))
        self.score = 0

    # Getter method for the score
    def get_score(self):
        return self.score

    # Method to check if the next cell is a wall
    def is_wall(self, x, y):
        return (x, y) in self.walls

    def update_score(self):
        if self.player_pos in self.rewards:
            self.score += self.rewards[self.player_pos] # Increase the score if the new cell is a reward
        elif self.player_pos in self.holes:
            self.score += self.holes[self.player_pos]  # Decrease the score if the new cell is a hole
        else:
            self.score += get_empty_reward()

    # Method to move the player
    def move(self, direction):
        x, y = self.player_pos
        new_x, new_y = x, y

        # Generate a random number for the state transition
        rand_num = random.random()

        # Determine the direction of movement based on the state transition probabilities
        if rand_num < 0.8:  # Move in the intended direction with a probability of 0.8
            if direction == 'up' and y > 0:
                new_y -= 1
            elif direction == 'down' and y < get_grid_size_h() - 1:
                new_y += 1
            elif direction == 'left' and x > 0:
                new_x -= 1
            elif direction == 'right' and x < get_grid_size_w() - 1:
                new_x += 1
        elif rand_num < 0.9:  # Incorrect movement with a probability of 0.1
            print("Incorrect movement")
            if direction == 'up' or direction == 'down':
                if x < get_grid_size_w() - 1:
                    new_x += 1
            else:
                if y < get_grid_size_h() - 1:
                    new_y += 1
        else:  # Opposite incorrect movement with a probability of 0.1
            print("Incorrect movement")
            if direction == 'up' or direction == 'down':
                if x > 0:
                    new_x -= 1
            else:
                if y > 0:
                    new_y -= 1

        if not self.is_wall(new_x, new_y):
            self.player_pos = (new_x, new_y)
            self.update_score()  # Update the score after moving
        else:
            print("Can't move in that direction!")

    def draw(self):
        for x in range(0, GRID_WIDTH, get_cell_size_w()):
            for y in range(0, GRID_HEIGHT, get_cell_size_h()):
                rect = pygame.Rect(x, y, get_cell_size_w(), get_cell_size_h())
                cell_pos = (x // get_cell_size_w(), y // get_cell_size_h())

                # Draw the appropriate cell
                pygame.draw.rect(self.screen, self.get_cell_color(cell_pos), rect, 0)
                pygame.draw.rect(self.screen, BLACK, rect, LINE_WIDTH)

                # Add text if necessary
                self.draw_text(cell_pos, rect)

                # Draw the player icon at the starting position
                if cell_pos == self.player_pos:
                    self.screen.blit(self.player_icon, rect.topleft)

    def get_cell_color(self, pos):
        if pos in self.rewards:
            return GREEN
        elif pos in self.holes:
            return ORANGE
        elif pos in self.walls:
            return MEDIUM_GREY
        else:
            return WHITE

    def draw_text(self, pos, rect):
        if pos in self.rewards or pos in self.holes:
            text = str(self.rewards.get(pos, self.holes.get(pos)))
            if int(text) > 0:
                text = '+' + text
            label = self.font.render(text, True, BLACK)
            label_rect = label.get_rect(center=rect.center)
            self.screen.blit(label, label_rect)
        elif pos in self.walls:
            label = self.font.render("Wall", True, BLACK)
            label_rect = label.get_rect(center=rect.center)
            self.screen.blit(label, label_rect)