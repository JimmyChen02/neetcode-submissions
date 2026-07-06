class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0 
        while l < r:
            diff = r - l
            curr = min(heights[r], heights[l]) * diff
            maximum = curr if curr > maximum else maximum
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return maximum