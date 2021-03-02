class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        dup = -1
        num_set = set()
        
        # Using set data structure
        for i in A:
            if i in num_set:
                dup = i
                break
            else:
                num_set.add(i)
                
        return dup