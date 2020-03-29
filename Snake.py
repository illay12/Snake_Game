import sys
from random import randint

import pygame
from settings import Settings
from snake_obj import Snake
from food import Food

class SnakeGame:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.FPS = 15

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Snake")

        self.snake = Snake(self)
        self.food = Food(self)
        self._create_food()

    def run_game(self):
        """Start the main loop."""
        while True:
            self.clock.tick(self.FPS)
            self._check_events()
            self.snake.update()
            self._check_snake_food_collision()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouseclicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self,event):
        """Checks for key presses."""
        if event.key == pygame.K_RIGHT:
            #Move the snake to the right
            self._reset_direction()
            self.snake.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the snake left
            self._reset_direction()
            self.snake.moving_left = True
        elif event.key == pygame.K_DOWN:
            #Move the snake down
            self._reset_direction()
            self.snake.moving_down = True
        elif event.key == pygame.K_UP:
            #Move the snake up.
            self._reset_direction()
            self.snake.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_food(self):
        """Updates the food's image on the screen."""
        self._check_snake_food_collision()

    def _check_snake_food_collision(self):
        if self.snake.rect.x == self.food.rect.x and self.snake.rect.y == self.food.rect.y:
            self._create_food()

    def _create_food(self):
        """Creates a new food object if necessary"""
        #Find the amount of spaces available
        self.number_lines = self.settings.screen_width // self.settings.scale - 1
        self.number_rows = self.settings.screen_height // self.settings.scale - 1

        self.food.rect.x = randint(1, self.number_lines) * self.settings.scale
        self.food.rect.y = randint(1, self.number_rows) * self.settings.scale

    def _reset_direction(self):
        """Resets the movement."""
        self.snake.moving_right = False
        self.snake.moving_left = False
        self.snake.moving_up = False
        self.snake.moving_down = False


    def _update_screen(self):
        """Update images on the screen and flip the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.snake.draw_Snake()
        self.food.draw_food()

        pygame.display.flip()


if __name__ == '__main__':
    #Make an instance of the game and run it.
    sk = SnakeGame()
    sk.run_game()