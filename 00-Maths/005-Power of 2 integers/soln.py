import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
            
        factors = [i for i in range(2, int(m.sqrt(A))+1) if A % i == 0]
        for i in factors:
            # log gives the number of times we need to divide a number to get 1.
            # Here we are calculating log A base p
            # log A base p = (log A base 10) / (log p base 10)
            ret =  math.log(A)/math.log(i)
            if ret - int(ret) <= 0.0000001:
                return 1
    
        return 0