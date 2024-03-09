from vector import Vector

class PhysicsObject:
    pos: Vector
    vel: Vector
    acc: Vector
    gravity_impact: float

    def __init__(self, pos: Vector, vel: Vector, acc: Vector, gravity_impact = 1.0) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.gravity_impact = gravity_impact
    
    def update(self, dt: float, gravity: Vector):
        self.vel += gravity * self.gravity_impact * dt
        self.vel += self.acc * dt
        self.pos += self.vel * dt