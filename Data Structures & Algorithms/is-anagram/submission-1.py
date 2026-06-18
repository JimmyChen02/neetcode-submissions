class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            if char not in seen:
                return False
            seen[char] -=1 
        for key in seen:
            if seen[key] != 0:
                return False
        return True