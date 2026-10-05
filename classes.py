from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
p1= Point(1.0, 2.0)
print(p1)