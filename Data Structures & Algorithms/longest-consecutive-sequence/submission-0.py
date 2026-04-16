class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {v: i for i, v in enumerate(nums)}
        max_count = 0
        for h in hm.keys():
            if h-1 not in hm.keys():
                count = 0
                start = h
                while start in hm.keys():
                    count += 1
                    start += 1
                if count > max_count:
                    max_count = count
        return max_count