class Solution:
    
    def rotate(self, A):
    # if we observe carefully we are spiraling each level
        n = len(A)-1
        for spiral in range(n-1):
            for i in range(n-spiral):
                temp = A[n-i][i]
                A[n-i][i] = A[n][n-i]
                A[n][n-i] = A[i][n]
                A[i][n] = A[spiral][i]
                A[spiral][i] = temp
                
        return A