from math import sin, pi # importacion selectiva

print(sin(pi/2))

pi = 3.14 #redefinir pi y por ende sin

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))