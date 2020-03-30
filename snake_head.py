import pygame
from snake_obj import Snake

class Snake_head(Snake):
    """A class representing the snake's head."""

    def __init__(self,sk_game):
        super().__init__(sk_game)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates the position of the snake."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.snake_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.snake_speed
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.snake_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.snake_speed

