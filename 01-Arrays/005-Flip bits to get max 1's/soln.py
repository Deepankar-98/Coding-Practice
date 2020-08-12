class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    
    def solve(self, A, B):
        
        sum_arr = sum(B)
        
        if sum_arr % 3 != 0:
            return 0
        else:
            part_sum = sum_arr // 3
            
            
        prefix = []
        suffix = []
        
        
        # Finding the prefix array.
        cum_sum = 0
        for ind, val in enumerate(B):
            cum_sum += val
            if cum_sum == part_sum:
                prefix.append(ind)
                
                
        # Finding the suffix array.
        cum_sum = 0
        for ind, val in enumerate(B[::-1]):
            cum_sum += val
            if cum_sum == part_sum:
                suffix.append(A - ind - 1)
                
        if suffix or prefix:
            count = 0
            for i in prefix:
                for j in suffix:
                    if i < j-1 and sum(B[i+1:j]) == part_sum:
                        count += 1
            return count
        return 0
        