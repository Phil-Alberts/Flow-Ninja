from pygame import sprite, math, rect
from objects.Physics import Physics
from pygame.sprite import Group

class SpriteWithPhysics(sprite.Sprite):
  physics: Physics
  rect: rect.Rect

  def __init__(self, *groups: Group) -> None:
    super().__init__(*groups)

  def update(self, pos: math.Vector2, events):
    self.rect.move_ip(pos.x, pos.y)