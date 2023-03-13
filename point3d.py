from dataclasses import dataclass

@dataclass
class Coordinate3D:
    y: float
    z: float
    x: float = 0.0


point_yz = Coordinate3D(1.5,3)
print(point_yz)
