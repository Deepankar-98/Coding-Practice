from math import factorial as f
def nCr(n,r):
    return f(n)//(f(r)*f(n-r))
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return nCr((A+B-2),A-1)