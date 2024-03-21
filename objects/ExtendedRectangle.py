from pygame import Rect
from pygame.math import Vector2

class ExtendedRectangle(Rect):
    def __init__(self, rect: Rect):
        super().__init__(rect.left, rect.top, rect.width, rect.height)
    
    def get_vertices(self):
        return Vector2(self.topleft), Vector2(self.topright), Vector2(self.bottomright), Vector2(self.bottomleft)