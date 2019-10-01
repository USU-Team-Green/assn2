import math
import base64
import sympy
import os

BYTE_SIZE=256
BLOCK_SIZE=16

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
    p, q = sympy.nextprime(int.from_bytes(os.urandom(BLOCK_SIZE + 1), byteorder='big')), sympy.nextprime(int.from_bytes(os.urandom(BLOCK_SIZE + 1), byteorder='big'))
    n = p * q
    lambda_n = lcm(p - 1, q - 1)
    e = 65537
    d = inverse(e, lambda_n)
    return str(n) + "$" + str(e), str(d)

def get_blocks(m):
    m = m.encode('ascii')
    blocks = []
    for blockStart in range(0, len(m), BLOCK_SIZE):
        block = 0
        for i in range(blockStart, blockStart + BLOCK_SIZE):
            if i < len(m):
                block += m[i] * BYTE_SIZE ** (i % BLOCK_SIZE)
            else:
                block += 32 * BYTE_SIZE ** (i % BLOCK_SIZE)
        blocks.append(block)
    return blocks

def encrypt(m, n, e):
    blocks = get_blocks(m)
    return ','.join([str(pow(block, e, n)) for block in blocks])

def get_text(blocks):
    message = []
    for block in blocks:
        blockM = []
        for i in range(BLOCK_SIZE - 1, -1, -1):
            asciiNum = block // (BYTE_SIZE ** i)
            block = block % (BYTE_SIZE ** i)
            print(asciiNum)
            blockM.insert(0, chr(asciiNum))
        message.extend(blockM)
    return "".join(message).strip()

def decrypt(c, n, d):
    decryptedBlocks = [pow(int(charNum), d, n) for charNum in c.split(',')]
    return get_text(decryptedBlocks)


def test_key_gen():
    public, private = generate_keys()
    n, e = public.split('$')
    n = int(n)
    e = int(e)
    d = int(private)
    m = 1234
    assert m == pow(pow(m, e, n), d, n)

def test_encrypt_decrypt():
    public, private = generate_keys()
    n, e = public.split('$')
    n = int(n)
    e = int(e)
    d = int(private)
    m = 'hello world'
    print(decrypt(encrypt(m, n, e), d, e))

    
