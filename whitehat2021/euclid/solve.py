#!/usr/local/bin/sage

from sage.all import *
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b

with open('flag_enc', 'rb') as f:
    c = b2l(f.read())

with open('output', 'r') as f:
    data = list(map(lambda x: int(x, 16), f.readlines()))

# Fabricate matrix
t = len(data)
lattice = Matrix(ZZ, t, t)

for i in range(t - 1):
    lattice[i, i] = 1
    lattice[i, -1] = data[i]

lattice[-1, -1] = data[-1]

lattice = lattice.LLL()

row, col = lattice.nrows(), lattice.ncols()
M = Matrix(ZZ, row - 1, col)
for i in range(row - 1):
    temp = 0
    for j in range(col - 1):
        M[i, j] = lattice[i, j]
        temp += M[i, j] * data[j]
    M[i, -1] = (lattice[i, -1] - temp) // data[-1]

v = vector([lattice[i, -1] for i in range(row - 1)])
es = M.solve_right(v)

"""
We don't need to consider homogeneous solution.
"""

# Recovered (n*k) (which is technically (p*k))
nk = [data[i] - es[i] for i in range(col)]

# p recovered
pr = int(gcd(nk))
assert is_prime(pr)

Z = Zmod(pr)
m = Z(c).nth_root(0x10001)

print(l2b(int(m)))