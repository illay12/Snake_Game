import pygame
from pygame.sprite import Sprite

class Snake(Sprite):
    """A class to manage the snake object."""
    def __init__(self,sk_game):
        super().__init__()
        self.screen = sk_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sk_game.settings
        self.stats = sk_game.stats

        #Set the diemnsions of the snake
        self.width,self.height = 50,50
        self.snake_color = (255,0,0)

        #Build the snake's rect object.
        self.rect = pygame.Rect(50, 350, self.width, self.height)

    def draw_Snake(self):
        """Draws the snake to the screen."""
        pygame.draw.rect(self.screen, self.snake_color,self.rect)
