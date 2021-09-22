# euclid writeup

In this task, we are given 50 values of `n * k + e`, where `n` (technically prime `p`): 2048-bit, nonce `k`: 1024-bit, and error `e`: 768-bit.

As stated in [1], we have sufficient information to recover `n` by using GACD (General Approximate Common Divisor).

Once we construct a lattice and reduce it via LLL, the result gives us a set of linear equations satisfied by error terms (`e`'s).

In [1], it says that we need to construct a lattice spanned by the row vectors from both homogeneous solution and particular solution and then reduce it once more to recover error terms.

In this challenge, however, one can easily find that we don't actually need to, since null space of the matrix is zero vector space.

That is, we can just use particular solution as the shortest vector in the lattice of solution space.

Once you get the error terms, you can easily recover `n` (or `p`) by Euclidean algorithm.


**Flag: `FLAG{gcd_in_2021s}`**


# Reference
[1] J Ding. A New Algorithm for Solving the General Approximate Common Divisors Problem and Cryptanalysis of the FHE Based on the GACD problem