import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")        
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-abs(angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster_a = Asteroid(self.position[0], self.position[1], new_radius)
        aster_b = Asteroid(self.position[0], self.position[1], new_radius)
        aster_a.velocity = vec1 * 1.2
        aster_b.velocity = vec2 * 1.2
