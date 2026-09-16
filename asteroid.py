from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):

        def __init__(self, x: float, y: float, radius: float) -> None:
                super().__init__(x, y, radius)

        def draw(self, screen):
                pygame.draw.circle(screen, "white",self.position,self.radius, LINE_WIDTH )

        def update(self, dt):
                self.position += (self.velocity * dt)

        def split(self):
                self.kill()
                if self.radius <= ASTEROID_MIN_RADIUS:
                        return
                else:
                        log_event("asteroid_split")
                        angle = random.uniform(20, 50)
                        rotation_one = self.velocity.rotate(angle)
                        rotation_two = self.velocity.rotate(-angle)
                        new_radius = self.radius - ASTEROID_MIN_RADIUS
                        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                        new_asteroidV2 = Asteroid(self.position.x, self.position.y, new_radius)
                        new_asteroid.velocity = rotation_one * 1.2
                        new_asteroidV2.velocity = rotation_two * 1.2
