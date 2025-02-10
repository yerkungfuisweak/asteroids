import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    # game initialization code
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create the necessary groups
    updatable = pygame.sprite.Group()  # For all objects that update
    drawable = pygame.sprite.Group()   # For all objects that are drawn
    asteroids = pygame.sprite.Group()  # Specifically for asteroids

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Set the containers   
    Player.containers = (updatable, drawable)    # Set containers for Player
    Asteroid.containers = (asteroids, updatable, drawable)    # Set containers for Asteroid
    AsteroidField.containers = (updatable)     #set containers for asteroidfield
    
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player = Player(player_x, player_y)  # Create Player at the center
    
    # Creating a new object is what we call “instantiating a class.” The class AsteroidField is essentially a “blueprint” for 
    # creating asteroid fields in your game. When you create an instance of this class, you’re using the blueprint to generate one 
    # specific asteroid field—an object.
    # Initialization code:
    asteroid_field = AsteroidField()   # Create the AsteroidField object

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0)) 
        updatable.update(dt)
        for sprite in asteroids:
            if sprite.collision(player) == True:
                print("Game over!")
                exit()
        for sprite in drawable:
            sprite.draw(screen)  # Call each sprite's custom draw() method
        pygame.display.flip()


if __name__ == "__main__":
    main()