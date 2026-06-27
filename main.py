# imports
import pygame
import sys
from logger import log_state
from logger import log_event
from shot import Shot
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

# main code block
def main():

    # initializes pygame and creates display
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #prints screen ratio info to console
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Creates clock and delta time var
    clock = pygame.time.Clock()
    dt = 0.0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # main event handler for game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        for aste in asteroids:
            if aste.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for aste in asteroids:
            for shot in shots:
                if shot.collides_with(aste):
                    log_event("asteroid_shot")
                    shot.kill()
                    aste.split()
        pygame.display.flip()

if __name__ == "__main__":
    main()
