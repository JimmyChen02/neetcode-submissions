class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        buckets = [] 
        for i in range(len(nums)+1):
            buckets.append([])
        for num, count in freq.items():
            buckets[count].append(num)
        i = len(buckets) - 1
        out = []
        while i >=0 and len(out) < k:
            if buckets[i] != []:
                for num in buckets[i]:
                    out.append(num)
                    if len(out) == k:
                        return out
            i -=1
        return out