from pygame.math import Vector2
from objects.Physics import Physics
from objects.SpriteWithPhysics import SpriteWithPhysics
import pygame

class PhysicsEngine:
  objects: list[SpriteWithPhysics] = []
  default_gravity: float

  def __init__(self, default_gravity = 100.0) -> None:
    self.default_gravity = default_gravity
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
      forces.append(Vector2(0, self.default_gravity))
      obj.physics.update(dt, forces)
      obj.update(events)
