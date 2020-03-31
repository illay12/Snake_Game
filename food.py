import pygame


class Food:
    """A class representing the food."""

    def __init__(self, sk_game):
        self.screen = sk_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sk_game.settings

        # Set the dimensions of the food
        self.width, self.height = 50,50
        self.food_color = (0, 255, 0)

        # Build the snake's rect object.
        self.rect = pygame.Rect(0, 0, self.width,
                                self.height)


    def draw_food(self):
        """Draws the food to the screen"""
        self.screen.fill(self.food_color,self.rect)