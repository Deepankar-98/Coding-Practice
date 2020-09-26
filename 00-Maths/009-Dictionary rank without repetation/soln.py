import math

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, s):

        s_asc = sorted(s)
        
        if s == ''.join(s_asc):
            return 1
        
        n = len(s_asc)
        rank = 0
        
        for i, j in enumerate(s):
            index = s_asc.index(j)
            rank += index * math.factorial(n-1)
            del s_asc[index]
            n -= 1
        return (rank + 1) % 1000003
    