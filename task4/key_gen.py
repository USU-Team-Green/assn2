import math
import base64
import sympy
import os

def lcm(a, b):
    return a * b // math.gcd(a, b)

def inverse(x, m): # for getting modular inverse (d)
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m
    else:
        print('something went wrong')


def generate_keys():
    p, q = sympy.nextprime(int.from_bytes(os.urandom(15), byteorder='big')), sympy.nextprime(int.from_bytes(os.urandom(15), byteorder='big'))
    n = p * q
    lambda_n = lcm(p - 1, q - 1)
    e = 65537
    d = inverse(e, lambda_n)
    return str(n) + "$" + str(e), str(d)
