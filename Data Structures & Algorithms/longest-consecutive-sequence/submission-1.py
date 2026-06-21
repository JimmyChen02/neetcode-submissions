class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        longest = 0
        for num in seen:
            if num-1 not in seen: #means start
                curr = 1
                while num+1 in seen:
                    curr += 1
                    num += 1
                if curr > longest:
                    longest = curr
        return longest