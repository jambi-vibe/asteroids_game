# imports
from constants import *
from circleshape import *

# Creates Player class and inherits from CircleShape for hitbox
class Player(CircleShape):
    def __init__(self, x, y):

        super().__init__(x, y, PLAYER_RADIUS)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    rotation = 0

    # Draws player sprite as triangle
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
