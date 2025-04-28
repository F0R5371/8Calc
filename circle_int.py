import math

def eval_circle(cen, r, var):

    ints = list()
    c = r**2 - center[1 - var]**2

    # If c is positive
    if c >= 0:
        sqrt = math.sqrt(c)
        var1 = sqrt + (-1 * cen[var])
        var2 = -sqrt + (-1 * cen[var])

        if var == 0:
            ints.append((var1, 0))
            ints.append((var2, 0))
        else:
            ints.append((0, var1))
            ints.append((0, var2))

    return ints

center = list(map(int, input("Center?").split()))
rad = int(input("Radius?"))

# 0 indicates x-intercepts, 1 indicates y-intercepts
ints = eval_circle(center, rad, 0) + eval_circle(center, rad, 1)
print(f"Intercepts: {ints}")



