import util
import codecs

class RSA:
    def __init__(
            s,
            public_exponent = 0x1001,    # e
            public_modulus = None,         # n
            secret_exponent = None,      # d
            p = None,              # p
            q = None,              # q
            totient_n = None        # φ(n)
            ):
        s._e = public_exponent
        s._d = secret_exponent
        s._p = p
        s._q = q
        s._n = public_modulus or p * q or None
        s._totient_n = totient_n or util.totient_from_two_primes(s._p, s._q) or None

    def encrypt(s, plaintext):
        if s._e is None or s._n is None:
            raise Exception
        return pow(plaintext, s._e, s._n)

    def decrypt(s, ciphertext):
        if s._n is None:
            raise Exception
        if s._d is None:
            s.generate_secret_key()
        return pow(ciphertext, s._d, s._n)

    def decrypt_hex(s,ciphertext, encoding='hex_codec'):
        m = s.decrypt(ciphertext)
        return codecs.decode(b'%0512x'%m, encoding)

    def generate_secret_key(s):
        if s._e is None or s._totient_n is None:
            raise Exception
        gcd, d, k = util.ex_gcd(s._e, s._totient_n)
        s._d = d % s._totient_n
        return s._d

