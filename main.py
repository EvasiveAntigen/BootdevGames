#Update the game loop to use the new groups instead of the Player object directly.
#Call the .update() method on the "updatable" group.
#Loop over all "drawables" and .draw() them individually.import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame


def main():
	pygame.init()
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt : float = 0.0
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
	asteroid_field = AsteroidField()
	while True:
		log_state()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		dt = clock.tick(60) / 1000
		updatable.update(dt)
		screen.fill("black")
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
if __name__ == "__main__":
	main()
