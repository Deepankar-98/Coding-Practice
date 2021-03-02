class Solution:
    # Returns no: of 0's
    def f(self, x):
        i=1
        c=0
        while x >= i:
            i *= 5
            c += x//i
        return c
        
    # Using Binary search.. 
    # Note no: of 2's is always grater than no: of 5's,
    # so finding no: of 5's s sufficient for finding 0's.
    # And also there are either 5 number with K no: of 0's, or none at all.
	# Runtime -- 28 ms, space -- 14 MB
	# Complexity -- log (base 2) K * log (base 5) K
    def preimageSizeFZF(self, K: int) -> int:
        n_5 = 0
        l = K
        h = K*5
        while l <= h:
            m = (l+h)//2
            n_5 = self.f(m)
            if n_5 == K:
                return 5
            elif K > n_5:
                l = m+1
            else:
                h = m-1
        return 0



	# Trying to remove binary search and using GP
	# S = x/5 + x/25 + x/125 + . . . 
	# 5S = x + (x/5 + x/25 + x/125 + . . .)
	# Hence, S = x/4
	# approx error in calculation: log (base 5) K + 1
	# Method not advised for interviews -- Runtime: 32 ms
	def preimageSizeFZF(self, K: int) -> int:
        x = 4 * K
        while self.f(x) < K:
            x += 5
        return 5 if self.f(x) == K else 0

ob = Solution()
K = 25
# print(ob.f(25*5))
print(ob.preimageSizeFZF(K))