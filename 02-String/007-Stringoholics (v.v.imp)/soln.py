# Solution 1 -- not good

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        len_arr = list(map(len, A))
        same_rotation = [-1] * len(A)
        n_true = 0
        prev_sum = 0
        count = 0
        
        while n_true != len(A):
            count += 1
            prev_sum += count
            
            for index, i in enumerate(A):
                if same_rotation[index] != -1:
                    continue
                
                mod = prev_sum % len_arr[index]
                if (i[mod:] + i[0: mod]) == i:
                    same_rotation[index] = count
                    n_true += 1
                    
        return self.get_lcm(same_rotation)


    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)



    def get_lcm(self, arr):
        if len(arr) == 1:
            return arr[0]

        first = arr[0]
        for i in arr[1:]:
            gcd = self.gcd(max(first, i), min(first, i))
            first = (first * i) // gcd
        
        return first

ob=Solution()
a= ['a','ababa','aba']
print(ob.solve(a))
   

# Solution 2:

#Check hint   