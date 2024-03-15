from pygame.math import Vector2

class Physics:
    pos: Vector2
    vel: Vector2
    acc: Vector2
    mass: float
    gravity_impact: float

    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), acc: Vector2 = Vector2(0, 0), mass=1, gravity_impact = 1.0) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.mass = mass
        self.gravity_impact = gravity_impact
    
    def update(self, dt: float, forces: list[Vector2] = []):
        acc_sum = Vector2()
        for force in forces:
            acc_sum += force / self.mass
        d_pos = self.vel * dt
        d_vel = self.acc * dt
        d_acc = acc_sum - self.acc

        self.acc = acc_sum
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        return (d_pos, d_vel, d_acc)
