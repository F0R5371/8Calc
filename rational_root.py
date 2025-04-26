import math

def factors(num):
    fac = list()
    for i in range(num + 1):
        if num % (i + 1) == 0:
            fac.append(float(i + 1))
    
    return sorted(fac)

def possible_roots(a, b):
    roots = set(a + b)
    for i in a:
        for j in b:
            if j != 0:
                roots.add(i / j)

    return roots

def get_roots(poly, n, roots):

    rat_roots = set()
    neg_roots = set(map(lambda f : f * -1, roots))
    all_roots = roots.union(neg_roots)

    for root in all_roots:

        terms = list()
        for i in range(n):
            exp = n - (i + 1)
            terms.append(float(poly[i]) * root ** exp)
        
        if sum(terms) == 0:
            rat_roots.add(root)

    return rat_roots

poly = input("Equation?").split()
n = len(poly)

p = factors(abs(int(poly[-1])))
q = factors(abs(int(poly[0])))

possible = possible_roots(p, q)

roots = get_roots(poly, n, possible)

if len(roots) == 0:
    print("NO RATIONAL ROOTS")
else:
    print(f"ROOTS: {roots}")