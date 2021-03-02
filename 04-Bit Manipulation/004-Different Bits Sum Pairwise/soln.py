class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        N = len(A)
        
        ans = 0
        two_pwr = 1
        for j in range(32):
            ones = 0
            for e in A:
                if e & two_pwr:
                    ones += 1
            
            ans += 2 * ones * (N - ones) % (10**9 + 7)
            two_pwr *= 2
            
        return ans % (10**9 + 7)
		
		