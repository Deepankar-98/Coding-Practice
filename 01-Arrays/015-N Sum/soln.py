from typing import List
class Solution:
    
    # The core is to implement a fast 2-pointer to solve 2-sum, 
    # and recursion to reduce the N-sum to 2-sum. 
    # Some optimization was be made knowing the list 
    # is sorted.
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNSums( nums, target, 4, [], results)
        return results
    
    # res_so_far contains the terms before this term.
    def findNSums (self, nums, target, N, res_so_far, results):
        # Base condition for recursion.
        if len(nums) < N or N < 2:
            return
    
        # 2-sum problem.
        if N == 2:
            # Using 2 pointer approach since we need the values.
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                # If sum == target.
                else:
                    results.append(res_so_far + [nums[l], nums[r]])
                    # We change both values as same values cant exist,
                    # else changing either values would do.
                    l += 1
                    r -= 1
                    
                    # Handling repeted elements.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        
        # Recursively handling case for N > 2 and reducing it to 2
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNSums(nums[i+1:], target-nums[i], N-1, res_so_far+[nums[i]], results)
        return
		
		
		