import pygame

class Snake():
    """A class to manage the snake object."""
    def __init__(self,sk_game):
        self.screen = sk_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sk_game.settings

        #Set the diemnsions of the snake
        self.width,self.height = 25, 25
        self.snake_color = (255,0,0)

        #Build the snake's rect object.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

        #Movement flags
        self.moving_right = True
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
        print(self.rect.x)
        print(self.rect.y)



    def draw_Snake(self):
        """Draws the snake to the screen."""
        self.screen.fill(self.snake_color,self.rect)
