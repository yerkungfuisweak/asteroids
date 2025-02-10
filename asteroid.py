import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass x, y, radius up to CircleShape
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroid_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(-angle) * 1.2

        # Create the new asteroid objects
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign the velocities to the new asteroids
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2

        # Add them to the group
        asteroid_group.add(asteroid1, asteroid2)
