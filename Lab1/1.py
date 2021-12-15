import math

R = float(input("R: "))
r = float(input("r: "))
H = float(input("H: "))

d = R - r

L = math.sqrt(H * H + d * d)

S = math.pi * (L * R + L * r + R * R + r * r)

print('S: {:.3f}'.format(S))