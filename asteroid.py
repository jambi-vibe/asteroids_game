from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            
            smaller_asteroid_1_velocity = self.velocity.rotate(angle)
            smaller_asteroid_2_velocity = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            smaller_asteroid_1.velocity = smaller_asteroid_1_velocity * 1.2
            smaller_asteroid_2.velocity = smaller_asteroid_2_velocity * 1.2

