# This solution is based on 2 pointers approach.
# Assume j, k to be 2 pointers left and right.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()
        hashmap = {}
        for i in range(n):
            a = nums[i]
            j = i + 1
            k = n-1
            
            while (j < k):
                b = nums[j]
                c = nums[k]
                s = (a + b + c)
                
                if s == 0:
                    hashmap.setdefault((a, b, c), 1)
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return [ list(i) for i in hashmap.keys()]
         