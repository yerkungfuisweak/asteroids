import pygame
from constants import *
from player import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player = Player(player_x, player_y)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0)) 
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)  # Call each sprite's custom draw() method
        pygame.display.flip()

if __name__ == "__main__":
    main()