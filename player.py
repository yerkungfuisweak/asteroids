import pygame
from circleshape import CircleShape
from constants import *

class Player(pygame.sprite.Sprite):  # Extending Sprite for group compatibility
    def __init__(self, x, y):
        super().__init__(self.containers)  # Automatically add to groups
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.position = pygame.Vector2(x, y)

        # Create a placeholder image and rect for compatibility with Group.draw()
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))  # Center rectangle
    
    def draw(self, screen):
        # Delegate drawing your custom triangular ship to this method
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)

        # Keep `rect.center` in sync with `position` for compatibility
        self.rect.center = self.position

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))