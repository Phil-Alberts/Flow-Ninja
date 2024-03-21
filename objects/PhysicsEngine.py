from pygame.math import Vector2
from pygame.sprite import Group
from objects.SpriteWithPhysics import SpriteWithPhysics
import pygame

class PhysicsEngine:
  objects: Group = Group()
  default_gravity: Vector2

  def __init__(self, gravity_const: float = 100.0) -> None:
    self.default_gravity = Vector2(0, gravity_const)
    pass


  def register_object(self, object: SpriteWithPhysics):
    self.objects.add(object)
  
  def update_entities(self, dt: float, keys_pressed: pygame.key.ScancodeWrapper, key_events):
    # loop through objects and develop expected position
    #  record any events that should happen
    # loop through objects and publish events
    events = []
    sprites = self.objects.sprites()
    for obj in sprites:
      if obj.physics is None:
        continue

      forces: list[Vector2] = []
      forces.append(self.default_gravity)
      obj.physics.update(dt, forces)

    # find any collisions
    num_calcs = len(sprites)
    for i in range(num_calcs):
      obj1 = sprites[0]
      for j in range(i + 1, num_calcs):
        obj2 = sprites[j]

        if obj1.physics is not None:
          # detect collision
          collide = obj1.rect.colliderect(obj2.rect)
          if collide:
            # calculate angle of collision
            events.append({'type': 'collision', 'actors': [obj1, obj2]})
    
    for obj in sprites:
      obj.update(events)
