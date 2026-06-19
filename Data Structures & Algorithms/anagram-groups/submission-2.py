class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            ordered = "".join(sorted(word))
            if ordered not in anagram:
                anagram[ordered] = []
            anagram[ordered].append(word)
        return list(anagram.values())