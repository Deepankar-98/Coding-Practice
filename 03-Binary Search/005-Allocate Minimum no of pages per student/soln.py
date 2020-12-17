class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def isValid(self, arr, m, max_val):
        n_stud = 1
        total = 0
        
        for i in arr:
            total += i
            
            if total > max_val:
                n_stud += 1
                if n_stud > m:
                    return False
                total = i
        return True
    
    def books(self, A, B):
        # Corner Cases
        if len(A) < B:
            return -1
        elif len(A) == B:
            return max(A)
        elif len(A) == 1:
            return sum(A)
            
        start = max(A)
        end = sum(A)
        result = end
        
        while start <= end:
            mid = (start+end)//2
            
            if self.isValid(A,B, mid):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return result
        