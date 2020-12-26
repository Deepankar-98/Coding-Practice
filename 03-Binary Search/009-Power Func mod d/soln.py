import math
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x > d:
            x = x%d
        
            
        res= 1
        
        while n > 0:
            if n & 1:   # Odd?
               res = (res * x) % d
               
            x = x**2 % d
            n >>= 1      # equiv to n m= n//2

        return res % d
            