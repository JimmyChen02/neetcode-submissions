class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        tot = 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                tot += lmax - height[l]
                l += 1
            else:
                tot += rmax - height[r]
                r -= 1
        return tot