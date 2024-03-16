from pygame.math import Vector2
from objects.Physics import Physics
from objects.SpriteWithPhysics import SpriteWithPhysics
import pygame

class PhysicsEngine:
  objects: list[SpriteWithPhysics] = []

  def __init__(self) -> None:
    pass

  def register_object(self, object: SpriteWithPhysics):
    self.objects.append(object)
  
  def update_entities(self, dt: float, keys_pressed: pygame.key.ScancodeWrapper, key_events):
    # loop through objects and develop expected position
    #  record any events that should happen
    # loop through objects and publish events
    events = []
    for obj in self.objects:
      if obj.physics is None:
        continue

      forces: list[Vector2] = []
      forces.append(Vector2(0, 1000))
      obj.physics.update(dt, forces)
      obj.update(events)
      print('updating object')
