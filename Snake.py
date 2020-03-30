import sys
from random import randint

import pygame

from settings import Settings
from snake_obj import Snake
from food import Food
from snake_head import Snake_head as SnakeHead

class SnakeGame:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.FPS = 10

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Snake")

        self.pozitii = {}
        self.pozitii['x'] = []
        self.pozitii['y'] = []

        self.snake = pygame.sprite.Group()
        self.food = Food(self)
        self._create_food()

        self.snake_head = SnakeHead(self)
        self._add_bit_position(self.snake_head)

    def run_game(self):
        """Start the main loop."""
        while True:
            self.clock.tick(self.FPS)
            self._check_events()
            self._update_food()
            self._update_snake()
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
            self.snake_head.moving_right = True
            print("yes")
        elif event.key == pygame.K_LEFT:
            #Move the snake left
            self._reset_direction()
            self.snake_head.moving_left = True
        elif event.key == pygame.K_DOWN:
            #Move the snake down
            self._reset_direction()
            self.snake_head.moving_down = True
        elif event.key == pygame.K_UP:
            #Move the snake up.
            self._reset_direction()
            self.snake_head.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_food(self):
        """Updates the food's image on the screen."""
        self._check_snake_food_collision()

    def _update_snake(self):
        """Updates the snake on the screen"""
        self.snake_head.update()
        self._update_snake_bits_positions()
        self._store_snake_head_pos()
        self.snake.update()

    def _store_snake_head_pos(self):
        """Stores the position of the snake's head after all bits have been updated."""
        self.pozitii['x'][0] = self.snake_head.rect.x
        self.pozitii['y'][0] = self.snake_head.rect.y


    def _update_snake_bits_positions(self):
        """Updates the position of all snake bits."""
        for snake_bit_count in range(len(self.snake),0,-1):
            self.pozitii['x'][snake_bit_count] = self.pozitii['x'][snake_bit_count-1]
            self.pozitii['y'][snake_bit_count] = self.pozitii['y'][snake_bit_count-1]
        i=0
        for snake_bit in self.snake:
            snake_bit.rect.x = self.pozitii['x'][i]
            snake_bit.rect.y = self.pozitii['y'][i]
            i+=1
        print(self.pozitii['x'])
        print(self.pozitii['y'])

    def _check_snake_food_collision(self):
        if self.snake_head.rect.x == self.food.rect.x and self.snake_head.rect.y == self.food.rect.y:
            self._create_snake_bit()
            self._create_food()

    def _create_snake_bit(self):
        """Makes the snake longer when food is eaten."""
        snake_bit = Snake(self)
        snake_bit.rect.x = self.food.rect.x
        snake_bit.rect.y = self.food.rect.y
        self.snake.add(snake_bit)
        self._add_bit_position(snake_bit)

    def _add_bit_position(self,snake_bit):
        """Adds a new bit when food is eaten."""
        self.pozitii['x'].append(snake_bit.rect.x)
        self.pozitii['y'].append(snake_bit.rect.y)


    def _create_food(self):
        """Creates a new food object if necessary"""
        #Find the amount of spaces available
        self.number_lines = self.settings.screen_width // self.settings.scale - 1
        self.number_rows = self.settings.screen_height // self.settings.scale - 1

        self.food.rect.x = randint(1, self.number_lines) * self.settings.scale
        self.food.rect.y = randint(1, self.number_rows) * self.settings.scale

    def _reset_direction(self):
        """Resets the movement."""
        self.snake_head.moving_right = False
        self.snake_head.moving_left = False
        self.snake_head.moving_up = False
        self.snake_head.moving_down = False


    def _update_screen(self):
        """Update images on the screen and flip the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.snake_head.draw_Snake()
        for snake_bit in self.snake.sprites():
            snake_bit.draw_Snake()
        self.food.draw_food()

        pygame.display.flip()


if __name__ == '__main__':
    #Make an instance of the game and run it.
    sk = SnakeGame()
    sk.run_game()