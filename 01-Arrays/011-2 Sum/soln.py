from typing import List
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # current value: index
        hashtable = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if hashtable.get(diff, -1) >= 0:
                return [hashtable[diff], i]
            else:
                hashtable[v] = i
                