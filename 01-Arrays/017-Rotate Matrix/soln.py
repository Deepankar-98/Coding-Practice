class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    
    def rotate(self, A):
    # if we observe carefully we are spiraling each level
        n = len(A)
        if n== 1:
            return A
        
        k= n//2
        n-=1
            
        for spiral in range(k):
            lo, hi = spiral, n - spiral
            for i in range(hi-lo):
                temp = A[lo][lo+i]
                A[lo][lo+i] = A[hi-i][lo]
                A[hi-i][lo] = A[hi][hi-i]
                A[hi][hi-i] = A[lo+i][hi]
                A[lo+i][hi] = temp
                
        return A