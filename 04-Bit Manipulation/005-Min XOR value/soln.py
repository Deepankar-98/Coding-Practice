class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        
        # Taking the highest value as minimum xor initialy
        xor_min = A[-1]
        for i in range(len(A)-1):
            xor = A[i] ^ A[i+1]
            
            if xor == 0:
                return 0
            elif xor_min > xor:
                xor_min = xor
                
        return xor_min	
		
		