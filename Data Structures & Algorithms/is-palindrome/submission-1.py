class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                alpha += char.lower()
        l,r = 0, len(alpha)-1
        while l <= r:
            if alpha[l] != alpha[r]:
                return False
            l+= 1
            r-= 1
        return True