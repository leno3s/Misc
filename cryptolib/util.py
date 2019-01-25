import secrets

def gcd(x, y):
    # euclidian algorithm
    if y == 0:
        return x
    return gcd(y, x%y)

def lcm(x, y):
    g, _, _ = ex_gcd(x, y)
    return x * y // g

def ex_gcd(x, y):
    # extended euclidian algorithm
    # x: gcd
    # a0, b0: solution
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while y:
        q, x, y = x // y, y, x % y
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    return x, a0, b0

def is_prime(n, k=30):
    # Miller-Rabin method
    if n == 2 : return True
    if n == 1 or n&1 == 0 : return False
    n = abs(n)
    d = (n-1)
    while d&1 == 0:
        d >>= 1
    for i in range(k):
        a = secrets.SystemRandom().randint(2, n-1)
        t = d
        y = pow(a, t, n)
        while t != n-1 and y != 1 and y != n-1:
            y = pow(y, 2, n)
            t <<= 1
        if y != n-1 and t&1 == 0:
            return False
    return True

def totient_from_two_primes(p, q):
    # Camichel`s theorem
    return lcm(p-1, q-1)

def generate_prime(bits=1024):
    while True:
        p = secrets.randbits(bits) | ((1<<(bits-1))+1)
        if is_prime(p):
            return p

def randint(length):
    return secrets.randbelow(length)

