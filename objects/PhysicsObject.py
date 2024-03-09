from pygame.math import Vector2

class PhysicsObject:
    pos: Vector2
    d_pos: Vector2
    vel: Vector2
    d_vel: Vector2
    acc: Vector2
    d_acc: Vector2
    gravity_impact: float

    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), acc: Vector2 = Vector2(0, 0), gravity_impact = 1.0) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.gravity_impact = gravity_impact
    
    def update(self, dt: float, forces: list[Vector2]):
        for force in forces:
            self.vel += force * dt
        
        self.vel += self.acc * dt
        self.pos += self.vel * dt