class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        for i in range(1, len(A) - 1):
            l, r = i - 1, i + 1
            while l >= 0:
                if A[l] < A[i]:
                    l -= 1
                else:
                    break
            while r < len(A):
                if A[r] > A[i]:
                    r += 1
                else:
                    break
            if l == -1 and r == len(A):
                return 1
        return 0