class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if A == "":
            return 0
        
        # Creating PI table for KMP
        i = 0
        pi = [0] * len(B)
        for j in range(1, len(B)):
            if B[i] == B[j]:
                pi[j] = i + 1
                i += 1
        
        # Now performing string search:
        i = 0
        m = len(B)
        for k, j in enumerate(A):
            if j == B[i]:
                i += 1
                
            # j != B[i] is automatically derived
            elif i != 0:
                
                # Traversing pi table for getting i index.
                while i > 0:
                    i = pi[i-1]
                    if j == B[i]:
                        i += 1
                        break
                    
            # Exit condition on 1st match
            if i == m:
                return k - m + 1
                
        return -1