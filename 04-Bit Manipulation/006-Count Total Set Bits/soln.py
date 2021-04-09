class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        ret = 0
        power = 2
        ret += A//2 + A%2
        
        for i in range(1,32):
            ret += (A//(power*2)) * power
            remdr = A%(power*2)
            
            if remdr//power:
                ret += (remdr%power) + 1
            
            power *= 2
            ret = int(ret%(1e9+7))
        
        return int(ret%(1e9+7)) 