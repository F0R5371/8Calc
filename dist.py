import math

def dist(c1, c2):
    dif_x = c2[0] - c1[0]
    dif_y = c2[1] - c1[1]
    return math.sqrt(dif_x**2 + dif_y**2)

pos1 = input("Point 1?").split()
pos2 = input("Point 2?").split()

coord1 = map(float, pos1)
coord2 = map(float, pos2)

d = dist(tuple(coord1), tuple(coord2))

print(f"DISTANCE: {d}")