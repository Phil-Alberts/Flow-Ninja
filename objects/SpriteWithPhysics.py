from pygame import sprite, math, rect
from objects.Physics import Physics
from pygame.sprite import Group
from objects.ExtendedRectangle import ExtendedRectangle

class SpriteWithPhysics(sprite.Sprite):
  physics: Physics
  collision: bool = True
  fixed: bool = False
  rect: ExtendedRectangle

  def __init__(self, *groups: Group) -> None:
    super().__init__(*groups)

  def update(self, events):
    if self.physics is not None:
      self.rect.center = self.physics.pos