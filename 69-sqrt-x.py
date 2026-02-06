"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, 
return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Intuition - use binary search to find the square root of the number.

Time Complexity - O(log n)
Space Complexity - O(1)

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2,  x//2
        while l <= r:
            m = l + (r - l) // 2
            m_sq = m*m
            if m_sq > x:
                r = m - 1
            elif m_sq < x:
                l = m + 1
            else:
                return m
        return r