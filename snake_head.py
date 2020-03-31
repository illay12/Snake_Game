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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Updates the position of the snake."""
        if self.moving_right:
            self.x += self.settings.snake_speed
        elif self.moving_left:
            self.x -= self.settings.snake_speed
        elif self.moving_up:
            self.y -= self.settings.snake_speed
        elif self.moving_down:
            self.y += self.settings.snake_speed

        if self._check_snake_walls_collisions():
            self.rect.x = self.x
            self.rect.y = self.y

    def _check_snake_walls_collisions(self):
        """Checks if the snake hit any walls."""
        #Trebuie sa stochez undeva doar x si y snake_headului intai,verific folosind functia asta si deabea
        # apoi updatezi recturile.
        if self.x >= self.settings.screen_width or self.x < 0:
            self.settings.game_active = False
        elif self.y < 0 or self.y >= self.settings.screen_height:
            self.settings.game_active = False
        else:
            return True