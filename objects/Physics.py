from pygame.math import Vector2

class Physics:
    pos: Vector2
    vel: Vector2
    acc: Vector2
    prev_pos: Vector2 = Vector2(0, 0)
    prev_vel: Vector2 = Vector2(0, 0)
    prev_acc: Vector2 = Vector2(0, 0)
    mass: float
    gravity_impact: float

    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), acc: Vector2 = Vector2(0, 0), mass=1, gravity_impact = 1.0) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.mass = mass
        self.gravity_impact = gravity_impact
    
    def get_values(self) -> tuple[Vector2, Vector2, Vector2]:
        return (self.pos, self.vel, self.acc)

    def update_values(self, pos: Vector2, vel: Vector2, acc: Vector2):
        pass

    def set_to_previous(self):
        self.pos = self.prev_pos
        self.vel = self.prev_vel
        self.acc = self.prev_acc

    def update(self, dt: float, forces: list[Vector2] = []):
        # just stop the objects when they collide
        self.prev_pos = Vector2(self.pos)
        self.prev_vel = Vector2(self.vel)
        self.prev_acc = Vector2(self.acc)
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
