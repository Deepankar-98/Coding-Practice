class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Method 1:
        val = bin(A)[2:]
        i = val.rfind('1')
        return len(val) - i - 1
        
        
        
        # Method 2:
        lookup = [32, 0, 1, 26, 2, 23, 27, 0, 3, 16, 24, 30, 28, 11, 0, 13, 4, 7, 17, 0, 25, 22, 31, 15, 29, 10, 12, 6, 0, 21, 14, 9, 5, 20, 8, 19, 18]
        # Only difference between (x and -x) is the value of signed magnitude(leftmostbit) negative numbers signed bit is 1
        return lookup[(-A & A) % 37]
        
        
        
        # Method 3:
        return int(math.log(A & ~(A-1), 2))