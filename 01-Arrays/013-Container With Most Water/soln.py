class Solution(object):
    def maxArea(self, height):
        begin = 0
        end = len(height) - 1
        res = (end - begin) * min(height[end], height[begin])
        while begin != end:
            if height[begin] <= height[end]:
                begin += 1
            else:
                end -= 1
            current = (end - begin) * min(height[end], height[begin])
            if current > res:
                res = current
        return res