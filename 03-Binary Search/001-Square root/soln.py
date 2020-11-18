class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A <= 1:
            return A
            
        l,h = 1, A//2
        while l<=h:
            mid = l + (h-l)//2
            sq = mid * mid
            if sq == A:
                return mid
            elif sq < A:
                l = mid+1
            else:
                h = mid-1
        return mid if sq < A else mid-1