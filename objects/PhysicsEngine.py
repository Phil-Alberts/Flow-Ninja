
from pygame.math import Vector2
from pygame.sprite import Group
from objects.Physics import Physics
from objects.SpriteWithPhysics import SpriteWithPhysics
import pygame

class PhysicsEngine:
  objects: Group = Group()
  default_gravity: Vector2

  def __init__(self, gravity_const: float = 100.0) -> None:
    self.default_gravity = Vector2(0, gravity_const)
    pass

  # def _determine_collision(self, i: SpriteWithPhysics, j: SpriteWithPhysics, dt: float):
  #   colliding = i.rect.colliderect(j.rect)
  #   if not colliding:
  #     return None

  # determines whether the polygons collide and returns the depth and normal axis
  def _intersect_polygons(self, verticesA: list[Vector2], verticesB: list[Vector2]) -> tuple[float, Vector2]:
    depth: float = None
    normal: Vector2 = None
    for vertList in [verticesA, verticesB]:
      for i in range(len(vertList)):
        va = vertList[i]
        vb = vertList[(i + 1) % len(vertList)]
        
        edge = vb - va
        axis = Vector2(-edge.y, edge.x)

        minA, maxA = self._project_vertices(verticesA, axis)
        minB, maxB = self._project_vertices(verticesB, axis)

        if minA >= maxB or minB >= maxA:
          return (0, None)
        
        axisDepth = min([maxB - minA, maxA - minB])
        if depth is None or axisDepth < depth:
          depth = axisDepth
          normal = axis
    # normalize depth and normal vector to be the correct depth in the right direction
    depth = depth / normal.magnitude()
    normal = normal.normalize()
    return (depth, normal)

  def _project_vertices(self, vertices: list[Vector2], axis: Vector2) -> tuple[float, float]:
    min: float = None
    max: float = None
    for vertex in vertices:
      proj = vertex.dot(axis)
      if min is None or proj < min:
        min = proj
      if max is None or proj > max:
        max = proj
    return (min, max)
  

  def register_object(self, object: SpriteWithPhysics):
    self.objects.add(object)
  
  def update_entities(self, dt: float, keys_pressed: pygame.key.ScancodeWrapper, key_events):
    # loop through objects and develop expected position
    # loop back through and do collision detection
    # loop through and publish events
    events = []
    sprites = self.objects.sprites()
    for obj in sprites:
      if obj.physics is None:
        continue

      forces: list[Vector2] = []
      forces.append(self.default_gravity * obj.physics.gravity_impact)
      obj.physics.update(dt, forces)

    # find any collisions
    num_calcs = len(sprites)
    for i in range(num_calcs):
      obj1: SpriteWithPhysics = sprites[0]

      for j in range(i + 1, num_calcs):
        obj2: SpriteWithPhysics = sprites[j]

        if obj1.physics is not None:
          # detect collision
          # collide = obj1.rect.colliderect(obj2.rect)
          dist, dir = self._intersect_polygons(
              obj1.rect.get_vertices(),
              obj2.rect.get_vertices()
            )
          
          # if we are some distance inside of the object (i.e. we have collided)
          if dist > 0:
            # emit the event so that objects are aware of collision
            events.append({ 'type': 'collision', 'actors': [obj1, obj2], 'intersect_depth': dist, 'direction': dir })
            # physics engine will handle collision logic here before the event is read by the objects

            if obj1.fixed:
              obj2.physics.pos += dir * dist
            elif obj2.fixed:
              obj1.physics.pos -= dir * dist
            else:
              # ratio = obj1.physics.mass / obj2.physics.mass
              obj1.physics.pos -= dir * dist / 2
              obj2.physics.pos += dir * dist / 2

    for obj in sprites:
      obj.update(events)
