class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps =0
        for i in range(len(A)-1):
            d_x = abs(A[i]-A[i+1])
            d_y = abs(B[i]-B[i+1])
            steps += min(d_x, d_y) + abs(d_x - d_y)
        return steps
