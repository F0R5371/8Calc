import math

# Probability operators
def and_prob(a, b):
    return a * b

def or_prob(a, b):
    return a + b - and_prob(a, b)

# Conditional prob
def given_prob(a, b):
    return and_prob(a, b) / b

def bayes_prob(b, a):
    return (b * and_prob(a, b)) / a

# For other functions
def factorial(num):
    fac = 1
    for i in range(num, 0, -1):
        fac *= i

    return fac

# Order does not matter
def combination(n, r):
    num = factorial(n)
    denom = factorial(r) * factorial(n - r)

    return float(num) / denom

# Order does matter, with repetition
def combination_rep(n, r):
    num = factorial(r + n - 1)
    denom = factorial(r) * factorial(n - 1)
    return float(num) / denom

# Order does matter, with repetition
# n = types, r = how many chosen
def permutation_rep(n, r):
    return n**r

# Order does matter, without repetition
def permutation(n, r):
    num = factorial(n)
    denom = factorial(n - r)
    return float(num) / denom

# Binomial distribution
def binom_pdf(trials, x, p):
    term1 = combination(trials, x)
    term2 = p**x
    term3 = (1 - p)**(trials - x)

    return term1 * term2 * term3

def binom_cdf(trials, x, p):
    cdf = 0
    for i in range(x + 1):
        cdf += binom_pdf(trials, i, p)

    return cdf

def binom_mean(trials, p):
    return trials * p

def binom_std(trials, p):
    return math.sqrt(trials * p * (1 - p))

# Geometric distribution
def geomet_pdf(f, p):
    return p * (1 - p)**(f - 1)

def geomet_cdf(f, p):
    cdf = 0
    for i in range(f):
        cdf += geomet_pdf(i + 1, p)

    return cdf

def geomet_mean(p):
    return 1 / p

def geomet_std(p):
    return math.sqrt((1 - p) / p**2)

print(geomet_cdf(4, 1/6))