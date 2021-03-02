class Solution:
    # @param A : string
    # @return a list of integers
    
    def flip(self, A):
        # Replace 1 with -1 & 0 with 1.
        a = [-1 if i == '1' else 1 for i in A]
        
        # Now applying Kedane's Algo
        max_so_far = 0
        curr_max = 0
        start = -1
        end = -1
        temp_start = 0
        
        
        # All negeive case, i.e., all 1's were present
        if max(a) < 0:
            return []
            

        # Using kedane Algo
        for i, v in  enumerate(a):
            max_so_far = max_so_far + v
            if max_so_far < 0:
                max_so_far = 0
                temp_start = i+1
            
            elif max_so_far > curr_max:
                curr_max = max_so_far
                start = temp_start
                end = i

        return [start+1, end+1]
        
