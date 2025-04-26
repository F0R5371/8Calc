import math

def quadratic(a, b, c):

    if a == 0:
        return None

    determ = math.sqrt(b**2 - (4 * a * c))
    sol1 = (-b + determ) / (2 * a)
    sol2 = (-b - determ) / (2 * a)

    return (sol1, sol2)

terms = input("Equation?").split()
eq = map(float, terms)

sol = quadratic(*eq)
if sol:
    print(f"SOLUTION: {sol}")
else:
    print("NO SOLUTION")