class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
        
    def cpFact(self, A, B):
        def gcd (x, y):
            if x == 0:
                return y
            return gcd (y%x, x)
            
            
        while gcd (A,B)!=1:
            A = A//gcd(A,B)
        return int(A)