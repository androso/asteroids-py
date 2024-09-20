import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for player in updatable:
            player.update(dt)

        for asteroid in asteroids:
            # if (asteroid.check_collision(player1)):
            if (player1.check_collision(asteroid)):
                print("Game Over!")
                sys.exit()
            
        screen.fill("black")

        for player in drawable:
            player.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(60)
        dt = delta_time / 1000

if __name__ == "__main__":
    main()