class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        pascals = []
        
        for i in range(A):

            s = []
            for j in range (i+1):
                
                if j ==0 or j == i:
                    s += [1]

                else:
                    s += [pascals[i-1][j-1] + pascals[i-1][j]]

            pascals.append(s)

        return pascals
