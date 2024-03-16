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
        self.font = pygame.font.SysFont(None, CELL_SIZE_H // 3)
        self.player_icon = pygame.transform.scale(pygame.image.load('./assets/player_icon.png'), (CELL_SIZE_W, CELL_SIZE_H))
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
            self.score += EMPTY_REWARD

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
            elif direction == 'down' and y < GRID_SIZE_H - 1:
                new_y += 1
            elif direction == 'left' and x > 0:
                new_x -= 1
            elif direction == 'right' and x < GRID_SIZE_W - 1:
                new_x += 1
        elif rand_num < 0.9:  # Incorrect movement with a probability of 0.1
            print("Incorrect movement")
            if direction == 'up' or direction == 'down':
                if x < GRID_SIZE_W - 1:
                    new_x += 1
            else:
                if y < GRID_SIZE_H - 1:
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
        for x in range(0, GRID_WIDTH, CELL_SIZE_W):
            for y in range(0, GRID_HEIGHT, CELL_SIZE_H):
                rect = pygame.Rect(x, y, CELL_SIZE_W, CELL_SIZE_H)
                cell_pos = (x // CELL_SIZE_W, y // CELL_SIZE_H)

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