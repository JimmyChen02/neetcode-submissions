class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1
            if (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest