class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, a, b):
        # Corner cases
        flag = 0
        if a == b:
            return 1
        elif a == 0:
            return 0
        elif b == 1:
            return a
        elif a > 0 and b > 0:
            if b > a:
                return 0
        elif a < 0 and b < 0:
            a, b = -a, -b
        elif a < 0:
            flag = 1
            a = -a
        elif b < 0:
            flag = 1
            b = -b
			


        # Finding solution.
        int_max = 2**31 -1
        temp = b
        n = 1
        p = 0
        while a >= b and p <= int_max:
            if temp > a:
                temp >>= 1
                n >>= 1
                continue
                
            a -= temp
            p += n
            temp <<= 1
            n <<= 1
            
        if p > int_max:
            p = int_max
            
            
        if flag == 1:
            return -p
        else:
            return p
        
