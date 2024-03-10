from pygame.math import Vector2

class PhysicsObject:
    pos: Vector2
    vel: Vector2
    acc: Vector2
    gravity_impact: float

    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), acc: Vector2 = Vector2(0, 0), gravity_impact = 1.0) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.gravity_impact = gravity_impact
    
    def update(self, dt: float, accels: list[Vector2]):
        acc_sum = Vector2()
        for acc in accels:
            acc_sum += acc
        d_pos = self.vel * dt
        d_vel = self.acc * dt
        d_acc = acc_sum - self.acc

        self.acc = acc_sum
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        return (d_pos, d_vel, d_acc)
        # return (self.acc, self.vel, self.pos)
        # print(self.pos)
        # for force in forces:
        #     self.vel += force * dt
        
