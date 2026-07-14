class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        letters = {}
        for char in s1:
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
        curr_window_letters = {}
        for i in range(len(s1)):
            if s2[i] not in curr_window_letters:
                curr_window_letters[s2[i]] = 0
            curr_window_letters[s2[i]] += 1
        if curr_window_letters == letters:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            if s2[r] not in curr_window_letters:
                curr_window_letters[s2[r]] = 0
            curr_window_letters[s2[r]] += 1
            curr_window_letters[s2[l]] -= 1
            if curr_window_letters[s2[l]] == 0:
                del curr_window_letters[s2[l]]
            l += 1
            if curr_window_letters == letters:
                return True
        return False