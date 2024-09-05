import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius <= ASTEROID_MIN_RADIUS:
            return
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        random_angle = random.uniform(20, 50)
        new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2