import pygame

# every object has this shape, even the player
# this way it's easier to detect collisions, which would be trickier if it was a triangle
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if (hasattr(self, "containers")):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    # methods that will be overdrawn 
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass