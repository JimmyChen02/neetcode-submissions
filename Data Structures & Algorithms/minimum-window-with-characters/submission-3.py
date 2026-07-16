class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        need = {}
        for char in t:
            if char not in need:
                need[char] = 0
            need[char] += 1

        window = {}
        have = 0
        req = len(need)
        l = 0
        res = ""
        for r in range(len(s)):
            char = s[r] 
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == req:
                current = s[l:r + 1]
                if res == "" or len(current) < len(res):
                    res = current
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
        return res